# pip install SpeechRecognition
import pyttsx3
import speech_recognition as sr

def get():
  r = sr.Recognizer()
  with sr.Microphone() as source:
    print('Sey something...! ')
    audio = r.listen(source)
    print('Done!')
  
  try:
    text = r.recognize_google_cloud(audio)
    print('You said :\n' + text)

  except Exception as e:
    print(e)

get()
