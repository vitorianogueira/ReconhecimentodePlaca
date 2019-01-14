import cv2
import pytesseract
from PIL import Image
import string
import re
img2 = cv2.imread("img/placa.jpg")
img = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
(T,Thresh1) = cv2.threshold(img, 44, 54, cv2.THRESH_TRUNC)
(T,Thresh3) = cv2.threshold(Thresh1, 43, 44, cv2.THRESH_BINARY)
(T,Thresh2) = cv2.threshold(Thresh3, 0 ,255,
 cv2.ADAPTIVE_THRESH_GAUSSIAN_C)
(T,Thresh4) = cv2.threshold(Thresh2, 30, 255, cv2.CALIB_CB_ADAPTIVE_THRESH)
cv2.imshow("Imagem 01", Thresh4)
cv2.imwrite('img/vitoria.jpg', Thresh4)
print(pytesseract.image_to_string( Image.open('img/vitoria.jpg'))) # Extraindo o texto da imagem
cv2.waitKey(0)