import requests
import json
import time
import pyttsx3 

API_KEY = "Insert your API Key here"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id) # for particular voice
engine.setProperty('rate', 170) # changes the rate/speed
engine.setProperty('volume', 1.0) # sets the volume

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

name = input("Enter Your name? ")
speak(f"Hi {name}, Welcome to News feed. We have news for the following countries. Enter the country code you want to see the news for.")
print("1. Enter 'au' for Australia\n2. Enter 'ca' for Canada\n3. Enter 'in' for India\n4. Enter 'nz' for New Zeland\n5. Enter 'za' for South Africa\n6. Enter 'gb' for United Kingdom\n7. Enter 'us' for United States")
country = input("Which Country News you want to listen? ") 

speak("How many news you want to listen")
howmany = input("How many news you want to listen? ")
speak(f"Here is the top {howmany} latest news for you")
print("Playing news...")

news = requests.get(f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}") # News (API-KEY)
data = json.loads(news.content)
    
if __name__ == '__main__' and int(howmany)>0:
    for i in range(int(howmany)):
        engine.setProperty('rate', 180) # changes the rate/speed
        engine.setProperty('volume', 1.0) # sets the volume
        speak(f"News {i+1}")
        title = data['articles'][i]['title']
        speak(title)
        volume = engine.setProperty('volume', 0.9)
        rate = engine.setProperty('rate', 190) # changes the rate/speed
        description = data['articles'][i]['description']
        speak(description)
        time.sleep(1)

speak(f"Thanks {name} for listening")
print(f"Thanks {name} for listening")