import streamlit as st
import pickle
import wikipedia

movies = pickle.load(open('movies_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
movies_list = movies['title'].values

st.header('Consigli film')
select_value = st.selectbox('Seleziona un film', movies_list)

def recommend(movies_data):
    index = movies[movies['title']==movies_data].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector:vector[1])
    recommend_movie = []
    for i in distance[1:6]:
        recommend_movie.append(movies.iloc[i[0]].title)
    return recommend_movie

def get_info(topic):
    try:
        wikipedia.set_lang('it')
        page = wikipedia.summary(topic, sentences=2)
        return page
    except wikipedia.exceptions.PageError:
        return f"Nessuna informazione disponibile per {topic}."

if st.button('Consiglia'):
    movie_name = recommend(select_value)
    c = st.container()
    for i in range(0, 5):
        c.write(movie_name[i] + ": " + get_info(movie_name[i]))





