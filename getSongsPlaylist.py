from ytmusicapi import YTMusic
import json

ytmusic = YTMusic("oauth.json")

try:
    liked = ytmusic.get_liked_songs(limit=10000)

    songs = liked.get("tracks", [])

    # Extrai os nomes e links das músicas
    songs_info = [{"title": song.get("title", "unknown"), "link": f'https://www.youtube.com/watch?v={song.get("videoId", "No link")}'}
                  for song in songs]
    song_names, song_links = zip(*[(info["title"], info["link"]) for info in songs_info]) if songs_info else ([], [])

    # Salva os dados em um arquivo JSON
    data_to_save = {"songs": [{"title": name, "link": link} for name, link in zip(song_names, song_links)],
                   "total": len(song_names)}

    with open("liked_songs_data.json", "w", encoding="utf-8") as json_file:
        json.dump(data_to_save, json_file, ensure_ascii=False, indent=2)

    print(f"Músicas curtidas: {song_names}, Links: {song_links}, Total: {len(song_names)}")
    print("Dados salvos em liked_songs_data.json")

except Exception as e:
    print(f"An error occurred: {e}")
