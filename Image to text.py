import cv2
import pytesseract
import numpy as np
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
img = cv2.imread('Resources/text.png')
cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

a = pytesseract.image_to_string(img)
b = pytesseract.image_to_boxes(img)
c = b.splitlines()

def toBox(Points) :
    h , w ,_= img.shape
    for box in Points:
        d = box.split(' ')
        cv2.putText(img,d[0],(int(d[1]),h-int(d[2])+20),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),1)
        cv2.rectangle(img,(int(d[1]),h-int(d[2])),(int(d[3]),h - int(d[4])),(255,0,0),1)

def toCsv(Text) :
    c = Text.splitlines()
    with open('Resources/Text.csv', 'r+') as f:
        for line in c:
            f.write(f'\n{line}')

toCsv(a)
toBox(c)
print(a)
cv2.imshow("img",img)
cv2.waitKey(0)
