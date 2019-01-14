import cv2
import pytesseract
from PIL import Image
import string
import re
img2 = cv2.imread('img/carro4.jpg')
img = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
(T,Thresh1) = cv2.threshold(img, 40, 50, cv2.THRESH_TRUNC)
(T,Thresh3) = cv2.threshold(Thresh1, 26, 44, cv2.THRESH_BINARY)
(T,Thresh2) = cv2.threshold(Thresh3, 0 ,255,
cv2.ADAPTIVE_THRESH_GAUSSIAN_C)
(T,Thresh4) = cv2.threshold(Thresh2, 30, 255, cv2.CALIB_CB_ADAPTIVE_THRESH)
pronta = cv2.resize(Thresh4, (300, 200))
pronta1 = cv2.GaussianBlur(pronta, (9,9), 1000)
cv2.imwrite("img/placa.jpg", pronta1)
caracs = pytesseract.image_to_string(Image.open("img/placa.jpg"), lang="por")
letras = caracs[:3]
num = caracs[4:8]
num = num.replace('O', "0")
num = num.replace('I', "1")
letras = letras.replace('0', "O")
letras = letras.replace('1', "I")
num = num.replace('G', "6")
letras = letras.replace('6', "G")
num = num.replace('B', "3")
letras = letras.replace('3', "B")
num = num.replace('T', "1")
letras = letras.replace('1', "T")
print("A placa é (sem modificações): " + caracs)
print("A placa é (com modificações): " + letras + '-' + num)