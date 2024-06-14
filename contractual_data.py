# OPÇÃO 2
import os
import pandas as pd
import pyautogui as pya
from dotenv import load_dotenv
from personal_data import get_name


load_dotenv()

# DADOS CONTRATUAIS
# Planilha Controle de Vagas
def get_order_worksheet():
    FILE_PATH1 = os.getenv('FILE_PATH1')
    SHEET_NAME1 = os.getenv('SHEET_NAME1')
    order_worksheet = pd.read_excel(FILE_PATH1, sheet_name=SHEET_NAME1, skiprows=6)
    order_worksheet = order_worksheet[['Tipo Movimento','Pessoa Afetada','Função','Data Início','Lotação','Status Pedido','Status Atualização Sistema']]
    order_worksheet['Data Início'] = pd.to_datetime(order_worksheet['Data Início'], errors='coerce')
    order_worksheet['Data Início'] = order_worksheet['Data Início'].dt.strftime('%d/%m/%Y')
    
    return order_worksheet


# Planilha Base Geral de Terceirizados ADMRH
def get_function_worksheet():
    FILE_PATH2 = os.getenv('FILE_PATH2')
    SHEET_NAME2 = os.getenv('SHEET_NAME2')
    function_worksheet = pd.read_excel(FILE_PATH2, sheet_name=SHEET_NAME2)
    desired_columns = ['EMPRESA','CONTRATO','FUNÇÃO','CÓD. FUNÇÃO']
    function_worksheet = function_worksheet[desired_columns].dropna(subset=['EMPRESA'])
    function_worksheet['CÓD. FUNÇÃO'] = function_worksheet['CÓD. FUNÇÃO'].fillna(0).astype(int).astype(str)
    
    return function_worksheet


# Planilha Base Geral de Lotações
def get_workplace_worksheet():
    FILE_PATH3 = os.getenv('FILE_PATH3')
    SHEET_NAME3 = os.getenv('SHEET_NAME3')
    workplace_worksheet = pd.read_excel(FILE_PATH3, sheet_name=SHEET_NAME3)
    desired_columns = ['Lotação', 'Cod. Lotação']
    workplace_worksheet = workplace_worksheet[desired_columns]
    workplace_worksheet['Cod. Lotação'] = workplace_worksheet['Cod. Lotação'].fillna(0).astype(int).astype(str)
    
    return workplace_worksheet


# RETURNS ALL CONTRACTUALS DATA
def get_contractuals_data():
    order_worksheet = get_order_worksheet()
    function_worksheet = get_function_worksheet()
    workplace_worksheet = get_workplace_worksheet()
    result_name = get_name()
    
    filtered_data = order_worksheet[order_worksheet['Pessoa Afetada'] == result_name]
    
    if filtered_data.empty:
        return None
    
    admissão = filtered_data.iloc[0]['Data Início']
    função = filtered_data.iloc[0]['Função']
    lotação = filtered_data.iloc[0]['Lotação']
    status_pedido = filtered_data.iloc[0]['Status Pedido']
    status_sistema = filtered_data.iloc[0]['Status Atualização Sistema']
    
    merged_data = pd.merge(filtered_data, function_worksheet, left_on='Função', right_on='FUNÇÃO', how='left')
    
    if merged_data.empty:
        return None
    
    empresa = merged_data.iloc[0]['EMPRESA']
    contrato = merged_data.iloc[0]['CONTRATO']
    cod_função = merged_data.iloc[0]['CÓD. FUNÇÃO']
    
    merged_data = pd.merge(merged_data, workplace_worksheet, left_on='Lotação', right_on='Lotação', how='left')
    
    if merged_data.empty:
        return None
    
    cod_lotação = merged_data.iloc[0]['Cod. Lotação']
    
    return admissão, função, cod_função, lotação, cod_lotação, contrato, empresa, status_pedido, status_sistema



print(get_contractuals_data())