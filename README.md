🍽️ Restaurant Recommender App
This repository contains a simple, yet effective, restaurant recommendation system built with Python, Pandas, and Streamlit. The application allows users to find similar restaurants based on a chosen restaurant, city, and/or cuisine.

🌟 Features
Restaurant-Based Recommendations: Select a specific restaurant to find others with similar cuisines and in the same city.

City & Cuisine Filtering: Refine your search by specifying a city and/or a cuisine.

Intuitive UI: A clean and user-friendly interface built with Streamlit makes the app easy to navigate.

🚀 How to Run the App
Prerequisites
You'll need to have Python installed on your machine. You can then install the required libraries using pip:

pip install pandas numpy streamlit scikit-learn

Setup
Clone the repository:

git clone <your-repository-url>
cd <your-repository-name>

Ensure you have the data and pickle files:

Make sure your project structure looks like this:

/your-project-name
|-- app.py
|-- Restaurant.ipynb
|-- restaurants.pkl
|-- similarity.pkl
|-- data/
    |-- Dataset.csv

The Restaurant.ipynb notebook is used to preprocess the data and create two pickle files: restaurants.pkl and similarity.pkl. You'll need to run this notebook first to generate these files, which will be saved in the root directory of your project.

Open the notebook and run all the cells. This will save the necessary files to your project directory.

Running the App
Once you have the prerequisite libraries and the necessary pickle files, you can run the Streamlit app with this simple command:

streamlit run app.py

Your app will automatically open in your web browser.

📂 Project Structure
.
├── app.py
├── data/
│   └── Dataset.csv
├── Restaurant.ipynb
├── restaurants.pkl
└── similarity.pkl

app.py: The main Streamlit application file.

Restaurant.ipynb: A Jupyter Notebook for data preprocessing.

data/Dataset.csv: The raw dataset used for the recommendations.

restaurants.pkl: A pickled file of the preprocessed restaurant data.

similarity.pkl: A pickled file containing the cosine similarity matrix.

🙏 Acknowledgments
This project was inspired by the need for a simple and effective way to discover new dining experiences.

📝 License
This project is open-source and available under the MIT License.