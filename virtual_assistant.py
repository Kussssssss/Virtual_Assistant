import os
import pyttsx3 as pt
import datetime as dt
import speech_recognition as sr 
import webbrowser as wb 
friday = pt.init()
voice = friday.getProperty('voices') 
friday.setProperty('voice',voice[1].id)


def speak(audio):
    print('F.R.I.D.A.Y: ' + audio)
    friday.say(audio)
    friday.runAndWait()

def time():
    Time = dt.datetime.now().strftime("%I:%M%p")
   
    speak(Time)

def welcome():
    hour = dt.datetime.now().hour
    if hour >= 6 and hour <12:
        speak("Good morning Miss Nhung!")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon Miss Nhung!")
    elif hour >= 18 and hour < 24:
        speak("What a beautiful night Miss Nhung!")
    speak("How can I help you?")
def command():
    c = sr.Recognizer(
    with sr.Microphone() as source:
        c.pause_threshold = 1 
        audio = c.listen(source)
    try:
        query = c.recognize_google(audio,language='en')
        print("Kus : " + query)
    except sr.UnknownValueError: 
        print("Please repeat or typing the command ")
        query = str(input('Your order is: '))
    return query
if __name__ == "__main__":
    welcome()
    while True:
        query = command().lower()
        if "my facebook" in query:
            url=f"https://www.facebook.com"
            wb.get().open(url) 
            speak(f'Here is your facebook on facebook')
        if "google" in query:
            speak("What should I search boss?")
            search = command().lower()
            url=f"https://www.google.com/search?q={search}"
            wb.get().open(url)
            speak(f'Here is your {search} on google')
        if "youtube" in query:
            speak("What should I search boss?")
            search = command().lower()
            url=f"https://www.youtube.com/search?q={search}"
            wb.get().open(url)
            speak(f'Here is your {search} on youtube')
        if "video one" in query:
            vid1=r"C:\Users\Admin\Videos\Captures\vid.mp4"
            os.startfile(vid1)
        if "video two" in query:
            vid2=r"C:\Users\Admin\Videos\Captures\vid2.mp4"
            os.startfile(vid2)
        if "time" in query:
            time()
        if "quit" in query:
            speak("Friday is quitting sir. Goodbye boss!")
            quit()
