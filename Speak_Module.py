# using gtts google txt to speech
from gtts import gTTS
from playsound import playsound
import os
def speak(text):
    tts = gTTS(text)
    tts.save('speech.mp3')
    playsound('speech.mp3')
    os.remove('speech.mp3')




# In built voice engine
# import pyaudio
# import pyttsx3
# engine = pyttsx3.init('sapi5')
# voices = engine.getProperty('voices')

# def speak(text):
#     engine.setProperty('voices', voices[0].id)
#     engine.say(text)
#     engine.runAndWait()
   


