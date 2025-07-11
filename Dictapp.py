import os
from time import sleep
import pyautogui
import webbrowser
import pyttsx3
import requests

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

dictapp = {"commandprompt":"cmd","paint":"paint","word":"winword","excel":"excel","chrome":"chrome","vscode":"code","powerpoint":"powerpnt"}

def openspotify(query):
    speak("Abriendo spotify")
    if "Song please" in query or "play some song" in query or "could you play some song" in query:
        speak("Señorita que cancion deberia reproducir...")
        song = query
        webbrowser.open(f'https://open.spotify.com/search/{song}')
        sleep(13)
        pyautogui.click(x=1055,y=617)
        speak("playing" + song)
    elif "play" in query or "can you play" in query or "please play" in query:
        speak("Ok! Ahi vamos")
        query = query.replace("play","")
        query = query.replace("could you play","")
        query = query.replace("please play","")
        webbrowser.open(f'https://open.spotify.com/search/{query}')
        sleep(19)
        pyautogui.click(x=1055,y=617)
        print("Disfruta!" )
        speak("Disfruta señorita")


def openappweb(query):
    speak("Acción en proceso, señorita")
    if ".com" in query or ".co.mx" in query or ".org" in query:
        query = query.replace("open","")
        query = query.replace("jarvis","")
        query = query.replace("launch","")
        query = query.replace(" ","")
        webbrowser.open(f"https://www.{query}")
    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"start{dictapp[app]}")
                


def closeappweb(query):
    speak("Cerrandolo, señorita")
    if "one tab" in query or "1 tab" in query:
        pyautogui.hotkey("ctrl","w")
        speak("Todas las ventanas cerradas")
    elif "2 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("Todas las ventanas cerradas")
    elif "3 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("Todas las ventanas cerradas")
    elif "4 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("Todas las ventanas cerradas")
    elif "5 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("Todas las ventanas cerradas")

    else:
        keys = list(dictapp.keys)
        for app in query:
            if app in query:
                os.system(f"taskkill /f /im {dictapp[app]}.exe")

