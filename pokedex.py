import requests
from tkinter import *

api_url = "https://pokeapi.co/api/v2/pokemon?limit=151&offset=0"
data = requests.get(api_url).json()

window=Tk()

for i in range(151):
    colonne = (i-i%25)/25
    lbl=Label(window, text=(str(i+1) + " - " + data["results"][i]["name"]), font=("TimesNewRoman", 16))
    lbl.place(x=(colonne*200)+50, y=32*(i%25))


window.title('Mon Pokedex')
window.geometry("1600x800+10+20")
window.mainloop()