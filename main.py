import streamlit as st
import pickle as pk
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_id = '7423351cb98a497eb3bc8604e3a9bc2b'
client_secret = '842760769cc54fff9322eb8c7a161036'

client_credentials_manager = SpotifyClientCredentials(
    client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

page_bg_img = """
<style>
[data-testid="stAppViewContainer"]{
background-image:url("https://static.vecteezy.com/system/resources/previews/003/559/330/original/abstract-background-with-gradient-blue-bubble-free-vector.jpg");
background-size:cover;
}
</style>
"""

# recommender


def recommend(musics):
    music_index = song_lst[song_lst['track_name'] == musics].index[0]
    distance = similar[music_index]
    music_list = sorted(list(enumerate(distance)),
                        reverse=True, key=lambda x: x[1])[1:6]

    recommSong = []
    recommPoster = []
    recommlink=[]

    for i in music_list:
        music_id = song_lst.iloc[i[0]].track_id
        track = sp.track(music_id)
        poster_image_url = track['album']['images'][2]['url']
        recommPoster.append(poster_image_url)
        recommSong.append(song_lst.iloc[i[0]].track_name)
        urls=track['external_urls']['spotify']
        recommlink.append(urls)

    return recommSong, recommPoster, recommlink


songs = pk.load(open("musics_list.pkl", "rb"))
song_lst = pd.DataFrame(songs)

similar = pk.load(open("similar.pkl", "rb"))

st.markdown(page_bg_img, unsafe_allow_html=True)
st.title("Discover Your perfect Music")

recommendMusic = st.selectbox(
    'Uplift Your Mood And Get Amazing Song',
    song_lst['track_name'].values)


if st.button("Recommend"):
    name, posters,spotifyurl = recommend(recommendMusic)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.markdown(f'[![Poster 1]({posters[0]})]({spotifyurl[0]})')
        # st.markdown(f'<a href="{spotifyurl[0]}" target="_blank">{st.image(posters[0])}</a>', unsafe_allow_html=True)
        st.write(name[0])

    with col2:
        st.markdown(f'[![Poster 1]({posters[1]})]({spotifyurl[1]})')
        st.write(name[1])
        
    with col3:
        st.markdown(f'[![Poster 1]({posters[2]})]({spotifyurl[2]})')
        st.write(name[2])
        
    with col4:
        st.markdown(f'[![Poster 1]({posters[3]})]({spotifyurl[3]})')
        st.write(name[3])
       
    with col5:
        st.markdown(f'[![Poster 1]({posters[4]})]({spotifyurl[4]})')
        st.write(name[4])
        
