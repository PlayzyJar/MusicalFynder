from time import sleep
import pandas as pd
import numpy as np

table = pd.read_excel("Músicas.xlsx")

name = artist = album = genre = releaseDate = spotifyMusic = spotifyArtist = ""

id = int(input("Digite o ID: "))

for index, row in table.iterrows():
    if row["ID"] == id:
        name = row["Nome"]
        artist = row["Artista(s)"]
        album = row["Álbum"]
        genre = row["Gênero(s)"]
        releaseDate = row["Lançamento"]
        spotifyMusic = row["SpotifyMúsica"]
        spotifyArtist = row["SpotifyArtista"]

print("Processando", end="")
for i in range(3):
    sleep(1)
    print(".", end="")


print()
print("=-="*15)
print(f"Nome: {name}")
print(f"Data de Lançamento: {releaseDate}")
print(f"Artista(s): {artist}")
print(f"Álbum: {album}")
print(f"Gênero: {genre}")
print(f"Spotify Música: {spotifyMusic}")
print(f"Spotify Artista: {spotifyArtist}")
