## Tesseract
## https://github.com/UB-Mannheim/tesseract/wiki
## Download the setup file in this link and install it
## pip install tesseract

import pytesseract
import os
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe" # Path to the tesseract

def convert():
  img = Image.open('img.jpg')
  text = pytesseract.image_to_string(img)
  print(text)

convert()
