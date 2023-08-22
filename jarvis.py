import speech_recognition as sr
import pyttsx3
import pywhatkit
import urllib.request
import json
import datetime
import wikipedia

name = 'cortana'  #nombre
key = 'AIzaSyB0xoE_CLEGZ9Iqi7hj5afRJNt7-TwIlEc'
listener = sr.Recognizer() #objeto de reconocimiento de voz Escucha la entrada del micrófono y la devuelve como un objeto
engine = pyttsx3.init() #objeto de motor de voz

voice = engine.getProperty('voices') #obtener las voces de la computadora
engine.setProperty('voice', voice[0].id) #asignar la voz en español mexicano

def talk(text): #función para hablar
    engine.say(text) #imprime el texto
    engine.runAndWait() #ejecuta

def listen():
    try:
        with sr.Microphone() as source: #objeto de microfono Escucha la entrada del micrófono.
            print("Escuchando...") #mensaje
            voice = listener.listen(source) 
            rec = listener.recognize_google(voice)  # Obtenga la transcripción de la entrada del micrófono.
            rec = rec.lower()
            if name in rec:
                rec = rec.replace(name, '')
                print(rec) #dice lo obtenido en el recognize_google
    except:
        pass
    return rec

def run():
    rec = listen()
    if 'reproduce' in rec:
      music = rec.replace('reproduce', '')
      talk('reproduciendo '+music)
      pywhatkit.playonyt(music)
      
    elif 'cuantos' in rec:
        print(rec)
        name_subs = rec.replace('cuantos seguidores tiene', '').strip()
        data = urllib.request.urlopen('https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername='+name_subs+'&key='+key).read()
        subs = json.loads(data)['items'][0]['statistics']['subscriberCount']
        talk(name_subs + ' tiene ' + str(subs) + ' suscriptores!')
        print(name_subs + ' tiene ' + str(subs) + ' suscriptores!')
        
    elif "hora" in rec:
        hora = datetime.datetime.now().strftime('%H:%M:%S')
        talk('La hora es ' + hora)
    elif "busca" in rec:
        order = rec.replace('busca', '')
        info = wikipedia.summary(order,1)
        talk(info)
run()