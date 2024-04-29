import cv2
import tempfile
from paddleocr import PaddleOCR

# Inicializando o PaddleOCR
ocr = PaddleOCR(use_angle_cls=True, lang="pt")

# Carregando a imagem
img_path = 'doc2.jpg'
img = cv2.imread(img_path)

# Realizando o OCR na imagem
result = ocr.ocr(img, cls=True)

# Processando o resultado para obter a localização de texto
text_locations = []
for idx, res in enumerate(result):
    for line in res:
        text = line[1][0]
        x, y, w, h = line[0]
        text_locations.append((text, x, y, w, h))

# Identificando as localizações de texto correspondentes às variáveis que você deseja extrair
variables = ['NOME', 'FILIAÇÃO', 'NATURALIDADE', 'CPF', 'DATA DE NASCIMENTO']
variable_locations = {}
for text, x, y, w, h in text_locations:
    text = text.strip().upper()
    if text in variables:
        variable_locations[text] = (x, y, w, h)

# Extraindo as informações correspondentes às localizações de texto
nome = ''
filiacao = ''
naturalidade = ''
cpf = ''
data_nascimento = ''
for variable, location in variable_locations.items():
    x, y, w, h = location
    y_start, y_end = int(y), int(y + h)
    x_start, x_end = int(x), int(x + w)
    info = img[y_start:y_end, x_start:x_end]

    # Salvando o recorte da imagem em um arquivo temporário
    temp_img_path = tempfile.NamedTemporaryFile(suffix='.jpg').name
    cv2.imwrite(temp_img_path, info)
    
    # Realizando o OCR no recorte da imagem
    ocr_result = ocr.ocr(temp_img_path)
    
    # Atualizando as variáveis com as informações extraídas
    extracted_text = ocr_result[0][0][1] if ocr_result else ''
    if variable == 'NOME':
        nome = extracted_text
    elif variable == 'FILIAÇÃO':
        filiacao = extracted_text
    elif variable == 'NATURALIDADE':
        naturalidade = extracted_text
    elif variable == 'CPF':
        cpf = extracted_text
    elif variable == 'DATA DE NASCIMENTO':
        data_nascimento = extracted_text

# Exibindo as informações extraídas
print("Nome:", nome)
print("Filiação:", filiacao)
print("Naturalidade:", naturalidade)
print("CPF:", cpf)
print("Data de Nascimento:", data_nascimento)