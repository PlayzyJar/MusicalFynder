from time import sleep
import pandas as pd
import numpy as np

table = pd.read_excel("Músicas.xlsx")

musicName = artist = album = genre = releaseDate = spotifyMusic = spotifyArtist = ""

id = int(input("Digite o ID: "))

for index, row in table.iterrows():
    if row["ID"] == id:
        genre = row["Gênero(s)"]

for index, row in table.iterrows():
    if row["Gênero(s)"] == genre:
        musicName = row["Nome"]
        spotifyMusic = row["SpotifyMúsica"]
        print(f"{musicName} - {spotifyMusic}")
