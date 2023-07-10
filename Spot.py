# shows artist info for a URN or URL

from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import sys
import pprint
import webbrowser
import pyautogui
from time import sleep
from tkinter import *

root = Tk()
root.title('Selector de canciones')
root.geometry('350x180')

song1 = StringVar()
artist = StringVar()

def reproducir():
    flag = 0
    client_id = '841427302fd04766a50fa501c3123438'
    client_secret = 'fa0e7070c51a4ee7b73cd953740c56c3'
    artist_op = artist.get()
    song = song1.get()
    song = song.upper()

    if len(artist_op) > 0:
        sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id, client_secret))
        result = sp.search(artist_op)
        for i in range (0,len(result['tracks']['items'])):
            name_song = result['tracks']['items'][i]['name'].upper()
            if song == name_song:
                flag = 1
                print ("Respreduciendo " + name_song + " ...")
                webbrowser.open(result['tracks']['items'][i]['uri'])
        
    if flag == 0:
        song = song.replace(" ", "%20")
        webbrowser.open(f'spotify:search:{song}')
        sleep(5)
        for i in range (2) :
            pyautogui.press("tab")
        pyautogui.press('enter') 
        sleep(2)
        pyautogui.press('enter')        
      
label1 = Label(root, text='Ingresa una canción o lista de reproduccion: ')
label1.place(x=10, y=20)
entry1 = Entry (root, textvariable= song1)
entry1.place (x=170, y = 20)

label2 = Label(root, text='Nombre de artista (opcional): ')
label2.place(x=10, y=60)
entry2 = Entry (root, textvariable= artist)
entry2.place (x=170, y = 60)

button = Button(root, text='Aceptar', command= reproducir)
button.place(x = 150, y = 150)

root.mainloop()         






#-------------- Spotify--------------

  
   

      