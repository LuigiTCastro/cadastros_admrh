import os
import pandas as pd
from dotenv import load_dotenv
from personal_data import get_personals_data_list


def get_links(link_tabela=None):
    load_dotenv()
    if link_tabela:
        if "\\" in link_tabela:
            link_tabela = link_tabela.replace("\\", "/").strip('\'"')
        FILE_PATH = link_tabela
    else:
        FILE_PATH = os.getenv('FILE_PATH1')
    print(f'file_path: {FILE_PATH}')
    return FILE_PATH


# DADOS CONTRATUAIS
# Planilha Controle de Vagas / Planilha Específica de Recadastro - [LIMPAR]
def get_order_worksheet(link_tabela=None):
    load_dotenv()
    FILE_PATH = get_links(link_tabela)
    SHEET_NAME = os.getenv('SHEET_NAME1')
    order_worksheet = pd.read_excel(FILE_PATH, sheet_name=SHEET_NAME, skiprows=6)
    order_worksheet = order_worksheet[['Tipo Movimento','Pessoa Afetada','Função','Data Início','Lotação','Status Pedido','Status Atualização Sistema']]
    # order_worksheet = order_worksheet[['Tipo Movimento','Pessoa Afetada','Função','Data Início','Lotação','Status Pedido','Status Atualização Sistema', 'Status Planilha Desligamento']]  # SOMENTE P/ O ASSEIO
    order_worksheet = order_worksheet.loc[order_worksheet['Status Atualização Sistema'].str.upper() == 'PENDENTE']
    # order_worksheet = order_worksheet.loc[order_worksheet['Status Planilha Desligamento'].str.upper() == 'INATIVO'] # SOMENTE P/ O ASSEIO
    order_worksheet['Data Início'] = pd.to_datetime(order_worksheet['Data Início'], dayfirst=True, errors='coerce')
    order_worksheet['Data Início'] = order_worksheet['Data Início'].dt.strftime('%d/%m/%Y')
    return order_worksheet


# Planilha Base Geral de Funções ADMRH
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


# Planilha Base Códigos ADMRH
def get_enterprises_worksheet():
    load_dotenv()
    FILE_PATH = os.getenv('FILE_PATH4')
    SHEET_NAME = os.getenv('SHEET_NAME4')
    enterprise_worksheet = pd.read_excel(FILE_PATH, sheet_name=SHEET_NAME, skiprows=1)
    return enterprise_worksheet


# Planilha Base Geral de Terceirizados ADMRH
def get_employess_worksheet():
    load_dotenv()
    FILE_PATH = os.getenv('FILE_PATH5')
    SHEET_NAME = os.getenv('SHEET_NAME5')
    worksheet = pd.read_excel(FILE_PATH, sheet_name=SHEET_NAME)
    worksheet = worksheet[['Nome','CPF']]
    worksheet = worksheet.drop_duplicates(subset=['Nome'])
    return worksheet


# RETURNS ALL CONTRACTUALS DATA - [LIMPAR]
def get_contractuals_data(pdf_link=None):
    order_worksheet = get_order_worksheet()
    function_worksheet = get_function_worksheet()
    workplace_worksheet = get_workplace_worksheet()
    enterprise_worksheet = get_enterprises_worksheet()
    employees_worksheet = get_employess_worksheet()
    contractuals_data_list = {}
    
    if pdf_link:
        NAME = get_personals_data_list(pdf_link)[1]['NAME']
        print(f'Nome no PDF: {NAME}')
        order_worksheet = order_worksheet[order_worksheet['Pessoa Afetada'] == NAME]
    
    merged_worksheet = pd.merge(order_worksheet, function_worksheet, on='Função', how='left')
    merged_worksheet = pd.merge(merged_worksheet, workplace_worksheet, on='Lotação', how='left')
    merged_worksheet = pd.merge(merged_worksheet, enterprise_worksheet, on='Empresa', how='left')
    merged_worksheet = pd.merge(merged_worksheet, employees_worksheet, left_on='Pessoa Afetada', right_on='Nome', how='left')
    merged_worksheet.drop_duplicates(subset=['Pessoa Afetada'], inplace=True)
    
    if merged_worksheet.empty:
        print('Colaborador(es) não encontrado(s) na(s) planilha(s) base(s)')
        return None
    
    for index, row in merged_worksheet.iterrows():    
        if pd.isna(row['CPF']) or not str(row['CPF']).strip():
            print(f'CPF não encontrado para {row["Pessoa Afetada"]} na planilha geral. Pulando...')
            # continue
        
        contractuals_data = {
            'NAME' : row['Pessoa Afetada'],
            'CPF' : row['CPF'],
            'ADMISSION' : row['Data Início'],
            'FUNCTION' : row['Função'],
            'WORKPLACE' : row['Lotação'],
            'ORDER_STATUS' : row['Status Pedido'],
            'SYSTEM_STATUS' : row['Status Atualização Sistema'],
            # 'EXCLUSION_STATUS' : row['Status Planilha Desligamento'], # SOMENTE P/ O ASSEIO
            'ENTERPRISE' : row['Empresa'],
            'CONTRACT' : row['Contrato'],
            'FUNCTION_COD' : row['Cód. Função'],
            'WORKPLACE_COD' : row['Cod. Lotação'],
            'ENTERPRISE_COD' : row['Código']
        }

        contractuals_data_list[index] = contractuals_data
        print(contractuals_data['CPF'])
    return contractuals_data_list