import pandas as pd
from PySimpleGUI import PySimpleGUI as sg

table = pd.read_excel("ProjetoFinderMusical/Músicas.xlsx")

origin = musicName = artist = album = genre = releaseDate = spotifyMusic = spotifyArtist = ""
artists = []
spotifys = []

sg.theme('Reddit')
layout = [
    [sg.Text("ID do Artista:"), sg.Input(key="id", size=(20, 1))],
    [sg.Button("Selecionar Artista")],
]
janela = sg.Window('Projeto TCC', layout)

while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == "Selecionar Artista":
        id = valores["id"]
        id = int(id)

        for index, row in table.iterrows():
            if row["ID"] == id:
                artist = row["Artista(s)"]

        layout = [
            [sg.Text("Artista Selecionado: " + artist)],
            [sg.Button("Listar Informações do Artista")],
            [sg.Button("Listar Músicas do Artista")],
            [sg.Button("Listar Músicas do Gênero")],
            [sg.Button("Listar Artistas do Gênero")],
            [sg.Button("Selecionar Outro Artista")],
        ]
        janela.close()
        janela = sg.Window('Projeto TCC', layout)
        eventos, valores = janela.read()

    if eventos == "Listar Informações do Artista":
        for index, row in table.iterrows():
            if row["ID"] == id:
                artist = row["Artista(s)"]
                genre = row["Gênero(s)"]
                spotifyArtist = row["SpotifyArtista"]
                origin = row["Origem"]

        print(f"Nome: {artist}")
        print(f"Origem: {origin}")
        print(f"Gênero: {genre}")
        print(f"Spotify: {spotifyArtist}")

        layout = [
            [sg.Text("Artista Selecionado: " + artist)],
            [sg.Text("Origem: " + origin)],
            [sg.Text("Gênero: " + genre)],
            [sg.Text("Spotify: " + spotifyArtist)],
            [sg.Button("Voltar")],
        ]
        janela.close()
        janela = sg.Window('Projeto TCC', layout)


    if eventos == "Listar Músicas do Artista":
        layout = []

        for index, row in table.iterrows():
            if row["Artista(s)"] == artist:
                musicName = row["Nome"]
                spotifyMusic = row["SpotifyMúsica"]
                print(f"{musicName} - {spotifyMusic}")
                layout.append([sg.Text(musicName + " - " + spotifyMusic)],)
        layout.append([sg.Button("Voltar")],)

        janela.close()
        janela = sg.Window('Projeto TCC', layout)

    if eventos == "Listar Músicas do Gênero":
        layout = []

        for index, row in table.iterrows():
            if row["ID"] == id:
                genre = row["Gênero(s)"]

        for index, row in table.iterrows():
            if row["Gênero(s)"] == genre:
                musicName = row["Nome"]
                spotifyMusic = row["SpotifyMúsica"]
                print(f"{musicName} - {spotifyMusic}")
                layout.append([sg.Text(musicName + " - " + spotifyMusic)],)
        layout.append([sg.Button("Voltar")],)
        
        janela.close()
        janela = sg.Window('Projeto TCC', layout)

    if eventos == "Listar Artistas do Gênero":
        layout = []

        for index, row in table.iterrows():
            if row["ID"] == id:
                genre = row["Gênero(s)"]
                artistSelected = row["Artista(s)"]

        for index, row in table.iterrows():
            if row["Gênero(s)"] == genre:
                artist = row["Artista(s)"]
                spotifyArtist = row["SpotifyArtista"]

                if artist not in artists and artist != artistSelected:
                    artists.append(artist)
                    spotifys.append(spotifyArtist)

        for n, i in enumerate(artists):
            layout.append([sg.Text(artists[n] + " - " + spotifys[n])])
            print(f"{artists[n]} - {spotifys[n]}")

        layout.append([sg.Button("Voltar")],)
        
        janela.close()
        janela = sg.Window('Projeto TCC', layout)

        artists = []
        spotifys = []

    if eventos == "Selecionar Outro Artista":
        layout = [
            [sg.Text("ID do Artista:"), sg.Input(key="id", size=(20, 1))],
            [sg.Button("Selecionar Artista")],
        ]
        janela.close()
        janela = sg.Window('Projeto TCC', layout)

    if eventos == "Voltar":
        layout = [
            [sg.Text("Artista Selecionado: " + artist)],
            [sg.Button("Listar Informações do Artista")],
            [sg.Button("Listar Músicas do Artista")],
            [sg.Button("Listar Músicas do Gênero")],
            [sg.Button("Listar Artistas do Gênero")],
            [sg.Button("Selecionar Outro Artista")],
        ]
        janela.close()
        janela = sg.Window('Projeto TCC', layout)