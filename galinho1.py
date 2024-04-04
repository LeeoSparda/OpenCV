import cv2

# Carregar a imagem
image_path = "D:/Desktop/CG/Atividade4/franginho.jpg"
image = cv2.imread(image_path)

# Converter a imagem para escala de cinza
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Aplicar a suavização para reduzir o ruído
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

# Limiarizar a imagem
_, thresholded_image = cv2.threshold(blurred_image, 100, 255, cv2.THRESH_BINARY)

# Encontrar contornos na imagem limiarizada
contours, _ = cv2.findContours(thresholded_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Desenhar os contornos na imagem original
contour_image = image.copy()
cv2.drawContours(contour_image, contours, -1, (0, 255, 0), 2)

# Exibir a imagem original com os contornos encontrados
cv2.imshow('Contours', contour_image)

# Contar o número de galinhas
num_galinhas = len(contours)
print("Número de galinhas:", num_galinhas)

cv2.waitKey(0)
cv2.destroyAllWindows()
