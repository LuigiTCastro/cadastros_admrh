import os
import re
import fitz
import pandas as pd
import pyautogui as pya
from dotenv import load_dotenv


# READ PDF 
def get_pdf_document(link_pdf):
    try:
        pdf_document = fitz.open(link_pdf)
        result_text = ''
        for page_num in range(len(pdf_document)):
            page = pdf_document.load_page(page_num)
            result_text += page.get_text()
        return result_text
    except Exception as e:
        print(f"Erro ao abrir o PDF: {e}")
        return None

load_dotenv()
LINK_PDF = os.getenv('LINK_PDF')
if "\\" in LINK_PDF:
    LINK_PDF = LINK_PDF.replace("\\", "/").strip('\'"')
result_text = get_pdf_document(LINK_PDF)
# print(result_text)


def get_personals_data():
    personals_data = {    
        'name': get_name(),
        'father': get_father(),
        'mother': get_mother(),
        'birth': get_birth(),
        'naturalness': get_naturalness(),
        'civil_status': get_civil_status(),
        'gender': get_gender(),
        'instruction': get_instruction(),
        'phone': get_fone(),
        'cep': get_cep(),
        'rg': get_rg(),
        'race': '',
        'CPF': get_cpf()
    }
    return personals_data


def get_name():
    try:
        pattern = r"NOME\s*:\s*(\b[A-Z\s]+\b)" #OK
        pattern2 = r"ELEITORAL\s*:\s*(\b[A-Z\s]+\b)" #OK
        match = re.search(pattern, result_text, re.IGNORECASE)
        if match:
            split_match = match.group(1).split()
            result = ' '.join(n for n in split_match if n != 'NATURALIDADE')
            # if match == None:
            if result == 'PIS':
                match = re.search(pattern2, result_text)
                split_match = match.group().split()
                if 'ELEITORAL' in split_match:
                    split_match = match.group(1).split()
                    result = ' '.join(n for n in split_match if n != 'NATURALIDADE')
            return result
        else:
            return None        
    except Exception as error:
        print("Não foi possível capturar o 'NOME'.")
        print(error)
        pya.alert(error)
        return None


def get_father():
    try:
        pattern = r"(\d{7})\s*([A-Z\s]+)\s*([A-Z\s]+)\s*\b\d{2}/\d{2}/\d{4}\b" #OK
        match = re.search(pattern, result_text, re.IGNORECASE)
        if match == None:
            result = 'N/C'
            return result
        else:
            split_match = match.group(0).split('\n')
            result = split_match[1]
            return result
    except Exception as error:
        print("Não foi possível capturar o 'PAI'.")
        print(error)
        pya.alert(error)


def get_mother():
    try:
        pattern = r"(\d{7})\s*([A-Z\s]+)\s*([A-Z\s]+)\s*\b\d{2}/\d{2}/\d{4}\b" #OK
        match = re.search(pattern, result_text, re.IGNORECASE)
        if match == None:
            result = 'N/C'
            return result
        else:
            split_match = match.group(0).split('\n')
            result = split_match[2]
            return result
    except Exception as error:
        print("Não foi possível capturar a 'MÃE'.")
        print(error)
        pya.alert(error)


def get_birth():
    try:
        pattern = r'\b\d{2}/\d{2}/\d{4}\b' #OK
        match = re.search(pattern, result_text)
        if match:
            result = match.group(0).strip()
            return result
        else:
            return None
    except Exception as error:
        print("Não foi possível capturar o 'NASCIMENTO'.")
        print(error)
        pya.alert(error)


def get_naturalness():
    try:
        pattern = r"BAIRRO\s*:\s*(\b[A-Z\s]+\b)\s*-\s*"
        match = re.search(pattern, result_text, re.IGNORECASE)
        if match:
            naturalidade = match.group(1).strip()
            return naturalidade
        else:
            pattern = r'BAIRRO\s*:\s*([^\n]+)\s*-\s*'
            match = re.search(pattern, result_text, re.IGNORECASE)
            if match:
                naturalidade = match.group(1).strip()
                return naturalidade
            else:
                return None
    except Exception as error:
        print("Não foi possível capturar a 'NATURALIDADE'.")
        print(error)
        pya.alert(error)


def get_civil_status():
    try:
        pattern = r'SEXO\s*:\s*(.*?)CEP' #OK
        match = re.search(pattern, result_text, re.DOTALL)
        if match:
            array_text = match.group(1).strip().split()
            if array_text[0] == 'M' or array_text[0] == 'F':
                # result = ' '.join(n for n in extracted_text if n != 'M' or n != 'F')
                extracted_text = array_text[1]
            else:
                extracted_text = array_text
            if extracted_text[-3:] == '(a)':
                # result = re.search(r'\b(\w+)\b', extracted_text, re.IGNORECASE)
                result = extracted_text[:-3:]
                return result
            else:
                result = extracted_text
                return result
        else:
            return None
    except Exception as error:
        print("Não foi possível capturar o 'ESTADO CIVIL'.")
        print(error)
        pya.alert(error)

    
def get_gender():
    try:
        pattern = r"SEXO\s*:\s*(\b[A-Z\s])" #OK
        match = re.search(pattern, result_text)
        if match:
            result = match.group(1)
            return result
        else:
            return None
    except Exception as error:
        print("Não foi possível capturar o 'GÊNERO'.")
        print(error)
        pya.alert(error)


def get_instruction():
    try:
        pattern = r"/\d{4}\b\s*(\b[A-Za-z\s]+\b)"
        match = re.search(pattern, result_text)
        if match:
            birth_pattern = r'\b\d{2}/\d{2}/\d{4}\b' #OK
            birth_match = re.search(birth_pattern, result_text)
            text_end = birth_match.end()
            text_after = result_text[text_end:].strip()
            lines = text_after.split('\n')
            result = lines[0]
            return result
        else:
            return None
    except Exception as error:
        print("Não foi possível capturar a 'INSTRUÇÃO'.")
        print(error)
        pya.alert(error)


def get_fone():
    try:
        pattern = r"FONE\s*:\s*(\d{11})" #OK
        match = re.search(pattern, result_text)
        if match:
            result = match.group(1)
            return result
        else:
            None
    except Exception as error:
        print("Não foi possível capturar o 'TELEFONE'.")
        print(error)
        pya.alert(error)
        
        
def get_cep():
    try:
        pattern = r"CEP\s*:\s*(\d{8})" #OK
        match = re.findall(pattern, result_text)
        if match:
            result = match[1]
            return result
        else:
            None
    except Exception as error:
        print("Não foi possível capturar o 'CEP'.")
        print(error)
        pya.alert(error)

    
def get_rg():
    try:
        pattern = r"\b\d{8,13}\b" #OK
        match = re.findall(pattern, result_text)
        if match:
            result = match[1]
            return result
        else:
            None
    except Exception as error:
        print("Não foi possível capturar o 'RG'.")
        print(error)
        pya.alert(error)

    
def get_cpf():
    try:
        pattern = r"\b\d{3}\.\d{3}\.\d{3}-\d{2}\b" #OK
        match = re.search(pattern, result_text)
        if match:
            result = match.group(0).replace('-','').replace('.','')
            return result
        else:
            None
    except Exception as error:
        print("Não foi possível capturar o 'CPF'.")
        print(error)
        pya.alert(error)




print(get_personals_data())
# print(get_name())