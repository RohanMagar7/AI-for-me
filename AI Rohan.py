import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser
import os


def speak(audio):
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()


def time():
    time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("current time is ")
    speak(time)


def Date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("current date is ")
    speak(date)
    speak(month)
    speak(year)


def wishme():
    speak(" System ready sir")

    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good morning sir")
    elif hour >= 12 and hour < 18:
        speak("Good afternon sir")
    elif hour >= 18 and hour < 24:
        speak("good evening sir")
    else:
        speak("good night sir")

    speak(" Your AI at your service ")


def TakeCommend():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listeing ..")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print(" Recongnizing ")
        query = r.recognize_google(audio, language='en-in')
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again please ...")
        return "none"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('rmtechyt8@gmail.com', 'Punam83@')
    server.sendmail('rmtechyt8@gmail.com', to, content)
    server.close()


if __name__ == "__main__":

    wishme()
    while True:
        query = TakeCommend().lower()
        if 'time' in query:
            time()

        elif 'date' in query:
            Date()

        elif 'state' in query:
            speak("maharastra")

        elif 'Hello' in query:
            speak("Hello sir" )

        elif 'who are you' in query:
            speak("i am jarves")

        elif 'stupid' in query:
            speak("yes, mansi is stupid? ")

        elif 'how are you' in query:
            speak("i am fine.. and you ? ")

        elif 'wikipedia' in query:
            speak('Search Wikipedia..')
            query = query.replace("wikipedia", " ")
            result = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia ")
            speak(result)
            print(result)

        elif 'send email ' in query:
            try:
                speak(" what should I say ? ")
                content = 'rmtechyt@gmail.com'
                to = 'rmtechyt8@gmail.com'
                sendEmail(to, content)
                speak("Email has been sent! ")
            except Exception as e:
                print(e)
                speak("uable to send the email")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'remember that' in query:
            speak("what should i remember")
            data = TakeCommend()
            remember = open('data.txt', 'w')
            remember.write(data)
            remember.close()
            speak("you said me to remember that "+data)

        elif 'do you know anything' in query:
            remember = open('data.txt', 'r')
            speak("you said me to remember that "+remember.read())

        elif 'play music' in query:
            music_dir = 'D:\\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'shudown' in query:
            os.system("shutdown /s /t 1")

        elif 'restart' in query:
            os.system("restart /r /t 1")

        elif 'logout' in query:
            os.system("logout  -l")

        elif 'shut down' in query:
            quit()
