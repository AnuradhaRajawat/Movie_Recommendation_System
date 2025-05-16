# 🎬 Movie Recommendation System
This project implements a  **Content-Based Movie Recommendation System** that suggests movies similar to a user’s choice based on movie metadata such as **genres, cast, and keywords**. It leverages natural language processing and vector similarity to deliver real-time recommendations through an interactive Streamlit web app.

# 📦 Project Overview
- Utilized the TMDB dataset, containing over 5,000 movie entries.

- Cleaned and processed data using Pandas, extracting features like genres, cast, crew, and keywords.

- Combined relevant text fields into a single composite feature for each movie.

- Applied NLTK for text preprocessing including stemming and stopword removal.

- Converted textual data into vectors using CountVectorizer.

- Calculated cosine similarity between movies to find the most relevant recommendations.

- Developed a clean and responsive interface using Streamlit to display top recommendations.

# 🔧 Tech Stack
Python, Pandas, NumPy, NLTK (Natural Language Toolkit), Scikit-learn, Streamlit

# 🚀 How to Run
- Clone the repository
  - git clone https://github.com/YourUsername/Movie-Recommender-System.git
   cd Movie-Recommender-System

- Install dependencies
   - pip install -r requirements.txt

# Run the Streamlit application
streamlit run app.py
# ✅ Features
Enter any movie title and get the top 5–10 similar movies instantly.

Recommendations are based purely on content similarity, not on user ratings or reviews.

Real-time, fast predictions with a clean, user-friendly interface.

Easily extendable to support new datasets or different similarity measures.
