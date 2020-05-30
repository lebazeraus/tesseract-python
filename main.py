# !#/usr/bin/python3
import pytesseract as tesseract
import time
import os
#
root = "D:\\GitHub\\tesseract-python\\imgs"
list = os.listdir(root)

for _ in list:
  if _.split('.')[-1] in ('jpg'):
    text = tesseract.image_to_string(root + '\\' + _, config='--psm 10 --oem 3 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ-1234567890')
    print(text, ' ... ', _)
