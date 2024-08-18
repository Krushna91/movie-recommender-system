import streamlit as st
import pickle
import pandas as pd
import requests

# Function to fetch the poster URL using the movie ID
def fetch_poster(movie_id):
    api_key = '1cb623e79b00986ecea3db79e9f6e538'
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        poster_path = data.get('poster_path')
        if poster_path:
            return f"https://image.tmdb.org/t/p/w500{poster_path}"
        else:
            return None
    else:
        st.error(f"Error fetching poster for movie ID {movie_id}")
        return None

# Function to recommend movies based on similarity
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_poster = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        poster = fetch_poster(movie_id)
        recommended_movies_poster.append(poster)

    return recommended_movies, recommended_movies_poster

# Load movie data and similarity matrix
movie_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Streamlit app
st.title('🎬 Movie Recommender System')

selected_movie = st.selectbox('🎥 Pick your movie', movies['title'].values)

if st.button('Recommend'):
    names, posters = recommend(selected_movie)

    # Display recommended movies and posters in a horizontal layout
    cols = st.columns(5)

    for i in range(5):
        with cols[i]:
            st.image(posters[i], use_column_width=True)
            st.text(names[i])
