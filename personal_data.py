import os
import re
import pandas as pd
import pyautogui as pya
from unidecode import unidecode
from pdfminer.high_level import extract_text
from pdfminer.layout import LAParams
from PyPDF2 import PdfReader


def process_pdf(pdf_link):
    personals_data_list = {}
    if "\\" in pdf_link:
            pdf_link = pdf_link.replace("\\", "/").strip('\'"')
    reader = PdfReader(pdf_link)
    num_pages = len(reader.pages)
    for page_index in range(num_pages):
        pdf_text = extract_pdf_text_from_page(pdf_link, page_index)
        pdf_text = unidecode(pdf_text)
        # print(pdf_text)
        personals_data = get_personals_data(pdf_text)
        page_number = page_index + 1
        personals_data_list[page_number] = personals_data
        # print(f'Dados da página {page_number}:')
        # print(personals_data_list[page_number])
    return personals_data_list


def get_personals_data(pdf_text):
    # pdf_text = extract_pdf_text(pdf_link)
    # pdf_text = unidecode(pdf_text)
    # reader = PdfReader(pdf_link)
    # num_pages = len(reader.pages)
    # for page_number in range(num_pages):
    #     pdf_text = extract_pdf_text_from_page(pdf_link, page_number)
    #     pdf_text = unidecode(pdf_text)
    personals_data = {    
        'NAME': get_name(pdf_text),
        'FATHER': get_father(pdf_text),
        'MOTHER': get_mother(pdf_text),
        'BIRTH': get_birth(pdf_text),
        'NATURALNESS': get_naturalness(pdf_text),
        'CIVIL_STATUS': get_civil_status(pdf_text),
        'GENDER': get_gender(pdf_text),
        'INSTRUCTION': get_instruction(pdf_text),
        'PHONE': get_fone(pdf_text),
        'CEP': get_cep(pdf_text),
        'RG': get_rg(pdf_text),
        'RACE': '',
        'CPF': get_cpf(pdf_text)
    }
    return personals_data


def extract_pdf_text_from_page(pdf_link, page_number):
    try:
        if "\\" in pdf_link:
            pdf_link = pdf_link.replace("\\", "/").strip('\'"')
        laparams = LAParams()
        with open(pdf_link, 'rb') as pdf_file:
            text = extract_text(pdf_file, page_numbers=[page_number], laparams=laparams)
            formatted_text = re.sub(":\n\n",": ", text).replace("\n\n","\n").replace(" :", ":")
        return formatted_text
    except Exception as e:
        print(f"Erro ao abrir o PDF: {e}")
        pya.alert(f"Erro ao abrir o PDF: {e}")
        return None   


def sanitize_filename(filename):
    return filename.replace('\n', '').replace('\r', '').replace('\\', '-').replace('/', '-').replace(':', '-').replace('*', '-').replace('?', '-').replace('"', '-').replace('<', '-').replace('>', '-').replace('|', '-')


def get_name(pdf_text): # OK
    try:
        pattern = r"NOME\s*:\s*([A-Z\s]+)"
        match = re.search(pattern, pdf_text, re.IGNORECASE)
        if match:
            result = match.group(1).strip().split('\n')[0].strip()
            result = sanitize_filename(result)
            return result
        else:
            pattern = r'EMPREGADO\s*:?\n?\s*(.+)'
            match = re.findall(pattern, pdf_text, re.IGNORECASE)
            if match:
                result = match[1].strip()
                return result
            else:
                return "Funcionario_Desconhecido"
    except Exception as error:
        print("Não foi possível capturar o 'NOME'.")
        print(error)
        return None


def get_father(pdf_text): # OK
    try:
        pattern = r"PAI\s*:\s*([A-Z\s]+?)(?=\s*MAE|$)"
        match = re.search(pattern, pdf_text, re.IGNORECASE)
        if match:
            result = match.group(1).split('\n')[0].strip()
            # result = match.group(1).strip()
            # if 'MAE' or 'MÃE' in result:
            #     result = result.upper().strip().split('MAE')
            return result
        else:
            pattern = r'PAI\s*:?\n?\s*(.+)'
            match = re.findall(pattern, pdf_text, re.IGNORECASE)
            if match:
                if 'NASCIMENTO' in match[0]:
                    result = match[1].strip()
                else:
                    result = match[0].strip()
                return result
            else:
                return None
    except Exception as error:
        print("Não foi possível capturar o 'PAI'.")
        print(error)
        return None


def get_mother(pdf_text): # OK
    try:
        pattern = r"MAE\s*:\s*([A-Z\s]+)"
        match = re.search(pattern, pdf_text, re.IGNORECASE)
        if match:
            result = match.group(1).split('\n')[0].strip()
            return result
        else:
            pattern = r":\s*([A-Z\s*]+)\n\s*MAE"
            match = re.search(pattern, pdf_text, re.IGNORECASE)
            if match:
                result = match.group(1).strip()
                return result
            else:
                pattern = r'MAE\s*:?\n?\s*(.+)'
                match = re.search(pattern, pdf_text, re.IGNORECASE)
                if match:
                    result = match.group(1).strip()
                    return result
                else:
                    return None
    except Exception as error:
        print("Não foi possível capturar a 'MÃE'.")
        print(error)
        return None


def get_birth(pdf_text): # OK
    try:
        pattern = r"NASCIMENTO\s*:\s*(\d{2}/\d{2}/\d{4})"
        match = re.search(pattern, pdf_text, re.IGNORECASE)
        if match:
            result = match.group(1).strip()
            return result
        else:
            pattern = r"NASCIMENTO\s*:?\n?\s*(\d{2}/\d{2}/\d{4})"
            match = re.search(pattern, pdf_text, re.IGNORECASE)
            if match:
                result = match.group(1).strip()
                return result
            else:
                return None
    except Exception as error:
        print("Não foi possível capturar a 'DATA DE NASCIMENTO'.")
        print(error)
        return None


def get_naturalness(pdf_text): # OK
    try:
        pattern = r"NATURALIDADE\s*:\s*(\b[A-Z\s]+\b)(?=\s*NACIONALIDADE|$)"
        match = re.search(pattern, pdf_text, re.IGNORECASE)
        if match:
            result = match.group(1).split('\n')[0].strip()
            return result
        else:
            pattern = r"NASCIMENTO\s*:\s*(\b[A-Z\s]+\b)"
            match = re.search(pattern, pdf_text, re.IGNORECASE)
            if match:
                result = match.group(1).strip()
                return result
            else:
                pattern = r'DE NASCIMENTO\s*:?\n?\s*(.+)'
                match = re.findall(pattern, pdf_text, re.IGNORECASE)
                if match:
                    result = match[1].strip().split('/')[0]
                    return result
                else:
                    return None
    except Exception as error:
        print("Não foi possível capturar a 'NATURALIDADE'.")
        print(error)
        return None


def get_civil_status(pdf_text): # OK
    try:
        pattern = r'CIVIL\s*:\s*(.*)'
        match = re.search(pattern, pdf_text, re.IGNORECASE)
        if match:
            result = match.group(1).strip()
        else:
            pattern = r'CIVIL\s*:\s*([A-Z\s]+)'
            match = re.search(pattern, pdf_text, re.IGNORECASE)
            if match:
                result = match.group(1).strip()
            else:
                pattern = r'CIVIL\s*:?\n?\s*(.+)'
                match = re.search(pattern, pdf_text, re.IGNORECASE)
                if match:
                    result = match.group(1).strip()
                else:
                    return None
        if 'CASADO' in result.upper():
            result = 'CASADO'
        elif 'SOLTEIRO' in result.upper():
            result = 'SOLTEIRO'
        elif 'UNIAO ESTAVEL' in result.upper():
            result = 'UNIAO ESTAVEL'
        else:
            result = 'OUTROS'
        return result
    except Exception as error:
        print("Não foi possível capturar o 'ESTADO CIVIL'.")
        print(error)
        return None

    
def get_gender(pdf_text): # OK
    try:
        # pattern = r"SEXO\s*:\s*(\b[A-Z\s])" #OK
        pattern = r':\s*(\b[A-Z\s])\s*SEXO'
        match = re.search(pattern, pdf_text, re.IGNORECASE)
        if match:
            result = match.group(0).strip()
        else:
            pattern = r'SEXO\s*:?\n?\s*(.+)'
            match = re.search(pattern, pdf_text, re.IGNORECASE)
            if match:
                result = match.group(1).strip()
            else:
                return None
        if 'MASCULINO' in result.upper() or 'M' in result[0].upper():
            result = 'M'
        elif 'FEMININO' in result.upper() or 'F' in result[0].upper():
            result = 'F'
        else:
            return None
        return result
    except Exception as error:
        print("Não foi possível capturar o 'GÊNERO'.")
        print(error)
        return None


def get_instruction(pdf_text):
    try:
        pattern = r"INSTRUCAO\s*:\s*([A-Z\s]+)"
        match = re.search(pattern, pdf_text, re.IGNORECASE)
        if match:
            result = match.group(0).strip()
        else:
            pattern = r'INSTRUCAO\s*:?\n?\s*(.+)'
            match = re.search(pattern, pdf_text, re.IGNORECASE)
            if match:
                result = match.group(1).strip()
            else:
                return None
        if 'MEDIO' in result.upper() and 'INCOMPLET' in result.upper():
            result = '6'
        elif 'MEDIO' in result.upper() and 'COMPLET' in result.upper():
            result = '7'
        elif 'SUPERIOR' in result.upper() and 'INCOMPLET' in result.upper():
            result = '8'
        elif 'SUPERIOR' in result.upper() and 'COMPLET' in result.upper():
            result = '9'
        elif 'POS' in result.upper():
            result = '9'
        else:
            result = '13'
        return result
    except Exception as error:
        print("Não foi possível capturar a 'INSTRUÇÃO'.")
        print(error)
        return None


def get_fone(pdf_text): # OK
    try:
        pattern = r"FONE\s*:?\n?\s*(\d{2}\s*\d{9})"
        match = re.search(pattern, pdf_text, re.IGNORECASE)
        if match:
            result = match.group(1).replace(' ','').strip()
            return result
        else:
            pattern = r"CELULAR\s*:?\n?\s*(\d{2}\s*\d{9})"
            match = re.search(pattern, pdf_text, re.IGNORECASE)
            if match:
                result = match.group(1).replace(' ','').strip()
                return result
            return None
    except Exception as error:
        print("Não foi possível capturar o 'TELEFONE'.")
        print(error)
        return None
          

def get_cep(pdf_text): # OK
    try:
        pattern = r"CEP\s*:?\n?\s*(\d{2}.?\d{3}-?\d{3})"
        match = re.findall(pattern, pdf_text, re.IGNORECASE)
        if match and len(match) > 1:
            result = match[1].strip()
            return result
        elif match and len(match) == 1:
            result = match[0].strip()
            return result
        else:
            pattern = r"(\d{2}\d{3}-\d{3})"
            match = re.findall(pattern, pdf_text, re.IGNORECASE)
            if match and len(match) > 1:
                result = match[1].strip()
                return result
            elif match and len(match) == 1:
                result = match[0].strip()
                return result
            # return None
    except Exception as error:
        print("Não foi possível capturar o 'CEP'.")
        print(error)
        return None

    
def get_rg(pdf_text): # OK
    try:
        pattern = r"IDENTIDADE\s*:\s*(\b\d{8,13}\b)"
        match = re.search(pattern, pdf_text, re.IGNORECASE)
        if match:
            result = match.group(1)
            return result
        else:
            pattern = r"RG\s*(?:NUMERO)?/?(?:ORGAO)?\s*:?\n?\s*(\d{8,13})"
            match = re.search(pattern, pdf_text, re.IGNORECASE)
            if match:
                result = match.group(0).strip().split()
                if any('NUMERO' in item.upper() for item in result):
                    return result[2]
                else:
                    return result[1]
            else:
                return None
    except Exception as error:
        print("Não foi possível capturar o 'RG'.")
        print(error)

    
def get_cpf(pdf_text): # OK
    try:
        # pattern = r"\b\d{3}\.\d{3}\.\d{3}-\d{2}\b" #OK
        pattern = r"\b\d{3}\.\d{3}\.\d{3}--?\d{2}\b" #OK
        match = re.search(pattern, pdf_text)
        if match:
            result = match.group(0).replace('-','').replace('.','')
            return result
        else:
            return None
    except Exception as error:
        print("Não foi possível capturar o 'CPF'.")
        print(error)
        return None



pdf_link = r"C:\Users\luigi\tjce.jus.br\Acompanhamento De Contratos - Documentos\RH TERCEIRIZAÇÃO 2024\00. CONTROLES\CONTROLE DE VAGAS E MOVIMENTAÇÕES\Relatórios\_MIGRAÇÕES DE CONTRATOS 2024\02 EDUCAÇÃO - OK\Registros\SABRINA FARIAS SOUZA DOS SANTOS.pdf"
pdf_link = r"C:\Users\luigi\tjce.jus.br\Acompanhamento De Contratos - Documentos\RH TERCEIRIZAÇÃO 2024\00. CONTROLES\CONTROLE DE VAGAS E MOVIMENTAÇÕES\Relatórios\_MIGRAÇÕES DE CONTRATOS 2024\02 EDUCAÇÃO - OK\Registros\LUANA MORAIS DE MELO.pdf"
print(process_pdf(pdf_link))
