from gtts import gTTS
import os

abc = open("sample.txt")
txt = abc.read()

language = "en"
obj = gTTS(text=txt, lang=language, slow=False)
obj.save("sample.mp3")
os.system("sample.mp3")