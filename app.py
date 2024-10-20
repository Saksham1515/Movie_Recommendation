import pickle
import streamlit as st
import requests
import pandas as pd

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    response = requests.get(url)
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" +  data['poster_path']
movies_dict = pickle.load(open('movies_dict.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))
movies = pd.DataFrame(movies_dict)
#print(movies)


def recommend(movie):
    index=movies[movies['title']==movie].index[0]
    #print(index)
    movies_list=sorted(list(enumerate(similarity[index])),reverse=True,key=lambda x:x[1])[1:6]
    #print(movies_list)
    recommended_movie_name = []
    recommended_movie_poster = []
    for i in movies_list:
        movies_id = movies.iloc[i[0]].movie_id
        recommended_movie_name.append(movies.iloc[i[0]].title)
        recommended_movie_poster.append(fetch_poster(movies_id))
    #print(recommended_movie_name)
    #print(recommended_movie_poster)
    return recommended_movie_name,recommended_movie_poster


st.header('Movie Recommender System')
selected_movie_name = st.selectbox("Type or select a movie from the dropdown",movies['title'].values)

if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])