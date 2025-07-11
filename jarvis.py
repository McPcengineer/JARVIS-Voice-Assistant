import pyttsx3
import requests
import speech_recognition as sr
import datetime
from bs4 import BeautifulSoup


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def greetMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Buenos días, madam!")

    elif hour>=12 and hour<18:
        speak("Buenas tardes, madam!")

    else:
        speak("Buenas noches, madam!")

    speak("Por favor dime, cómo te puedo ayudar?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Escuchando...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)

    try:
        print("Entendiendo...")
        query = r.recognize_google(audio, language='en-es')
        print(f"El usuario dijo: {query}\n")

    except Exception as e:
        print("Dilo otra vez por favor...")
        return "None"
    return query

if __name__== "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            greetMe()

            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("Ok madam, puedes llamarme si me necesitas")
                    break

                elif "hello" in query:
                    speak("Hola madam, cómo está?")
                elif "i am fine" in query:
                    speak("Eso me alegra mucho madam")
                elif "how are you" in query:
                    speak("Bien, pero no mejor que usted madam")
                elif "thank you" in query:
                    speak("De nada, madam")

                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)



                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)
                elif "temperature" in query:
                    search = "temperature in San jose iturbide guanajuato"
                    url = f"https://www.google.com.mx/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div",class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")
                elif "weather" in query:
                    search = "temperature in San jose iturbide guanajuato"
                    url = f"https://www.google.com.mx/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div",class_ = "BNeaWE").text
                    speak(f"current{search} is {temp}")

                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"Señorita, la hora es {strTime}")
                elif "finally sleep" in query:
                    speak("Yendome a dormir, madam")
                    exit()
    