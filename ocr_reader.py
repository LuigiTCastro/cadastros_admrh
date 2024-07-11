import pytesseract
import os
from dotenv import load_dotenv
from pdf2image import convert_from_path
from PIL import Image, ImageEnhance, ImageFilter


def pdf_img_to_txt(pdf_path, output_img_dir):
    load_dotenv()
    TESSERACT = os.getenv('TESSERACT') # captura a venv do tesseract
    if TESSERACT is None:
        raise ValueError("A variável de ambiente TESSERACT não está configurada.")
    # tesseract_path = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    # pytesseract.pytesseract.tesseract_cmd = tesseract_path
    
    # tessdata_dir_config = '--tessdata-dir "C:/Program Files/Tesseract-OCR/tessdata"' # configura TESSDATA_PREFIX para o diretório de tessdata
    tessdata_dir = r"C:/Program Files/Tesseract-OCR/tessdata"
    if not os.path.exists(tessdata_dir):
        raise ValueError(f"O diretório tessdata não foi encontrado em {tessdata_dir}")

    pytesseract.pytesseract.tesseract_cmd = TESSERACT
    
    POPPLER = os.getenv('POPPLER') # captura a venv do POPPLER
    if os.name == 'nt':
        poppler_path = r"C:\Program Files\poppler-24.02.0\Library\bin"  # VERIFICAR
        os.environ['PATH'] += os.pathsep + poppler_path # configura o caminho do Poppler no Windows
        
    if not os.path.exists(output_img_dir):
        os.makedirs(output_img_dir)
        
    if not os.path.isfile(pdf_path):
        raise FileNotFoundError(f'O arquivo PDF não foi encontrado: {pdf_path}')
    
    try:
        img_pages = convert_from_path(pdf_path, 300) # transforma o pdf em imagem
    except Exception as error:
        print(f"Erro ao tentar converter PDF em imagens: {error}")
        return

    try:
        result = ''
        for page_number, page in enumerate(img_pages):
            img_path = os.path.join(output_img_dir, f'page_{page_number+1}.png') # cria o caminho do arquivo
            page.save(img_path, 'PNG') # salva
            img_file = Image.open(img_path) # lê o arquivo
            try:
                enhancer = ImageEnhance.Contrast(img_file.convert('L'))
                img_file = enhancer.enhance(2)
                custom_config = r'--oem 3 --psm 6'
                page_txt = pytesseract.image_to_string(img_file, lang='por', config=custom_config).lower() # transforma a imagem em texto
                page_txt = page_txt.replace('ª', 'a').replace('º', 'o')
            except Exception as error:
                print(f"Erro ao tentar converter a imagem em texto: {error}")
                return
            result += page_txt + '\n'
    except Exception as error:
        print(f"Erro ao tentar ...: {error}")
        return
           
    return result
    


# pdf_path = r"\\TJCE-SAI-01\Teceirização\RH - TERCEIRIZAÇÃO 2023\00. CONTROLES\DOCUMENTOS CADASTRAIS - Colaboradores\_ParaCadastro\Recadastro Geral Asseio + OF. 245-2023-CAC-Comarcas\Documentos Admissões\Fichas de Registro\MARIA JOSE DA SILVA.pdf"
# pdf_path = r"\\TJCE-SAI-01\Teceirização\RH - TERCEIRIZAÇÃO 2023\00. CONTROLES\DOCUMENTOS CADASTRAIS - Colaboradores\_ParaCadastro\Recadastro Geral Asseio + OF. 245-2023-CAC-Comarcas\Documentos Admissões\Fichas de Registro\SILVANE MARIA ASSUNCAO MARQUES.pdf"
# output_img_dir = 'output_img'
# pdf_img_to_txt(pdf_path, output_img_dir)
