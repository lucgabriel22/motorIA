import cv2
from paddleocr import PaddleOCR
import json

# Carregar o modelo do PaddleOCR
ocr = PaddleOCR()

# Carregar a imagem
image = cv2.imread('doc1.jpg')

# Converter a imagem para o formato RGB
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Extrair texto
result = ocr.ocr(image)

# Convertendo o resultado em um JSON
data = {'texto': []}
for line in result:
    data['texto'].append(line[1][0])

# Exibir o JSON no terminal
print(json.dumps(data, indent=4))