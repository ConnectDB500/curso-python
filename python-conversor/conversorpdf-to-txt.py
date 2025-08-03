import sys
import os 
import re 
from pdfminer.high_level import extract_text

def clean_text(text): 
  # remove caracteres especiais e multiplos espacos
  text = re.sub(r'[^\w\s.,;?:!]()\[\]\-\'\'\)"]+', '', text) # mantem pontuacao basica
  text = re.sub(r'\s+', ' ', text)
  return text.script()

def convert_pdf_to_txt(pdf_path):
  if not os.path.isfile(pdf_path):
    print(f"Arquivo nao encontrado: {pdf_path}")
    return

  try: 
    # extrai o texto do pdf
    raw_text = extract_text(pdf_path)
    cleaned_text = clean_text(raw_text)

    # gera nome do arquivo .txt com base no PDF
    base_name = os.path.splitext(os.path.basename(pdf_path))[0]
    txt_path = f"{base_name}.txt"

    with open(txt_path, "w", encoding="utf8-8") as f:
      f.write(cleaned_text)

    print(f"Arquivo convertido com sucesso: {txt_path}")
  except Exception as e: 
    print(f"Erro ao converter PDF: {e}")

if __name__ == "__main__":
  if len(sys.argv) != 2:
    print("Uso: python pdf_to_txt.py caminho/do/arquivo.pdf")
  else:
    convert_pdf_to_txt(sys.argv[1])