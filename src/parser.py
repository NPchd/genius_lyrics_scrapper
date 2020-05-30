import re

def parser_solo_lyrics(lyrics):
    regex = (r"\[.*?\]")
    lyrics = re.sub(regex, "", lyrics)
    return(lyrics)

def parser_feat_lyrics(lyrics, artist):
    parsed_lyrics = ""

    regex_title = (r"(\[.*?Paroles.*?\])")
    lyrics = re.sub(regex_title, "", lyrics)
    regex_artist = (r"(?=({artist}.*?\]))")
    regex_artist = regex_artist.format(artist = artist)
    regex_lyrics = (r"(?=({artist}.{range}?\]))(.*?)(?=\[)")
    regex_lyrics = regex_lyrics.format(artist = artist, range = "{0,20}")
    lyrics = lyrics.replace("\n", " - ")
    result_lyrics = re.findall(regex_lyrics, lyrics)
    if(result_lyrics):
        for result in result_lyrics:
            parsed_lyrics += result[1]
            parsed_lyrics = parsed_lyrics.replace(result[0], "")
            parsed_lyrics = parsed_lyrics.replace(" - ", "\n")
    return(parsed_lyrics)
