import streamlit as st
import pickle
import gzip
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get(
        f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=0f6ef77b185e4ce4b597488cd3ac770c&language=en-US'
    )
    data = response.json()
    if 'poster_path' in data and data['poster_path']:
        return "https://image.tmdb.org/t/p/original/" + data['poster_path']
    return "https://via.placeholder.com/500x750?text=No+Poster"

def recommend(selected_movie_name):
    # Find the index of the movie from the movie DataFrame based on title
    movie_index = movies[movies['title'] == selected_movie_name].index[0]

    # Get the similarity scores for the movie at movie_index
    distances = similiarity[movie_index]

    # Get the top 5 most similar movies (excluding the first one as it's the movie itself)
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []

    # Get the titles and posters of the recommended movies
    for i in movies_list:
        # Use 'id' or appropriate column for the unique movie identifier
        movie_id = movies.iloc[i[0]].id  # Replace 'id' with the correct column if different
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_movies_posters


# Load pre-trained data
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

# Check if the 'id' column exists; if not, raise an error
if 'id' not in movies.columns:
    raise ValueError("The 'id' column is missing from the dataset. Ensure your dataset includes a unique identifier for each movie.")


# Load the compressed similiarity matrix
with gzip.open('similiarity.pkl.gz', 'rb') as f:
    similiarity = pickle.load(f)

# Streamlit interface
st.title('Movie Recommender System')

selected_movie_name = st.selectbox("Select a movie to get recommendations:", movies['title'].values)

if st.button("Recommend"):
    try:
        names, posters = recommend(selected_movie_name)
        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            st.text(names[0])
            st.image(posters[0])

        with col2:
            st.text(names[1])
            st.image(posters[1])

        with col3:
            st.text(names[2])
            st.image(posters[2])

        with col4:
            st.text(names[3])
            st.image(posters[3])

        with col5:
            st.text(names[4])
            st.image(posters[4])
    except Exception as e:
        st.error(f"An error occurred: {e}")
