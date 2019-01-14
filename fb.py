import cv2
image = cv2.imread('img/carro.jpg')
#Cria um retangulo verde da linha 150 a 300 nas colunas 250 a 350
image[160:250, 200:550] = (0, 255, 0)


cv2.imshow("Imagem alterada", image)
cv2.imwrite("alterada.jpg", image)
cv2.waitKey(0)
