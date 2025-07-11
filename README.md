# JARVIS Voice Assistant

JARVIS is a voice-controlled desktop automation tool that executes natural language commands such as opening applications, performing web searches, playing music, checking the weather, and more. It supports multilingual input and achieves around 90% accuracy in speech recognition.

## Features

- Voice recognition in English and Spanish
- Wake word activation ("wake up") and sleep command ("go to sleep")
- Personalized greetings based on time of day
- Web search through Google, YouTube, and Wikipedia
- Basic control for Spotify
- Weather and location reporting via web scraping
- Time announcements
- Customizable commands to open or close applications

## Technologies Used

- Python 3.8 or higher
- `pyttsx3` for text-to-speech synthesis
- `SpeechRecognition` for voice input
- `BeautifulSoup` for web scraping
- `requests`, `datetime`, `geocoder`
