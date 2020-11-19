from gtts import gTTS

# set file location
file = "D:/Anonymous/Documents/PycharmProjects/pdf2audio/tech.txt"
f = open(file, 'r')
text = f.read()
f.close()

# saving audio and set destination
print("File saving!")
tts = gTTS(text=text, lang='en')
tts.save("D:/Anonymous/Documents/PycharmProjects/pdf2audio/tech.mp3")
print("File saved!")