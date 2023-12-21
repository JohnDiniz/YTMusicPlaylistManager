from ytmusicapi import YTMusic
import json

def read_json_file(file_path):
    with open(file_path, "r", encoding="utf-8") as json_file:
        data = json.load(json_file)
    return data

def create_playlist(ytmusic, title, description, video_ids):
    playlist_id = ytmusic.create_playlist(title=title, description=description, privacy_status='PRIVATE', video_ids=video_ids)
    return playlist_id

try:
    # Leitura do arquivo JSON
    liked_songs_data = read_json_file("liked_songs_data.json")

    # Verifica se há músicas na lista
    if "songs" in liked_songs_data and liked_songs_data["songs"]:
        # Obtém a lista de IDs dos vídeos
        video_ids = [song["link"].split('=')[1] for song in liked_songs_data["songs"]]

        # Inicializa a instância da classe YTMusic
        ytmusic = YTMusic("oauth.json")

        # Cria a playlist no YouTube
        playlist_title = "YOUR_PLAYLIST_TITLE"
        playlist_description = "YOUR_PLAYLIST_DESCRIPTION"
        playlist_id = create_playlist(ytmusic, playlist_title, playlist_description, video_ids)

        print(f"Playlist criada com sucesso! ID da Playlist: {playlist_id}")

    else:
        print("Nenhuma música encontrada para criar a playlist.")

except Exception as e:
    print(f"An error occurred: {e}")
