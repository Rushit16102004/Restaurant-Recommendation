import streamlit as st
import pandas as pd
import pickle
from urllib.parse import quote

# ------------------------
# Helper functions
# ------------------------
def clean_city(city):
    if isinstance(city, list):
        return city[0] if city else ""
    return str(city).strip()

def join_address(addr):
    if isinstance(addr, list):
        return " ".join(str(a) for a in addr)
    return str(addr)

def recommend(restaurant_name=None, city_name=None, cuisine_name=None):
    global restaurants

    if restaurant_name:
        match = restaurants[
            restaurants["Restaurant Name"].str.lower() == restaurant_name.strip().lower()
        ]
        if match.empty:
            return pd.DataFrame()

        base_city = match.iloc[0]["City"]
        base_cuisines = set(c.strip().lower() for c in match.iloc[0]["Cuisines"].split(",") if c.strip())

        df_filtered = restaurants.copy()

        if city_name or cuisine_name:
            if cuisine_name:
                cuisine_lower = cuisine_name.strip().lower()
                df_filtered = df_filtered[
                    df_filtered["Cuisines"].str.lower().str.contains(cuisine_lower)
                ]
            else:
                df_filtered = df_filtered[
                    df_filtered["Cuisines"].apply(
                        lambda x: not base_cuisines.isdisjoint(
                            set(c.strip().lower() for c in x.split(",") if c.strip())
                        )
                    )
                ]

            if not city_name:
                city_name = base_city

            if city_name:
                city_lower = city_name.strip().lower()
                df_filtered = df_filtered[
                    df_filtered["City"].str.lower() == city_lower
                ]
        else:
            df_filtered = df_filtered[
                df_filtered["City"].str.lower() == str(base_city).lower()
            ]
            df_filtered = df_filtered[
                df_filtered["Cuisines"].apply(
                    lambda x: not base_cuisines.isdisjoint(
                        set(c.strip().lower() for c in x.split(",") if c.strip())
                    )
                )
            ]

        df_filtered = df_filtered[
            df_filtered["Restaurant Name"].str.lower() != restaurant_name.strip().lower()
        ]

    else:
        filters = []
        if city_name:
            filters.append(("City", city_name))
        if cuisine_name:
            filters.append(("Cuisines", cuisine_name))

        if len(filters) < 2:
            st.warning("⚠ Please enter at least two filters: Restaurant Name, City, or Cuisines.")
            return pd.DataFrame()

        df_filtered = restaurants.copy()
        for col, val in filters:
            val = str(val).strip().lower()
            df_filtered = df_filtered[df_filtered[col].astype(str).str.lower().str.contains(val)]

    return df_filtered

def top_recommendations(df, n=7):
    return df.sort_values(by="Aggregate rating", ascending=False).head(n)

def render_card(row):
    rating_percent = (row['Aggregate rating'] / 5) * 100
    address_query = quote(row['Address'])
    st.markdown(f"""
        <div class='restaurant-card'>
            <h4>🍴 {row['Restaurant Name']}</h4>
            <p>📍 <a href="https://www.google.com/maps/search/?api=1&query={address_query}" target="_blank" style="color: #00acee; text-decoration: underline;">{row['Address']}</a></p>
            <p>🍽 {row['Cuisines']}</p>
            <p>⭐ {row['Aggregate rating']}</p>
            <div class='rating-bar' style='width:{rating_percent}%;'></div>
        </div>
    """, unsafe_allow_html=True)

# ------------------------
# Load data
# ------------------------
with open("restaurants.pkl", "rb") as f:
    restaurants_dict = pickle.load(f)

restaurants = pd.DataFrame(restaurants_dict)

restaurants["City"] = restaurants["City"].apply(clean_city)
restaurants["Cuisines"] = restaurants["Cuisines"].apply(
    lambda x: ", ".join(x) if isinstance(x, list) else str(x)
)
restaurants["Address"] = restaurants["Address"].apply(join_address)

# ------------------------
# Streamlit UI (Dark Theme)
# ------------------------
st.set_page_config(page_title="🍽 Restaurant Search", layout="wide", page_icon="🍴")

st.markdown("""
    <style>
    body {background-color: #0e1117; color: white;}
    .stApp {background-color: #0e1117;}
    h1, h2, h3, h4, h5, h6 {color: #f5f5f5;}
    .restaurant-card {
        background-color: #1e222b;
        padding: 15px;
        border-radius: 12px;
        margin-bottom: 12px;
        transition: all 0.2s ease-in-out;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.3);
    }
    .restaurant-card:hover {
        background-color: #2c313c;
        transform: scale(1.02);
    }
    .rating-bar {
        height: 10px;
        border-radius: 5px;
        background: linear-gradient(90deg, gold, orange);
    }
    </style>
""", unsafe_allow_html=True)

st.title("🍽 Restaurant Search App")

# Prepare selectbox options
restaurant_names = sorted(restaurants["Restaurant Name"].dropna().unique().tolist())
restaurant_names = [name for name in restaurant_names if name.strip().lower() != "shree rathnam"]

city_list = [""] + sorted(restaurants["City"].dropna().unique().tolist())
cuisine_options = sorted(set(
    c.strip() for sublist in restaurants["Cuisines"].dropna().apply(lambda x: x.split(",")) for c in sublist
))

# Search filters
col1, col2, col3 = st.columns(3)
with col1:
    restaurant_input = st.selectbox("🏢 Restaurant Name (optional)", [""] + restaurant_names, help="Pick a restaurant to find similar ones")
with col2:
    city_input = st.selectbox("🌆 City Name (optional)", city_list, help="Filter by city")
with col3:
    cuisine_input = st.selectbox("🍜 Cuisine Name (optional)", [""] + cuisine_options, help="Filter by cuisine")

# Search button
if st.button("🔍 Search"):
    recommendations = recommend(restaurant_input, city_input, cuisine_input)

    if not recommendations.empty:
        top_recs = top_recommendations(recommendations)
        st.subheader("✨ Top Recommendations for You")
        for _, row in top_recs.iterrows():
            render_card(row)
    else:
        st.warning("❌ No restaurants found matching your filters.")