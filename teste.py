import cv2
import pytesseract
from PIL import Image
import string
import re

#Ler a  imagem
img = cv2.imread('img/carro.jpg')
cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


b, binario = cv2.threshold(cinza, 90, 250, cv2.THRESH_BINARY)
desfoque = cv2.GaussianBlur(binario, (5, 5), 0)
contornos, hier = cv2.findContours(desfoque, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

for c in contornos:
    perimetro = cv2.arcLength(c, True) #Cria um contorno fechado do proprio contorno
    if perimetro > 300: # diminui o espaço do contorno
        aprox = cv2.approxPolyDP(c, 0.02 * perimetro, True) #Cria um contorno da forma mais proxima dela
        if len(aprox) == 4: #Verifica se tamanho do contorno é igual a 4(Quadrado)
            (x, y, alt, lar) = cv2.boundingRect(c) #Formula para aproxima a imagem em algo proximo de um retangulo
            cv2.rectangle(binario, (x, y), (x+alt, y+lar), (255,255,255), 2)
            placa = binario[y:y + lar, x:x + alt] #delimita os espaço de onde começar e até aonde vai
            cv2.imshow('placa', binario)
            cv2.imwrite('img/placa/placa2.jpg', placa)    

#cv2.imshow("Imagem Calibrada", placa)
print("A placa é:", pytesseract.image_to_string( Image.open('img/placa/placa2.jpg')))

cv2.waitKey(0)
cv2.destroyAllWindows()

