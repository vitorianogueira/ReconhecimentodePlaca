import cv2
import numpy as np
import pytesseract as ocr

from PIL import Image

#Ler a  imagem
img = cv2.imread('img/meucarro.jpg')
cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


_, bin = cv2.threshold(cinza, 90, 255, cv2.THRESH_BINARY)

desfoque = cv2.GaussianBlur(bin, (5, 5), 0)


#Procurar contornos da imagem de acordo com a imagem desfocada
contornos, hier = cv2.findContours(desfoque, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

#pega o retangulo da placa
for c in contornos:
    perimetro = cv2.arcLength(c, True)
    if perimetro > 300:
        aprox = cv2.approxPolyDP(c, 0.05 * perimetro, True)
        if len(aprox) == 4:
            (x, y, alt, lar) = cv2.boundingRect(c)
            cv2.rectangle(img, (x, y), (x+alt, y+lar), (0, 255, 0), 2)
            placa = img[y:y + lar, x:x + alt]
            cv2.imshow('placa', img)
            cv2.imwrite('img/20.jpg', placa)

#phrase = ocr.image_to_string(Image.open('img/placa.jpg'), lang='por')
#print(phrase)
  
            
# Aguarda até uma tecla ser pressionada para fechar
cv2.waitKey(0)
# Fechar a janela aberta e só vai acontencer quando alguma tecla foi clicada
cv2.destroyAllWindows()

