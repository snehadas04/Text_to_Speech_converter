from gtts import gTTS
text = "Hello, Good morning everyone"
language = "en"
obj = gTTS(text=text, lang=language, slow=False)
obj.save("sample.mp3")