# OPÇÃO 2
import os
import pandas as pd
import pyautogui as pya
from dotenv import load_dotenv
from personal_data import get_personals_data


# FILE_PATH = os.getenv('FILE_PATH1')
def get_links(link_tabela=None, link_diretorio=None):
    print(f'get_links: {link_tabela}')
    print(f'get_links: {link_diretorio}')
    if link_tabela:
        if "\\" in link_tabela:
            link_tabela = link_tabela.replace("\\", "/").strip('\'"')
        FILE_PATH = link_tabela
    else:
        FILE_PATH = os.getenv('FILE_PATH1')
    print(f'file_path: {FILE_PATH}')
    return FILE_PATH

# DADOS CONTRATUAIS
# Planilha Controle de Vagas
def get_order_worksheet():
    load_dotenv()
    FILE_PATH = get_links()
    SHEET_NAME = os.getenv('SHEET_NAME1')
    order_worksheet = pd.read_excel(FILE_PATH, sheet_name=SHEET_NAME, skiprows=6)
    order_worksheet = order_worksheet[['Tipo Movimento','Pessoa Afetada','Função','Data Início','Lotação','Status Pedido','Status Atualização Sistema']]
    order_worksheet['Data Início'] = pd.to_datetime(order_worksheet['Data Início'], errors='coerce')
    order_worksheet['Data Início'] = order_worksheet['Data Início'].dt.strftime('%d/%m/%Y')
    return order_worksheet


# Planilha Base Geral de Terceirizados ADMRH
def get_function_worksheet():
    load_dotenv()
    FILE_PATH = os.getenv('FILE_PATH2')
    SHEET_NAME = os.getenv('SHEET_NAME2')
    function_worksheet = pd.read_excel(FILE_PATH, sheet_name=SHEET_NAME)
    desired_columns = ['Empresa','Contrato','Função','Cód. Função']
    function_worksheet = function_worksheet[desired_columns].dropna(subset=['Empresa'])
    function_worksheet['Cód. Função'] = function_worksheet['Cód. Função'].fillna(0).astype(int).astype(str)
    
    return function_worksheet


# Planilha Base Geral de Lotações
def get_workplace_worksheet():
    load_dotenv()
    FILE_PATH = os.getenv('FILE_PATH3')
    SHEET_NAME = os.getenv('SHEET_NAME3')
    workplace_worksheet = pd.read_excel(FILE_PATH, sheet_name=SHEET_NAME)
    desired_columns = ['Lotação', 'Cod. Lotação']
    workplace_worksheet = workplace_worksheet[desired_columns]
    workplace_worksheet['Cod. Lotação'] = workplace_worksheet['Cod. Lotação'].fillna(0).astype(int).astype(str)
    
    return workplace_worksheet



def get_enterprises_worksheet():
    load_dotenv()
    FILE_PATH = os.getenv('FILE_PATH4')
    SHEET_NAME = os.getenv('SHEET_NAME4')
    enterprise_worksheet = pd.read_excel(FILE_PATH, sheet_name=SHEET_NAME, skiprows=1)
    return enterprise_worksheet
    

# RETURNS ALL CONTRACTUALS DATA
def get_contractuals_data(pdf_link):
    order_worksheet = get_order_worksheet()
    function_worksheet = get_function_worksheet()
    workplace_worksheet = get_workplace_worksheet()
    enterprise_worksheet = get_enterprises_worksheet()
    NAME = get_personals_data(pdf_link)['NAME']
    
    filtered_data = order_worksheet[order_worksheet['Pessoa Afetada'] == NAME]
    if filtered_data.empty:
        return None
    ADMISSION = filtered_data.iloc[0]['Data Início']
    FUNCTION = filtered_data.iloc[0]['Função']
    WORKPLACE = filtered_data.iloc[0]['Lotação']
    ORDER_STATUS = filtered_data.iloc[0]['Status Pedido']
    SYSTEM_ORDER = filtered_data.iloc[0]['Status Atualização Sistema']
    
    merged_data = pd.merge(filtered_data, function_worksheet, left_on='Função', right_on='Função', how='left')
    if merged_data.empty:
        return None
    ENTERPRISE = merged_data.iloc[0]['Empresa']
    CONTRACT = merged_data.iloc[0]['Contrato']
    FUNCTION_COD = merged_data.iloc[0]['Cód. Função']
    
    merged_data = pd.merge(merged_data, workplace_worksheet, left_on='Lotação', right_on='Lotação', how='left')
    if merged_data.empty:
        return None
    WORKPLACE_COD = merged_data.iloc[0]['Cod. Lotação']
    
    merged_data = pd.merge(merged_data, enterprise_worksheet, left_on='Empresa', right_on='Empresa', how='left')
    if merged_data.empty:
        return None
    ENTERPRISE_COD = merged_data.iloc[0]['Código']
    
    contractuals_data = {
        'ADMISSION' : ADMISSION,
        'FUNCTION' : FUNCTION,
        'WORKPLACE' : WORKPLACE,
        'ORDER_STATUS' : ORDER_STATUS,
        'SYSTEM_ORDER' : SYSTEM_ORDER,
        'ENTERPRISE' : ENTERPRISE,
        'CONTRACT' : CONTRACT,
        'FUNCTION_COD' : FUNCTION_COD,
        'WORKPLACE_COD' : WORKPLACE_COD,
        'ENTERPRISE_COD' : ENTERPRISE_COD
    }
    return contractuals_data


