import requests
import string
import re
import os.path
from bs4 import BeautifulSoup

from parser import *
from add_file import *

URL_GENIUS_TRACKS = "https://genius.com/api/artists/{id_artist}/songs?page={index_page}&sort=popularity"
URL_GENIUS_TRACK = "https://genius.com{track}"

months = ["January","February","March","April", "May", "June", "July", "August", "September", "October", "November", "December"]

def check_feat(title):
    result = True if ("Ft." in title or " x " in title) else False
    return result

def check_author(author, artist):
    result = True if (author != artist) else False
    return result

def main():
    with open("../Artist.csv", "r", encoding="utf-8") as csv_artist:
        reader = csv.DictReader(csv_artist)
        for row in reader:
            index_page = 1
            artist = row["artist_name"]
            id_artist = row["artist_id"]
            #Format the URL with artist ID
            pages_tracks = URL_GENIUS_TRACKS.format(id_artist = id_artist, index_page = index_page)
            #Get the page with artist tracks
            result_tracks = requests.get(pages_tracks)
            soup_tracks = result_tracks.json()["response"]
            while soup_tracks["songs"]:
                for song in soup_tracks["songs"]:
                    #Format the URL with track path
                    page_track = URL_GENIUS_TRACK.format(track = song["path"])
                    #Get the track page
                    result_track = requests.get(page_track)
                    soup_track = BeautifulSoup(result_track.content, "html.parser")
                    #Extract the lyrics
                    lyrics = soup_track.find("div", class_="lyrics")
                    items = soup_track.find_all("span", class_="metadata_unit-info metadata_unit-info--text_only")
                    for item in items:
                        if any(month in item.text for month in months):
                            date = item.text
                    if(lyrics != None):
                        if(check_feat(song["full_title"]) or check_author(song["primary_artist"]["name"], artist)):
                            result_parser = parser_feat_lyrics(lyrics.text, artist)
                            add_lyrics_csv(result_parser, song["full_title"], song["primary_artist"]["name"], date, artist)
                        else:
                            result_parser = parser_solo_lyrics(lyrics.text)
                            add_lyrics_csv(result_parser, song["full_title"], song["primary_artist"]["name"], date, artist)
                index_page+=1
                #Format the URL with artist ID and page index
                pages_tracks = URL_GENIUS_TRACKS.format(id_artist = id_artist, index_page = index_page)
                #Get the page with artist tracks
                result_tracks = requests.get(pages_tracks)
                soup_tracks = result_tracks.json()["response"]

if __name__ == "__main__":
    main()
