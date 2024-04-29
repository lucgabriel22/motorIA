import cv2

# Carregando a imagem
img = cv2.imread('doc2.jpg')

# Redimensionando a imagem para 50% do tamanho original
width = int(img.shape[1] * 0.25)
height = int(img.shape[0] * 0.25)
dim = (width, height)
img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

# Coordenadas do retângulo (x, y) do canto superior esquerdo e (x+w, y+h) do canto inferior direito
x = 100
y = 100
w = 200
h = 150

# Desenhando o retângulo na imagem
cv2.rectangle(img, (100, 200), (x+w, y+h), (255, 0, 0), 2)  # (255, 0, 0) representa a cor em BGR e 2 é a espessura da linha

# Exibindo a imagem com o retângulo desenhado
cv2.imshow('Retângulo', img)
cv2.waitKey(0)
cv2.destroyAllWindows()