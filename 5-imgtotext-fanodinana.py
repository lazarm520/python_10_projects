## Tesseract
## https://github.com/UB-Mannheim/tesseract/wiki
## Download the setup file in this link and install it
## pip install tesseract

import pytesseract
import os
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe" # Path to the tesseract



def getText(txt):
  with open("all.txt", "a") as fil:
    ele1 = txt + '\n'
    # print(ele1)
    fil.write(ele1)


def convert(file):
  img = Image.open(file)
  text = pytesseract.image_to_string(img)
  getText(text)


# convert('img.jpg')

# print(os.listdir('./aa'))

for i in range(150):
  convert(f"./aa/Slide{i+1}.jpg")
  print(i+1, "done")
  # print(f"./aa/Slide{i+1}.jpg")

