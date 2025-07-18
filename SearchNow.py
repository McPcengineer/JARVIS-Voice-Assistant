from unittest import result
import webbrowser
import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import webbrowser


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

query = takeCommand().lower()  

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def searchGoogle(query):
    if "google" in query:
        import wikipedia as googleScrap
        query = query.replace("jarvis","")
        query = query.replace("google search","")
        query = query.replace("google","")
        speak("Esto es lo que encontré en google")

    try:
        pywhatkit.search(query)
        result = googleScrap.summary(query,1)
        speak(result)

    except:
        speak("No está disponible lo que pides")

def searchYoutube(query):
    if "youtube" in query:
        speak("Esto es lo que encontré para tu busqueda!")
        query = query.replace("youtube search","")
        query = query.replace("youtube","")
        query = query.replace("jarvis","")
        web = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("Listo, señorita")

def searchWikipedia(query):
    if "wikipedia" in query:
        speak("Buscando de wikipedia...")
        query = query.replace("wikipedia","")
        query = query.replace("search wikipedia","")
        query = query.replace("jarvis","")
        results = wikipedia.summary(f'{query}', sentences=2)
        speak("De acuerdo a wikipedia...")
        print(results)
        speak(results)
        
        

    
        

        

      
