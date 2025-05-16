🎬 Movie Recommendation System

This project implements a Content-Based Movie Recommendation System that suggests movies similar to those a user likes, based on movie metadata such as genres, cast, and keywords. It uses natural language processing and vector-based similarity to provide real-time recommendations through an interactive Streamlit web app.

📦 Project Overview
Utilized the TMDB dataset, containing over 5,000 movie entries.

Cleaned and processed data using Pandas, extracting features like genres, cast, crew, and keywords.

Combined relevant text fields into a single feature for each movie.

Applied NLTK for text preprocessing (e.g., stemming, stopword removal).

Transformed text into vectors using CountVectorizer.

Calculated cosine similarity between movies to find the most similar ones.

Built a clean, responsive interface using Streamlit to display top recommendations.

🔧 Tech Stack
Python

Pandas, NumPy

NLTK for text processing

Scikit-learn for vectorization and similarity calculations

Streamlit for web deployment

🚀 How to Run
bash
Copy
Edit
# Clone the repository
git clone https://github.com/YourUsername/Movie-Recommender-System.git
cd Movie-Recommender-System

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py
✅ Features
Enter any movie title and get top 5–10 similar movies.

Recommendations are based on content similarity (not user ratings).

Real-time predictions with fast performance and a clean UI.

Easily customizable to support other datasets or new similarity metrics.
