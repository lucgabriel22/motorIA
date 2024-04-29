import os
import cv2
from paddleocr import PaddleOCR

# Inicializando o PaddleOCR
ocr = PaddleOCR(use_angle_cls=True, lang="pt")

# Carregando a imagem da CNH
img_path = 'cnh.jpg'
img = cv2.imread(img_path)

# Verificando se a imagem foi carregada corretamente
if img is None:
    print("Erro ao carregar a imagem da CNH")
    exit()

# Convertendo a imagem para o formato RGB
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Realizando o OCR na imagem da CNH
result = ocr.ocr(img, cls=True)

# Inicializando as variáveis para armazenar as informações extraídas
nome = ""
data_emissao = ""
validade = ""
cpf = ""
filiacao = ""

# Processando o resultado para extrair as informações desejadas
for idx, res in enumerate(result):
    for line in res:
        text = line[1][0]
        if ":" in text:
            if "NOME" in text:
                nome = text.split(":")[1].strip()
            elif "DATA DE EMISSÃO" in text:
                data_emissao = text.split(":")[1].strip()
            elif "VALIDADE" in text:
                validade = text.split(":")[1].strip()
            elif "CPF" in text:
                cpf = text.split(":")[1].strip()
            elif "FILIAÇÃO" in text:
                filiacao = text.split(":")[1].strip()
        else:
            print(f"A linha {idx} não contém dois pontos")

# Exibindo as informações extraídas
print("NOME:", nome)
print("DATA DE EMISSÃO:", data_emissao)
print("VALIDADE:", validade)
print("CPF:", cpf)
print("FILIAÇÃO:", filiacao)