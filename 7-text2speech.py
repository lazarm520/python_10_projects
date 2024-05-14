## pip install pyttsx3
## pip install pywin32

import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices')       #getting details of current voice
# for voice in voices:
#   print(voice.name)

# Change here the Voice language that you choose, here 2 is the 3rd item index (French)
# idx = 0 # English Male
# idx = 1 # English Female
idx = 2 # French
engine.setProperty("voice", voices[idx].id)


""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
# print (rate)                        # printing current voice rate
engine.setProperty('rate', 190)     # setting up new voice rate

with open('7-textToSpeech.txt', 'r') as doc:
  text = doc.read()

# data = input("Enter text which you want to convert to speech: \n")
data = text

engine.say(data)

"""Saving Voice to a file"""
# On linux make sure that 'espeak' and 'ffmpeg' are installed
engine.save_to_file(data, "voice.mp3")
engine.runAndWait()
