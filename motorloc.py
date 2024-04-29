import cv2
from paddleocr import PaddleOCR
import os

output_dir = './uncropped-img-results'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Inicializando o PaddleOCR
ocr = PaddleOCR(use_angle_cls=True, lang="pt")

# Carregando a imagem
img_path = 'doc2.jpg'
img = cv2.imread(img_path)

# Convertendo a imagem para o formato RGB
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Redimensionando a imagem para 50% do tamanho original
width = int(img.shape[1] * 0.25)
height = int(img.shape[0] * 0.25)
dim = (width, height)
img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

# Realizando o OCR na imagem
result = ocr.ocr(img, cls=True)


# Coordenadas do retângulo (x, y) do canto superior esquerdo e (x+w, y+h) do canto inferior direito
x = 100
y = 100
w = 200
h = 150


# Desenhando o retângulo na imagem
cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)  # (255, 0, 0) representa a cor em BGR e 2 é a espessura da linha

# Exibindo a imagem com as localizações de texto demarcadas
cv2.imshow("Text Locations", img)
cv2.waitKey(0)
cv2.destroyAllWindows()