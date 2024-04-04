import cv2
import numpy as np

def nothing(x):
    pass

def inRange_image(image, lower_color, upper_color):
 
    # Converte as cores para o formato HSV
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define a faixa de cores a ser detectada
    lower_bound = np.array(lower_color, dtype=np.uint8)
    upper_bound = np.array(upper_color, dtype=np.uint8)

    # Aplica a função inRange para obter a máscara
    mask = cv2.inRange(hsv_image, lower_bound, upper_bound)

    # Aplica a máscara na imagem original
    masked_image = cv2.bitwise_and(image, image, mask=mask)

    return masked_image

# Cria uma janela para a imagem
cv2.namedWindow('Imagem com inRange')

image = cv2.imread("C:/Users/Leonardo Borges/Desktop/CG/Atividade4/bocha.jpg")

# Define a faixa de cores inicial (no formato HSV)
lower_color = np.array([0, 0, 0], dtype=np.uint8)  # Valor inicial para Hue, Saturation e Value
upper_color = np.array([255, 255, 255], dtype=np.uint8)  # Valor inicial para Hue, Saturation e Value

# Cria trackbars para cada componente de cor (Hue, Saturation e Value)
cv2.createTrackbar('Hue Min', 'Imagem com inRange', 0, 179, nothing)
cv2.createTrackbar('Hue Max', 'Imagem com inRange', 179, 179, nothing)
cv2.createTrackbar('Saturation Min', 'Imagem com inRange', 0, 255, nothing)
cv2.createTrackbar('Saturation Max', 'Imagem com inRange', 255, 255, nothing)
cv2.createTrackbar('Value Min', 'Imagem com inRange', 0, 255, nothing)
cv2.createTrackbar('Value Max', 'Imagem com inRange', 255, 255, nothing)

while True:
    # Obtém a posição atual das trackbars
    lower_color[0] = cv2.getTrackbarPos('Hue Min', 'Imagem com inRange')
    upper_color[0] = cv2.getTrackbarPos('Hue Max', 'Imagem com inRange')
    lower_color[1] = cv2.getTrackbarPos('Saturation Min', 'Imagem com inRange')
    upper_color[1] = cv2.getTrackbarPos('Saturation Max', 'Imagem com inRange')
    lower_color[2] = cv2.getTrackbarPos('Value Min', 'Imagem com inRange')
    upper_color[2] = cv2.getTrackbarPos('Value Max', 'Imagem com inRange')

    # Aplica a função inRange na imagem
    masked_image = inRange_image(image, lower_color, upper_color)

    # Mostra a imagem resultante
    cv2.imshow("Imagem com inRange", masked_image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
