import os
from paddleocr import PaddleOCR, draw_ocr
from PIL import Image

output_dir = './uncropped-img-results'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Initializing the PaddleOCR class
ocr = PaddleOCR(use_angle_cls=True, lang="en")
img_path = 'cnh.jpg'

# Actual OCR happens here
result = ocr.ocr(img_path, cls=True)

# Extracting the desired information
nome = ""
data_nascimento = ""
nacionalidade = ""
filiacao = ""
orgao_expedidor = ""

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
            nome = line[1][0]
        elif "DATADENASCIMENTO" in line[1][0]:
            data_nascimento = line[1][0]
        elif "NATURALIDADE" in line[1][0]:
            nacionalidade = line[1][0]
        elif "FILIACAO" in line[1][0]:
            filiacao = line[1][0]
        elif "ORGAO EXPEDIDOR" in line[1][0]:
            orgao_expedidor = line[1][0]

# Print the extracted information in the terminal
print("NOME:", nome)
print("DATADENASCIMENTO:", data_nascimento)
print("NATURALIDADE:", nacionalidade)
print("FILIACAO:", filiacao)
print("ORGAO EXPEDIDOR:", orgao_expedidor)
