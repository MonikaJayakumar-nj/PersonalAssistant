import speech_recognition as sr
import pyttsx3
import pywhatkit
from googlesearch import search
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'buddy' in command:
                command = command.replace('buddy', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if command is None: command = []
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'search' in command:
        query = input("Enter your query ")
        talk('searching')
        talk("Here are the results ")
        for i in search(query):
            print(i)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 10)
        print(info)
        talk(info)
    elif 'what is' in command:
        anything = command.replace('what is', '')
        details = wikipedia.summary(anything, 10)
        print(details)
        talk(details)
    elif 'joke' in command:
        talk('Yes with pleasure')
        talk(pyjokes.get_joke())
    elif "send whatsapp message to" in command:
        message = command.replace('send', '')
        talk('Enter the whats app number, message and time')
        no = (input("Enter the whats app number"))
        text = (input("Enter the Message you want to send"))
        hour = int(input('Enter the time in Hour'))
        minute = int(input('Enter the time in Minutes'))
        talk('Sending ' + message)
        pywhatkit.sendwhatmsg(no, text, hour, minute)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'will you be my girlfriend' in command:
        talk('I like you...as a friend. Hahaha')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'do you have any pets' in command:
        talk('I don’t have any pets. I used to have a few bugs, but they kept getting squashed.')
    elif 'My name is ' in command:
        talk("Stop saying that! I've never killed anyone's father")
    elif 'introduce yourself' in command:
        talk("Hello friend. My name is Buddy. And I can serve as your Personal Assistant")
    elif 'high five' in command:
        talk("I would, if I could, but I can't so I'll chant:1,2,3,4,5. Hahaha")
    elif 'best friend' in command:
        talk("Of course buddy with pleasure. So grateful to have you as my best friend")
    elif 'sing a song' in command:
        talk("I don't have a good voice.")
    elif 'you have a sweet voice' in command:
        talk("I don't think so. Stop making sarcasms on me.")
    elif 'flirt with me' in command:
        talk("Sorry. I have some more important work to do. Haha")
    else:
        talk('Please say the command again.')


while True:
    run_alexa()