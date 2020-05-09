import speech_recognition
import re

# get audio from mic
recognizer = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    print("Say something!")
    audio = recognizer.listen(source)

# recognize speech using Google Speech Recognition
words = recognizer.recognize_google(audio)

# responses
hello = re.search("my name is (.*)", words)

if hello:
    print(f"Hello {hello[1]}!")
else:
    print(" Hello unknown!")

if "goodbye" in words:
    print("Goodbye to you too!")