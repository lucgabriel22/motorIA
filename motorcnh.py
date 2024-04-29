import os
from paddleocr import PaddleOCR, draw_ocr
from PIL import Image

output_dir = 'imagens_ocr_cnh'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Initializing the PaddleOCR class
ocr = PaddleOCR(use_angle_cls=True, lang="en")
img_path = 'cnh.jpg'

# Actual OCR happens here
result = ocr.ocr(img_path, cls=True)

# Extracting the desired information
nome_e_sobrenome = ""
data_local_e_uf_de_nascimento = ""
data_emissao = ""
validade = ""
cpf = ""
nacionalidade = ""
# filiação = ""
# filiação = ""


for idx, res in enumerate(result):
    image = Image.open(img_path).convert('RGB')
    boxes = [line[0] for line in res]
    txts = [line[1][0] for line in res]
    scores = [line[1][1] for line in res]
    
    output_filename = os.path.join(output_dir, f'result_IDexample{idx+1}.jpg')
    
    im_show = draw_ocr(image, boxes, txts, scores, font_path='./font/Roboto-Medium.ttf')
    im_show = Image.fromarray(im_show)
    im_show.save(output_filename)
    
    # Check if the extracted information matches the desired fields
    for line in res:
        if "NOME" in line[1][0]:
            nome_e_sobrenome = line[1][0]
        elif "DATA_LOCAL_UF_NASCIMENTO" in line[1][0]:
            data_local_e_uf_de_nascimento = line[1][0]
        elif "DATA_EMISSAO" in line[1][0]:
            data_emissao = line[1][0]
        elif "VALIDADE" in line[1][0]:
            validade = line[1][0]
        elif "cpf" in line[1][0]:
            cpf = line[1][0]
        elif "NACIONALIDADE" in line[1][0]:
            nacionalidade = line[1][0]
        # elif "filiação" in line[1][0]:
           # filiação = line[1][0]
        #elif "filiação2" in line[1][0]:
            #filiação2 = line[1][0]

# Print the extracted information in the terminal
print("NOME:", nome_e_sobrenome)
print("DATADENASCIMENTO:", data_local_e_uf_de_nascimento)
print("DATA_EMISSÃO_CNH:", data_emissao)
print("VALIDADE_CNH:", validade)
print("CPF:", cpf)
print("NACIONALIDADE:", nacionalidade)
# print("FILIACAO:", filiação)
# print("FILIACAO2:", filiação2)