# 🍽️ Restaurant Recommender App

A simple and effective restaurant recommendation system built with **Python**, **Pandas**, and **Streamlit**. This app allows users to discover restaurants similar to a chosen restaurant, filtered by city and/or cuisine.  

---

## 🌟 Features

- **Restaurant-Based Recommendations**: Select a specific restaurant to find others with similar cuisines and in the same city.  
- **City & Cuisine Filtering**: Refine your search by specifying a city and/or a cuisine.  
- **Intuitive UI**: A clean, user-friendly interface built with Streamlit.  

---

## 🚀 How to Run the App

### Prerequisites
Make sure you have **Python** installed. Then install the required libraries:

bash pip install pandas numpy streamlit scikit-learn

--- 

## 🚀 Setup

### Clone the Repository
        bash
        git clone <your-repository-url>
        cd <your-repository-name>

* Ensure you have the data and pickle files:

* Make sure your project structure looks like this:

        /your-project-name
        |-- app.py
        |-- Restaurant.ipynb
        |-- restaurants.pkl
        |-- similarity.pkl        
        |-- data/
            |-- Dataset.csv

* The Restaurant.ipynb notebook is used to preprocess the data and create two pickle files: restaurants.pkl and similarity.pkl. You'll need to run this notebook first to generate these files, which will be saved in the root directory of your project.

* Open the notebook and run all the cells. This will save the necessary files to your project directory.

 * Running the App
Once you have the prerequisite libraries and the necessary pickle files, you can run the Streamlit app with this simple command:

* streamlit run app.py

* Your app will automatically open in your web browser.

---

## 📂 Project Structure

        ├── app.py
        ├── data/
        │   └── Dataset.csv
        ├── Restaurant.ipynb
        ├── restaurants.pkl
        └── similarity.pkl

* app.py: The main Streamlit application file.

* Restaurant.ipynb: A Jupyter Notebook for data preprocessing.

* data/Dataset.csv: The raw dataset used for the recommendations.

* restaurants.pkl: A pickled file of the preprocessed restaurant data.

* similarity.pkl: A pickled file containing the cosine similarity matrix.

---

## 🙏 Acknowledgments
* This project was inspired by the need for a simple and effective way to discover new dining experiences.

---

## 📝 License
* This project is open-source and available under the MIT License.
