from gtts import gTTS
import os

def convertTxt(txt,lan):
    try:
        tts = gTTS(text=txt, lang=lan)
        tts.save("/tmp/TtoSpeech.mp3")
        return "Sucessfully text is converted to speech"
    except:
        return "Something went wrong"


def getSpeech():
    try:
        os.system("mpg321 /tmp/TtoSpeech.mp3")
        return "Sucess"
    except:
        return "Problem in playing the audio"



