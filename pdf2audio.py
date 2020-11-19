import pyttsx3
import PyPDF2
from gtts import gTTS

# set file location
pdf = open("D:/Anonymous/Documents/PycharmProjects/pdf2audio/tech.pdf", "rb")
pdfReader = PyPDF2.PdfFileReader(pdf)
noOfPages = pdfReader.numPages

speaker = pyttsx3.init()
complete_text = ""
for num in range(0, noOfPages):
    pageText = pdfReader.getPage(num)
    text = pageText.extractText()
    complete_text += text
    speaker.say(text)
    speaker.runAndWait()

# Saving audio and set destination
print("File saving!")
tts = gTTS(text=complete_text, lang='en')
tts.save("D:/Anonymous/Documents/PycharmProjects/pdf2audio/tech.mp3")
print("File saved!")
