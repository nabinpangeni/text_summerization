from gtts import gTTS
import os
mytext=open("Readme_test.txt","r").read().replace("\n"," ")
language='en'
myobj=gTTS(text=str(mytext),lang=language,slow=False)
myobj.save("readme.mp3")
os.system("mpg321 readme.mp3")


