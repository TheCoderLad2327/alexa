import pyautogui
import keyboard
import winapps
import os
import deep_translator
import speech_recognition as sr
import webbrowser
import wikipedia
import time
import smtplib
import win10toast
import pyttsx3
from datetime import datetime
import threading
from deep_translator import GoogleTranslator
speaker = pyttsx3.init()
notification = win10toast.ToastNotifier
recog = sr.Recognizer()
paused = False

def time_now():
    time = datetime.now()
    time = str(time.hour) + ':' + str(time.minute)
    speaker.say('The time now is' + time)
    speaker.runAndWait()
    print(time)

def take_command():
    with sr.Microphone() as source:
        recog.adjust_for_ambient_noise(source)
        print('Listening...')
        audio = recog.listen(source)
        print('recognising...')
        ga = recog.recognize_google(audio, language='en-in')
        print(f'You said: {ga}')
    return ga

def send_email(mailto, subject, body):
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login('dummy@gmail.com', 'dummy')
        msg = f'Subject: {subject} \n\n\n {body}'
        smtp.sendmail('dummy@gmail.com',mailto,msg)

def reminder():
    speaker.say('Please type name for the reminder: ')
    speaker.runAndWait()
    name_reminder = str(input('name: '))
    speaker.say('Please type waiting time for the remainder: ')
    speaker.runAndWait()
    t = int(input('time: '))
    time.sleep(h)
    notification.show_toast(name_reminder, f"It is time for {name_reminder}")

def adam():
    global paused
    while True:
        google_audio = take_command().lower()
        ga = google_audio
        if 'time' in ga and paused == False:
            time_now()
        elif 'youtube' in ga and paused == False:
            speaker.say('Opening Sir...')
            speaker.runAndWait()
            webbrowser.open_new(r'https://www.youtube.com/')
        elif 'google' in ga and paused == False:
            speaker.say('Opening Sir...')
            speaker.runAndWait()
            webbrowser.open_new(r'https://www.google.com/')
        elif 'facebook' in ga and paused == False:
            speaker.say('Opening Sir...')
            speaker.runAndWait()
            webbrowser.open_new(r'https://www.facebook.com/')
        elif 'microsoft word' in ga and paused == False:
            speaker.say('Opening Sir...')
            speaker.runAndWait()
            os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\Microsoft Office Word 2007.lnk")
            time.sleep(6)
        elif 'microsoft excel' in ga and paused == False:
            speaker.say('Opening Sir...')
            speaker.runAndWait()
            os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\Microsoft Office Excel 2007.lnk")
            time.sleep(6)
        elif 'wikipedia' in ga and paused == False:
            speaker.say('opening,sir')
            speaker.runAndWait()
            google_audio = ga.replace('according to wikipedia' , '')
            summary= wikipedia.summary(google_audio,sentences = 2)
            print(summary)
            speaker.say(summary)
            speaker.runAndWait()
        elif 'play' in ga and paused == False:
            x = ga.replace('play','')
            webbrowser.open_new('https://www.youtube.com/results?search_query=' + x)
        elif 'good morning' in ga and paused == False:
            speaker.say('good morning')
            speaker.runAndWait()
        elif 'type' in ga and paused == False:
            google_audio = ga.replace('type' , '')
            pyautogui.write(google_audio)
            time.sleep(5)
        elif 'send' in ga and paused == False:
            mailto = input('''Enter reciever's email id: ''')
            engine.say('Please say the subject.')
            engine.runAndWait()
        elif 'subject' in ga and paused == False:
            s = google_audio.replace('subject is ', '')
            engine.say('Please say the body.')
            engine.runAndWait()
        elif 'body' in ga and paused == False:
            b = google_audio.replace('body is ', '')
            send_email(mailto,s,b)
        elif 'reminder' in ga and paused == False:
            ta = threading.Thread(target = reminder, daemon = False)
            ta.start()
        elif 'translate' in ga and paused == False:
            what = str(input('what to translate: '))
            lang = str(input('language to translate to in short form: '))
            translated = GoogleTranslator(source='auto',target=lang).translate(what)
            print(translated)
        elif 'pause' in ga:
            paused = True
        elif 'continue' in ga:
            paused = False
        elif 'quit' in ga and paused == False:
            break
        elif paused == False:
            speaker.say('opening')
            speaker.runAndWait()
            webbrowser.open_new('https://www.google.com/search?q=' + google_audio)
adam()
