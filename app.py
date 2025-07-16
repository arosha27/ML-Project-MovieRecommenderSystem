import streamlit as st
import pickle
import pandas as pd
import requests
import gdown
import os

#fetch poster
def fetch_poster(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=7549a08b1176533e26488ebcdb0fddc3".format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/original" + data['poster_path']


# recommend function to recommend the five movies
def recommend(movie):
    movie_index = movies[movies["title"] == movie].index[0]
    distances = similarity[movie_index]
    similar_five = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in similar_five:
         movie_id = movies.iloc[i[0]].movie_id
         recommended_movies.append(movies.iloc[i[0]].title)
         #fetch poster from API
         recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies , recommended_movies_posters


#3rd
#movies.pkl file contains a dataframe with three columns movie_id , title and tags .It has been dumped through pickle
movies = pickle.load(open("movies.pkl","rb")) #movies_list is now new_df
movies_list = movies["title"].values #values of title column in movies_list dataframe are stored in movies_lists

# Only download if file is not already there
if not os.path.exists("similarity.pkl"):
    url = "https://drive.google.com/uc?id=1HlHIZ6ao64xgsX71q2rWYHQxQ0ipR50Q"
    gdown.download(url, "similarity.pkl", quiet=False)

# Now load it
similarity = pickle.load(open("similarity.pkl", "rb"))

#ist - setting title
st.title("Movie Recommender System")

#2nd - selectbox showing total movies list
selected_movie_name= st.selectbox(
    "Choose the movie you want to get recommendations for?",
    movies_list)


# #recommend button
if st.button("Recommend"):

    names , posters =  recommend(selected_movie_name)

    col1 , col2, col3, col4, col5 = st.columns(5)

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






