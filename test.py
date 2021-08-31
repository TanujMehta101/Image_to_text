# import the following libraries 
# will convert the image to text string 

import pytesseract       

# adds image processing capabilities 

from PIL import Image    

###
from gtts import gTTS
import os
  
# opening an image from the source path 

img = Image.open('text15.png')      

  
# describes image format in the output 

print(img)                           
# path where the tesseract module is installed 

pytesseract.pytesseract.tesseract_cmd ='C:\\Program Files\\Tesseract-OCR\\tesseract.exe'   
# converts the image to result and saves it into result variable 

result = pytesseract.image_to_string(img)    
# write text in a text file and save it to source path    

with open('abc.txt',mode ='w') as file:      

      

                 file.write(result) 

                 print(result)


###
#opening text file in read mode
fh = open("abc.txt", "r")
#replacing all next line to space
mytext = fh.read().replace("\n"," ")
#speech language is english
language = 'en'
output = gTTS(text=mytext, lang=language, slow=False)
#saving audio file
output.save("audio.mp3")
fh.close()
#start playing audio
os.system("start audio.mp3")
