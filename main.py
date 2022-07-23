import PyPDF2
import pyttsx3
import webbrowser as wb
import speech_recognition as sr
from translate import Translator
from gtts import gTTS
from playsound import playsound
import os
wb.register('chrome', None)

r = sr.Recognizer()
translator= Translator(to_lang="Hindi")

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
book = open('The Alchemist.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
info = PyPDF2.PdfFileReader('The Alchemist.pdf')
print(info)
print(pages)

os.startfile('The Alchemist.pdf')


speaker = pyttsx3.init()
for num in range(0, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()

    translation = translator.translate('The Alchemist.pdf')
    print(translation)

    voice = gTTS(translation, lang="hi")
    voice.save("voice.mp3")
    playsound("voice.mp3")

