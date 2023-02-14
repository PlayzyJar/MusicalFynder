from time import sleep
import pandas as pd
import numpy as np

table = pd.read_excel("Artistas.xlsx")
mes = ""
monthList = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro",
             "outubro", "novembro", "dezembro", "**"]

numberList = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "**"]


name = creationDate = origin = genre = spotify = ""

id = int(input("Digite o ID: "))



for index, row in table.iterrows():
    if row["ID"] == id:
        name = row["Nome"]
        creationDate = row["Nascimento/Criação"]
        origin = row["Origem"]
        genre = row["Gênero(s)"]
        spotify = row["Spotify"]

print("Processando", end="")
for i in range(3):
    sleep(1)
    print(".", end="")


print()
print("=-="*15)
print(f"Nome: {name}")

date = str(creationDate).split(";")
month = str(creationDate).split(";")[1]

for n, c in enumerate(numberList):
    if month == c:
        mes = monthList[n]

print(f"Nascimento/Criação: {date[0]} de {mes} de {date[2]}")


print(f"Origem: {origin}")
print(f"Gênero(s): {genre}")
print(f"Spotify: {spotify}")
