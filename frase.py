from PIL import Image # Importando o módulo Pillow para abrir a imagem no script

import pytesseract # Módulo para a utilização da tecnologia OCR

print(pytesseract.image_to_string( Image.open('img/placa.jpg'))) # Extraindo o texto da imagem