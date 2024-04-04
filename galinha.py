import cv2
import numpy as np

# Carregar a imagem
image = cv2.imread("D:/Desktop/CG/Atividade4/Galinha.png")

# Converter a imagem de BGR para HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Definir a faixa de cor vermelha na escala HSV
lower_red = np.array([0, 100, 100])
upper_red = np.array([10, 255, 255])

# Criar uma máscara para identificar áreas na imagem que correspondem à faixa de cor vermelha
mask = cv2.inRange(hsv, lower_red, upper_red)

# Encontrar contornos na imagem com a máscara aplicada
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Iterar sobre os contornos e encontrar o maior
max_contour = max(contours, key=cv2.contourArea)

# Obter as coordenadas do retângulo delimitador ao redor do maior contorno
x, y, w, h = cv2.boundingRect(max_contour)

# Recortar a região da imagem encontrada
franginho = image[y:y+h, x:x+w]

# Salvar a imagem recortada como 'franginho.jpg'
cv2.imwrite('D:/Desktop/CG/Atividade4/franginho.jpg', franginho)

# Mostrar a imagem recortada
cv2.imshow('Franginho', franginho)
cv2.waitKey(0)
cv2.destroyAllWindows()
