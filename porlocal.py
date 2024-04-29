from paddleocr import PaddleOCR
from PIL import Image
import re
import json

# Initialize the PaddleOCR
try:
    ocr = PaddleOCR(use_angle_cls=True, lang="pt")
except Exception as e:
    print(f"Error initializing PaddleOCR: {e}")
    exit(1)

# Load the image of the identity
try:
    img = Image.open("doc2.jpg")
except FileNotFoundError:
    print("Image file 'doc2.jpg' not found.")
    exit(1)

# Perform text detection on the image
try:
    result = ocr.ocr(img)
except Exception as e:
    print(f"Error performing text detection: {e}")
    exit(1)

# Extract the information of NAME and CPF
nome = ""
cpf = ""

for line in result:
    text = line[1][0]
    
    if "NOME" in text:
        nome_match = re.search(r'NOME: (.+)', text)
        if nome_match:
            nome = nome_match.group(1).strip()
    
    elif "CPF" in text:
        cpf_match = re.search(r'CPF: (.+)', text)
        if cpf_match:
            cpf = cpf_match.group(1).strip()

# Convert the extracted information to JSON and print it
data = {'NOME': nome, 'CPF': cpf}
print(json.dumps(data, indent=4))