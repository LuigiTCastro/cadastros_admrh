import os
import re
import pandas as pd
import pyautogui as pya
from pdfminer.high_level import extract_text
    

def get_personals_data(link_pdf):
    pdf_text = extract_pdf_document(link_pdf)
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

    
def extract_pdf_document(link_pdf):
    try:
        if "\\" in link_pdf:
            link_pdf = link_pdf.replace("\\", "/").strip('\'"')
        text = extract_text(link_pdf)
        formatted_text = re.sub(":\n\n",": ", text).replace("\n\n","\n").replace(" :", ":")
        return formatted_text
    except Exception as e:
        print(f"Erro ao abrir o PDF: {e}")
        pya.alert(f"Erro ao abrir o PDF: {e}")
        return None   


def get_name(pdf_text): # OK
    try:
        pattern = r"NOME\s*:\s*(.+)"
        match = re.search(pattern, pdf_text, re.IGNORECASE)
        if match:
            result = match.group(1).strip()
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
        pattern = r"PAI\s*:\s*([A-Z\s]+)"
        match = re.search(pattern, pdf_text, re.IGNORECASE)
        if match:
            result = match.group(1).split('\n')[0].strip()
            return result
        else:
            pattern = r'PAI\s*:?\n?\s*(.+)'
            match = re.search(pattern, pdf_text, re.IGNORECASE)
            if match:
                result = match.group(1).strip()
                return result
            else:
                return None
    except Exception as error:
        print("Não foi possível capturar o 'PAI'.")
        print(error)
        return None


def get_mother(pdf_text): # OK
    try:
        pattern = r"MÃE\s*:\s*([A-Z\s]+)"
        match = re.search(pattern, pdf_text, re.IGNORECASE)
        if match:
            result = match.group(1).split('\n')[0].strip()
            return result
        else:
            pattern = r":\s*([A-Z\s*]+)\n\s*MÃE"
            match = re.search(pattern, pdf_text, re.IGNORECASE)
            if match:
                result = match.group(1).strip()
                return result
            else:
                pattern = r'MÃE\s*:?\n?\s*(.+)'
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
        pattern = r"NATURALIDADE\s*:\s*(\b[A-Z\s]+\b)"
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
        pattern = r"INSTRUÇÃO\s*:\s*([A-Z\s]+)"
        # pattern = r"INSTRUÇÃO\s*:\s*(.*)"
        match = re.search(pattern, pdf_text, re.IGNORECASE)
        if match:
            result = match.group(0).strip()
        else:
            pattern = r'INSTRUÇÃO\s*:?\n?\s*(.+)'
            match = re.search(pattern, pdf_text, re.IGNORECASE)
            if match:
                result = match.group(1).strip()
            else:
                return None
        if 'MÉDIO' in result.upper() and 'INCOMPLET' in result.upper():
            result = '6'
        elif 'MÉDIO' in result.upper() and 'COMPLET' in result.upper():
            result = '7'
        elif 'SUPERIOR' in result.upper() and 'INCOMPLET' in result.upper():
            result = '8'
        elif 'SUPERIOR' in result.upper() and 'COMPLET' in result.upper():
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
            return None
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
            pattern = r"RG\s*(?:NÚMERO)?/?(?:ÓRGÃO)?\s*:?\n?\s*(\d{8,13})"
            match = re.search(pattern, pdf_text, re.IGNORECASE)
            if match:
                result = match.group(0).strip().split()
                if any('NÚMERO' in item.upper() for item in result):
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
        pattern = r"\b\d{3}\.\d{3}\.\d{3}-\d{2}\b" #OK
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



# print('\nDados Pessoais:\n------------------------------------------------------')
# print(get_personals_data(link_pdf))