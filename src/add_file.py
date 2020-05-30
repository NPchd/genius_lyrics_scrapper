import json
import csv

def add_lyrics_json(lyrics, title, artist_track, date, artist):
    file_name = "../" + artist + ".json"
    data = {}
    data["tracks"] = []
    data["tracks"].append({
        "name": title,
        "date": date,
        "author": artist_track,
        "lyrics": lyrics
    })
    try:
        with open(file_name, "r") as artist_file:
            data_file = json.load(artist_file)
            data_file["tracks"].append(data["tracks"][0])
            data = data_file
    except FileNotFoundError as exc:
        pass
    with open(file_name, "w") as json_file:
        json.dump(data, json_file, ensure_ascii=False)

def add_lyrics_csv(lyrics, title, artist_track, date, artist):
    file_name = "../" + artist + ".csv"
    file_exists = os.path.isfile(file_name)
    with open(file_name, "a") as csv_file:
        headers = ["name", "date", "author", "lyrics"]
        writer = csv.DictWriter(csv_file, delimiter=",", lineterminator="\n", fieldnames=headers)
        if not file_exists:
            writer.writeheader()
        writer.writerow({"name": title, "date":date, "author":artist_track, "lyrics":lyrics})