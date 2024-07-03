import os
import re
import time
from dotenv import load_dotenv
import pyautogui as pya
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from personal_data import get_personals_data
from contractual_data import get_contractuals_data


def create_driver():
    driver = webdriver.Chrome()
    return driver


def access_system(driver):
    load_dotenv()
    URL_PATH = os.getenv('URL_PATH')
    USER = os.getenv('USER')
    PASSWORD = os.getenv('PASSWORD')
    
    # ACESSANDO O SISTEMA
    driver.get(URL_PATH)
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    
    # USUARIO
    user_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:txtDesUsuario_c')))
    user_field.send_keys(USER)

    # SENHA
    password_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:txtDesSenha_c')))
    password_field.send_keys(PASSWORD)

    # CLICAR PARA ENTRAR
    enter_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='ui-button-text ui-c']")))
    enter_button.click()
    
    # TABELAS
    tables_button = driver.find_elements(By.XPATH, "//h3[@class='ui-accordion-header ui-helper-reset ui-state-default ui-corner-all']")
    tables_button[0].click()
    
    # CADASTROS
    register_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Cadastro de Servidores/Magistrados')))
    register_button.click()


def import_of_existent_register(driver, personals_data, contractuals_data, matr):
    wait = WebDriverWait(driver, 10)
    NAME = personals_data['NAME']
    CPF = personals_data['CPF']
    ADMISSION = contractuals_data['ADMISSION']
    FUNCTION_COD = contractuals_data['FUNCTION_COD']
    WORKPLACE_COD = contractuals_data['WORKPLACE_COD']
    ENTERPRISE_COD = contractuals_data['ENTERPRISE_COD']
    PATTERN = 'NAO INFORMADO'
    TIME_COD = '1'
    CLASS_COD = 'A'
    COST_COD = '9'
    RELATION_COD = '4'
    
    # RELATÓRIO DE EXECUÇÃO
    with open('C:/Users/luigi/tjce.jus.br/Acompanhamento De Contratos - Documentos/RH TERCEIRIZAÇÃO 2024/00. CONTROLES/DOCUMENTOS CADASTRAIS - Colabs/_Para Cadastro/Execution Reports/report.csv', 'w') as report:
        report.write('Relatório de cadastrados realizados nessa execução:\n')
    try:
        new_button = wait.until(EC.element_to_be_clickable((By.ID, 'form:j_idt75')))
        new_button.click()
    except Exception as error:
        print("Erro ao tentar clicar no botão 'NOVO'")
        print(error)
        pya.alert("Erro ao tentar clicar no botão 'NOVO'")
    
    try:
        existent_register = wait.until(EC.element_to_be_clickable((By.ID, 'form:btn_importar_existente')))
        existent_register.click()
    except Exception as error:
        print("Erro ao tentar clicar no botão 'IMPORTAR DE REGISTRO EXISTENTE'")
        print(error)
        pya.alert("Erro ao tentar clicar no botão 'IMPORTAR DE REGISTRO EXISTENTE'")
        
    try:
        matr_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:lovCpMatricula_txt_cod')))
        matr_field.send_keys(matr)
        pya.press('tab')
        time.sleep(2)
    except Exception as error:
        print("Erro ao tentar inserir 'MATRÍCULA'")
        print(error)
        pya.alert("Erro ao tentar inserir 'MATRÍCULA'")
    
    # name_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:lovCpMatricula_txt_desc')))
    # name_field.send_keys()
    
    try:
        admission_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:txtAdmissaoCop_c_input')))
        admission_field.clear()
        admission_field.send_keys(ADMISSION)
        pya.press('tab')
        time.sleep(1)
    except Exception as error:
        print("Erro ao tentar cadastrar 'ADMISSÃO'")
        print(error)
        pya.alert("Erro ao tentar cadastrar 'ADMISSÃO'")

    try:        
        office_cod_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:lovCpCargo_txt_cod')))
        office_cod_field.clear()
        pya.press('tab')
        time.sleep(2)
        office_cod_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:lovCpCargo_txt_cod')))
        office_cod_field.send_keys(FUNCTION_COD)
        pya.press('tab')
        time.sleep(2)
    except Exception as error:
        print("Erro ao tentar cadastrar 'CÓDIGO FUNÇÃO'")
        print(error)
        pya.alert("Erro ao tentar cadastrar 'CÓDIGO FUNÇÃO'")
        
    try:        
        pattern_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:lovCpPadrao_txt_desc')))
        pattern_field.clear()
        pattern_field.send_keys(PATTERN)
        pya.press('tab')
        time.sleep(1)
    except Exception as error:
        print("Erro ao tentar cadastrar 'PADRÃO'")
        print(error)
        pya.alert("Erro ao tentar cadastrar 'PADRÃO'")
        
    try:
        time_cod_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:lovCpHorario_txt_cod')))
        time_cod_field.clear()
        pya.press('tab')
        time.sleep(1)
        time_desc_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:lovCpHorario_txt_desc')))
        time_desc_field.clear()
        pya.press('tab')
        time.sleep(1)
        time_cod_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:lovCpHorario_txt_cod')))
        time_cod_field.send_keys(TIME_COD)
        pya.press('tab')
        time.sleep(1)
    except Exception as error:
        print("Erro ao tentar cadastrar 'CÓDIGO HORÁRIO'")
        print(error)
        pya.alert("Erro ao tentar cadastrar 'CÓDIGO HORÁRIO'")
        
    try:
        class_cod_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:lovNivel_txt_cod')))
        class_cod_field.clear()
        class_cod_field.send_keys(CLASS_COD)
        pya.press('tab')
        time.sleep(1)
    except Exception as error:
        print("Erro ao tentar cadastrar 'CÓDIGO CLASSE'")
        print(error)
        pya.alert("Erro ao tentar cadastrar 'CÓDIGO CLASSE'")
        
    try:
        workplace_cod_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:lovCpSetor_txt_cod')))
        workplace_cod_field.clear()
        pya.press('tab')
        time.sleep(2)
        workplace_cod_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:lovCpSetor_txt_cod')))
        workplace_cod_field.send_keys(WORKPLACE_COD)
        pya.press('tab')
        time.sleep(2)
    except Exception as error:
        print("Erro ao tentar cadastrar 'CÓDIGO LOTAÇÃO'")
        print(error)
        pya.alert("Erro ao tentar cadastrar 'CÓDIGO LOTAÇÃO'")
    
    try:
        function_cod_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:lovCpFuncao_txt_cod')))
        function_cod_field.clear()
        pya.press('tab')
        time.sleep(2)
        function_cod_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:lovCpFuncao_txt_cod')))
        function_cod_field.send_keys(FUNCTION_COD)
        pya.press('tab')
        time.sleep(2)
    except Exception as error:
        print("Erro ao tentar cadastrar 'CÓDIGO FUNÇÃO'")
        print(error)
        pya.alert("Erro ao tentar cadastrar 'CÓDIGO FUNÇÃO'")
    
    try:
        cost_cod_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:lovCpCcusto_txt_cod')))
        cost_cod_field.clear()
        pya.press('tab')
        time.sleep(1)
        cost_cod_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:lovCpCcusto_txt_cod')))
        cost_cod_field.send_keys(COST_COD)
        pya.press('tab')
        time.sleep(1)
    except Exception as error:
        print("Erro ao tentar cadastrar 'CÓDIGO CUSTO'")
        print(error)
        pya.alert("Erro ao tentar cadastrar 'CÓDIGO CUSTO'")
    
    try:
        relation_cod_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:lovCpVinculo_txt_cod')))
        relation_cod_field.clear()
        pya.press('tab')
        time.sleep(1)
        relation_cod_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:lovCpVinculo_txt_cod')))
        relation_cod_field.send_keys(RELATION_COD)
        pya.press('tab')
        time.sleep(1)
    except Exception as error:
        print("Erro ao tentar cadastrar 'CÓDIGO VÍNCULO'")
        print(error)
        pya.alert("Erro ao tentar cadastrar 'CÓDIGO VÍNCULO'")
    
    try:
        register_button = wait.until(EC.element_to_be_clickable((By.ID, 'form:btn_confirma_copia_func')))
        register_button.click()
        time.sleep(5)
    except Exception as error:
        print("Erro ao tentar clicar no botão 'REGISTRAR'")
        print(error)
        pya.alert("Erro ao tentar clicar no botão 'REGISTRAR'")
    
    # PÓS MATRÍCULA
    # ---------------------------------------------------------------------------
    try:
        wait.until(EC.presence_of_element_located((By.ID, 'form:txtMatriculaCabInc_c')))
    except TimeoutException:
        wait.until(EC.presence_of_element_located((By.ID, 'form:txtMatriculaCabInc_c')))

    new_matr_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:txtMatriculaCabInc_c')))
    new_matr_txt = new_matr_field.get_attribute('value')
    print(f'tentativa matr txt 1: {new_matr_txt}')
    
    try:
        email_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:tabFuncionarios:txtEmail_c')))
        email_txt = email_field.get_attribute('value')
    except:
        email_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:tabFuncionarios:txtEmail')))
        email_txt = email_field.get_attribute('value')
    
    # if email_txt:
    #     add_email_button = wait.until(EC.element_to_be_clickable((By.ID, 'form:tabFuncionarios:btnAddMail')))
    #     add_email_button.click()
    #     new_email_button = wait.until(EC.element_to_be_clickable((By.ID, 'frmEmails:btnNovoEmail')))
    #     new_email_button.click()
    #     new_email_field = wait.until(EC.element_to_be_clickable((By.ID, 'frmEmail:txtEmailF_c')))
    #     new_email_field.send_keys(email_txt)
    #     type_button = wait.until(EC.element_to_be_clickable((By.ID, 'frmEmail:cboTipoF_c')))
    #     type_button.click()
    #     particular_option = wait.until(EC.visibility_of_element_located((By.XPATH, "//li[@data-label='1-Particular']")))
    #     particular_option.click()
    #     save_button = wait.until(EC.element_to_be_clickable((By.ID, 'frmEmail:btn_gravar')))
    #     save_button.click()
    #     time.sleep(2)
    #     try:
    #         close_button = wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='ui-icon ui-icon-closethick']")))
    #         print("Elemento encontrado. Verificando se está clicável.")
    #         close_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='ui-icon ui-icon-closethick']")))
    #         close_button.click()
    #         print("Elemento clicado com sucesso.")

    #     except TimeoutException as e:
    #         print("TimeoutException: Não foi possível encontrar ou clicar no elemento dentro do tempo limite.")
    #         raise e
    # else:
    #     email_field.clear()
    #     email_field.send_keys(f'{new_matr_txt}@tjce.jus.br')
    email_field.clear()
    email_field.send_keys(f'{new_matr_txt}@tjce.jus.br')
     
    general_save_button = wait.until(EC.element_to_be_clickable((By.ID, 'form:btnGravar_Funcionarios')))
    general_save_button.click()
    time.sleep(5)
        
    professional_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[@class='ui-state-default ui-corner-top']")))
    professional_button.click()
    
    covenant_cod_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:tabFuncionarios:lovConvOut_txt_cod')))
    # covenant_cod_value = covenant_cod_field.text
    covenant_cod_value = covenant_cod_field.get_attribute('value')
    if covenant_cod_value:
        covenant_cod_field.clear()
        covenant_cod_field.send_keys(ENTERPRISE_COD)
    pya.press('tab')
    time.sleep(1)
    
    general_save_button = wait.until(EC.element_to_be_clickable((By.ID, 'form:btnGravar_Funcionarios')))
    general_save_button.click()
    time.sleep(5)
    
    # RELATÓRIO DE EXECUÇÃO
    with open('C:/Users/luigi/tjce.jus.br/Acompanhamento De Contratos - Documentos/RH TERCEIRIZAÇÃO 2024/00. CONTROLES/DOCUMENTOS CADASTRAIS - Colabs/_Para Cadastro/Execution Reports/report.csv', 'a') as report:
        report.write(f'{NAME} - {CPF} - {new_matr_txt} - Feito')


def include_manually(driver, personals_data, contractuals_data):
    wait = WebDriverWait(driver, 10)
    print('Incluir manualmente')
    
    # PERSONALS DATA
    NAME = personals_data['NAME']
    FATHER = personals_data['FATHER']
    MOTHER = personals_data['MOTHER']
    BIRTH = personals_data['BIRTH']
    NATURALNESS = personals_data['NATURALNESS']
    CIVIL_STATUS = personals_data['CIVIL_STATUS']
    GENDER = personals_data['GENDER']
    INSTRUCTION = personals_data['INSTRUCTION']
    PHONE = personals_data['PHONE']
    CEP = personals_data['CEP']
    RG = personals_data['RG']
    RACE = personals_data['RACE']
    CPF = personals_data['CPF']
    
    # CONTRACTUALS DATA
    ADMISSION = contractuals_data['ADMISSION']
    FUNCTION_COD = contractuals_data['FUNCTION_COD']
    WORKPLACE_COD = contractuals_data['WORKPLACE_COD']
    ENTERPRISE_COD = contractuals_data['ENTERPRISE_COD']
    PATTERN = 'NAO INFORMADO' 
    TIME_COD = '1' 
    COST_COD = '9' 
    RELATION_COD = '4' 
    
    with open('C:/Users/luigi/tjce.jus.br/Acompanhamento De Contratos - Documentos/RH TERCEIRIZAÇÃO 2024/00. CONTROLES/DOCUMENTOS CADASTRAIS - Colabs/_Para Cadastro/Execution Reports/report.csv', 'w') as report:
        report.write('Relatório de cadastrados realizados nessa execução:\n')
    
    try:
        wait.until(EC.presence_of_element_located((By.ID, 'form:j_idt75')))    
    except TimeoutException:
        wait.until(EC.presence_of_element_located((By.ID, 'form:j_idt75')))    
        
    new_button = wait.until(EC.element_to_be_clickable((By.ID, 'form:j_idt75')))
    new_button.click()
    
    manual_register = wait.until(EC.element_to_be_clickable((By.ID, 'form:btn_digitar_novo')))
    manual_register.click()
    
    # PERSONAL DATA
    # -----------------------------------------------------------------------------------------------------
    try:
        name_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:txtNomeCab_c')))
        name_field.send_keys(NAME)
    except Exception as error:
        print("Erro ao tentar registrar 'NOME'")
        print(error)
        pya.alert("Erro ao tentar registrar 'NOME'")
    
    try:
        cpf_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:txtCpf_c')))
        cpf_field.click()
        pya.press('home')
        cpf_field.send_keys(CPF)
    except Exception as error:
        print("Erro ao tentar registrar 'CPF'")
        print(error)
        pya.alert("Erro ao tentar registrar 'CPF'")
    
    try:
        admission_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:txtAdmissao_c_input')))
        admission_field.send_keys(ADMISSION)
    except Exception as error:
        print("Erro ao tentar registrar 'ADMISSÃO'")
        print(error)
        pya.alert("Erro ao tentar registrar 'ADMISSÃO'")

    try:
        cep_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:txtCep_empresa_c'))) # TO ANALYZE
        cep_field.click()
        pya.press('home')
        cep_field.send_keys(CEP)
        pya.press('tab')
        time.sleep(3)
    except Exception as error:
        print("Erro ao tentar registrar 'CEP'")
        print(error)
        pya.alert("Erro ao tentar registrar 'CEP'")
    
    try:
        cellphone_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:txtCelular_c')))
        cellphone_field.send_keys(PHONE)
    except:
        cellphone_field.send_keys('')
        
    try:
        naturalness_cod_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:lovNatural_txt_cod'))) # THIS NEEDS OF THE CODE
        # naturalness_cod_field.send_keys(NATURALNESS)
        naturalness_cod_field.send_keys('2304400') # CORRIGIR
        pya.press('tab')
        time.sleep(1)
    except Exception as error:
        print("Erro ao tentar registrar 'NATURALIDADE'")
        print(error)
        pya.alert("Erro ao tentar registrar 'NATURALIDADE'")
        
    try:
        instruction_cod_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:lovGrauInst_txt_cod'))) # THIS NEEDS OF THE CODE
        instruction_cod_field.send_keys(INSTRUCTION)
        pya.press('tab')
        time.sleep(1)
    except Exception as error:
        print("Erro ao tentar registrar 'INSTRUÇÃO'")
        print(error)
        pya.alert("Erro ao tentar registrar 'INSTRUÇÃO'")
        
    try:
        rg_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:txtIdentidade_c'))) # INCOMPLETE INFORMATION
        rg_field.send_keys(RG)
        rg_agency = wait.until(EC.element_to_be_clickable((By.ID, 'form:txtOrgaoexp_c')))
        rg_agency.send_keys('SSPDS')
        rg_uf = wait.until(EC.element_to_be_clickable((By.ID, 'form:cboIdentidadeuf_c_label')))
        rg_uf.click()
        # ce_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[@data-label='CE']")))
        # ce_option.click()
        pya.write('ce')
        pya.press('tab')
    except:
        print("Erro ao tentar cadastrar RG")
    
    try:
        birth_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:txtDtnascimento_c_input')))
        birth_field.send_keys(BIRTH)
        pya.press('tab')
        time.sleep(1)
    except Exception as error:
        print("Erro ao tentar registrar 'DATA DE NASCIMENTO'")
        print(error)
        pya.alert("Erro ao tentar registrar 'DATA DE NASCIMENTO'")
        
    try:
        gender_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:cboSexo_c_label')))
        gender_field.click()
        time.sleep(1)
        if GENDER == 'F':
            female_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[@data-label='Feminino']")))
            female_option.click()
        elif GENDER == 'M':
            male_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[@data-label='Masculino']")))
            male_option.click()
        else:
            pya.alert('Gênero não reconhecido')
        time.sleep(1)
    except Exception as error:
        print("Erro ao tentar registrar 'GÊNERO'")
        print(error)
        pya.alert("Erro ao tentar registrar 'GÊNERO'")
    
    try:
        civil_status_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:cboEC_c_label')))
        civil_status_field.click()
        time.sleep(1)
        if CIVIL_STATUS.upper() == 'SOLTEIRO':
            option = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[@data-label='SOLTEIRO']")))
            option.click()
        elif CIVIL_STATUS.upper() == 'CASADO':
            option = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[@data-label='CASADO']")))
            option.click()
        elif CIVIL_STATUS.upper() == 'UNIAO ESTAVEL':
            option = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[@data-label='UNIAO ESTAVEL']")))
            option.click()
        else:
            option = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[@data-label='OUTROS']")))
            option.click()
        time.sleep(1)
    except Exception as error:
        print("Erro ao tentar cadastrar 'ESTADO CIVIL'")
        print(error)
        pya.alert("Erro ao tentar cadastrar 'ESTADO CIVIL'")
        
    try:
        race_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:cboCor_c_label')))
        race_field.click()
        time.sleep(1)
        if RACE == '':
            uninformed_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[@data-label='Não Informado']")))
            uninformed_option.click()
        time.sleep(1) # CORRIGIR
    except Exception as error:
        print("Erro ao tentar registrar 'RAÇA'")
        print(error)
        pya.alert("Erro ao tentar registrar 'RAÇA'")
    
    try:    
        deficiency_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:cboDeficiencias_c_label')))
        deficiency_field.click()
        time.sleep(1)
        not_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[@data-label='Não']")))
        not_option.click()
        time.sleep(1)
    except Exception as error:
        print("Erro ao tentar registrar 'DEFICIÊNCIA'")
        print(error)
        pya.alert("Erro ao tentar registrar 'DEFICIÊNCIA'")
        
    try:
        next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='ui-button-icon-left ui-icon ui-c ui-icon-arrowthick-1-e']")))
        next_button.click()
        time.sleep(3)
    except Exception as error:
        print("Erro ao tentar clicar no botão 'PRÓXIMO'")
        print(error)
        pya.alert("Erro ao tentar clicar no botão 'PRÓXIMO'")
        
    # PROFESSIONAL DATA
    # -----------------------------------------------------------------------------------------------------
    try:
        relation_cod_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:lovVinculo_txt_cod')))
        relation_cod_field.send_keys(RELATION_COD)
        pya.press('tab')
        time.sleep(2)
    except Exception as error:
        print("Erro ao tentar registrar 'VÍNCULO'")
        pya.alert("Erro ao tentar registrar 'VÍNCULO'")
        
    try:
        type_adm_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:lovAdmissao_txt_cod')))
        type_adm_field.send_keys('1')
        pya.press('tab')
        time.sleep(2)
    except Exception as error:
        print("Erro ao tentar registrar 'TIPO ADMISSÃO'")
        pya.alert("Erro ao tentar registrar 'TIPO ADMISSÃO'")
    
    
    try:
        time_cod_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:lovHorario_txt_cod')))
        time_cod_field.send_keys(TIME_COD)
        pya.press('tab')
        time.sleep(2)
    except Exception as error:
        print("Erro ao tentar registrar 'HORÁRIO'")
        pya.alert("Erro ao tentar registrar 'HORÁRIO'")
        
    try:
        covenant_cod_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:lovConvOut_txt_cod')))
        covenant_cod_field.send_keys(str(ENTERPRISE_COD))
        pya.press('tab')
        time.sleep(2)
    except Exception as error:
        print("Erro ao tentar registrar 'CONVÊNIO'")
        pya.alert("Erro ao tentar registrar 'CONVÊNIO'")
        
    try:
        workplace_cod_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:lovSetor_txt_cod')))
        workplace_cod_field.send_keys(WORKPLACE_COD)
        pya.press('tab')
        time.sleep(2)
    except Exception as error:
        print("Erro ao tentar registrar 'LOTAÇÃO'")
        pya.alert("Erro ao tentar registrar 'LOTAÇÃO'")
        
    try:
        office_cod_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:lovCargo_txt_cod')))
        office_cod_field.send_keys(FUNCTION_COD)
        pya.press('tab')
        time.sleep(3)
    except Exception as error:
        print("Erro ao tentar registrar 'CARGO'")
        pya.alert("Erro ao tentar registrar 'CARGO'")
        
    try:
        function_cod_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:lovFuncao_txt_cod')))
        function_cod_field.send_keys(FUNCTION_COD)
        pya.press('tab')
        time.sleep(3)
    except Exception as error:
        print("Erro ao tentar registrar 'FUNÇÃO'")
        pya.alert("Erro ao tentar registrar 'FUNÇÃO'")
    
    
    try:
        cost_cod_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:lovCcusto_txt_cod')))
        cost_cod_field.send_keys(COST_COD)
        pya.press('tab')
        time.sleep(2)
    except Exception as error:
        print("Erro ao tentar registrar 'C.CUSTO'")
        pya.alert("Erro ao tentar registrar 'C.CUSTO'")
        
    try:
        pattern_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:lovPadrao_txt_desc')))
        pattern_field.send_keys(PATTERN)
        pya.press('tab')
        time.sleep(2)
    except Exception as error:
        print("Erro ao tentar registrar 'PADRÃO'")
        pya.alert("Erro ao tentar registrar 'PADRÃO'")
        
    try:
        specie_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:txtModalidadepg_c_label')))
        specie_field.click()
        time.sleep(1)
        pya.write('outros')
        pya.press('tab')
        time.sleep(1)
    except Exception as error:
        print("Erro ao tentar registrar 'ESPÉCIE'")
        pya.alert("Erro ao tentar registrar 'ESPÉCIE'")
    
    try:
        payment_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:cboTiposalbase_c_label')))
        payment_field.click()
        time.sleep(1)
        pya.write('outros')
        pya.press('tab')
        time.sleep(1)
    except Exception as error:
        print("Erro ao tentar registrar 'TIPO PAGAMENTO'")
        pya.alert("Erro ao tentar registrar 'TIPO PAGAMENTO'")
    
    try:
        salary_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:txtSalbase_c')))
        salary_field.send_keys('0')
        pya.press('tab')
        time.sleep(1)
    except Exception as error:
        print("Erro ao tentar registrar 'SALÁRIO'")
        pya.alert("Erro ao tentar registrar 'SALÁRIO'")
        
    try:
        next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='ui-button-icon-left ui-icon ui-c ui-icon-arrowthick-1-e']")))
        next_button.click()
        time.sleep(3)
    except Exception as error:
        print("Erro ao tentar clicar no botão 'PRÓXIMO'")
        pya.alert("Erro ao tentar clicar no botão 'PRÓXIMO'")
        
        
    # DEPENDENTS
    # -----------------------------------------------------------------------------------------------------
    try:
        mother_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='ui-button-icon-left ui-icon ui-c icon-editar']")))
        mother_button.click()
        time.sleep(1)
        
        mother_field = wait.until(EC.element_to_be_clickable((By.ID, "frmDependente:txtNome_c")))
        mother_field.send_keys(MOTHER)
        time.sleep(1)
        
        save_button = wait.until(EC.element_to_be_clickable((By.ID, "frmDependente:btn_gravar")))
        save_button.click()
        time.sleep(2)
    except Exception as error:
        print("Erro ao tentar registrar 'MÃE'")
        print(error)
        pya.alert("Erro ao tentar registrar 'MÃE'")
        
    try:
        father_button = wait.until(EC.element_to_be_clickable((By.ID, "form:tabDependentes:1:btn_edita_dependente")))
        father_button.click()
        time.sleep(1)
        
        father_field = wait.until(EC.element_to_be_clickable((By.ID, "frmDependente:txtNome_c")))
        father_field.send_keys(FATHER)
        time.sleep(1)
        
        save_button = wait.until(EC.element_to_be_clickable((By.ID, "frmDependente:btn_gravar")))
        save_button.click()
        time.sleep(2)
    except Exception as error:
        print("Erro ao tentar registrar 'PAI'")
        print(error)
        pya.alert("Erro ao tentar registrar 'PAI'")

    if CIVIL_STATUS.upper() == 'CASADO':
        try:
            try:
                wait.until(EC.presence_of_element_located((By.ID, "form:tabDependentes:2:btn_edita_dependente")))    
            except TimeoutException:
                wait.until(EC.presence_of_element_located((By.ID, "form:tabDependentes:2:btn_edita_dependente")))    
            partner_button = wait.until(EC.element_to_be_clickable((By.ID, "form:tabDependentes:2:btn_edita_dependente")))
            partner_button.click()
            time.sleep(1)
            
            partner_field = wait.until(EC.element_to_be_clickable((By.ID, "frmDependente:txtNome_c")))
            partner_field.send_keys('N/C')
            time.sleep(1)
            
            gender_button = wait.until(EC.element_to_be_clickable((By.ID, "frmDependente:cboSexo_c")))
            gender_button.click()
            time.sleep(1)
            if GENDER == "M":
                female_option = wait.until(EC.element_to_be_clickable((By.ID, "frmDependente:cboSexo_c_1")))
                female_option.click()
            elif GENDER == "F":
                male_option = wait.until(EC.element_to_be_clickable((By.ID, "frmDependente:cboSexo_c_2")))
                male_option.click()
                
            save_button = wait.until(EC.element_to_be_clickable((By.ID, "frmDependente:btn_gravar")))
            save_button.click()
            time.sleep(2)
        except Exception as error:
            print("Erro ao tentar cadastrar 'CÔNJUGE'")
            print(error)
            pya.alert("Erro ao tentar cadastrar 'CÔNJUGE'")

    try:
        try:
            wait.until(EC.presence_of_element_located((By.ID, "form:btn_finalizar_dependentes")))    
        except TimeoutException:
            wait.until(EC.presence_of_element_located((By.ID, "form:btn_finalizar_dependentes")))    
        finish_button = wait.until(EC.element_to_be_clickable((By.ID, "form:btn_finalizar_dependentes")))
        finish_button.click()
    except:
        print('Erro ao tentar finalizar cadastro')
        pya.alert('Erro ao tentar finalizar cadastro')
    time.sleep(10)
        
        
    # PÓS MATRÍCULA
    # ---------------------------------------------------------------------------
    try:
        wait.until(EC.presence_of_element_located((By.ID, 'form:txtMatriculaCabInc_c')))
    except TimeoutException:
        wait.until(EC.presence_of_element_located((By.ID, 'form:txtMatriculaCabInc_c')))

    new_matr_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:txtMatriculaCabInc_c')))
    new_matr_txt = new_matr_field.get_attribute('value')
    print(f'tentativa matr txt 1: {new_matr_txt}')
    
    # try:
    #     new_matr_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:txtMatriculaCabInc')))
    #     print(f'tentativa 2: {new_matr_field}')
    # except:
    #     new_matr_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:j_idt2179')))
    #     print(f'tentativa 3: {new_matr_field}')
    
    # pya.alert('Observar matrícula')
    
    try:
        email_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:tabFuncionarios:txtEmail_c')))
        email_txt = email_field.get_attribute('value')
    except:
        email_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:tabFuncionarios:txtEmail')))
        email_txt = email_field.get_attribute('value')
    
    if email_txt:
        add_email_button = wait.until(EC.element_to_be_clickable((By.ID, 'form:tabFuncionarios:btnAddMail')))
        add_email_button.click()
        new_email_button = wait.until(EC.element_to_be_clickable((By.ID, 'frmEmails:btnNovoEmail')))
        new_email_button.click()
        new_email_field = wait.until(EC.element_to_be_clickable((By.ID, 'frmEmail:txtEmailF_c')))
        new_email_field.send_keys(email_txt)
        type_button = wait.until(EC.element_to_be_clickable((By.ID, 'frmEmail:cboTipoF_c')))
        type_button.click()
        particular_option = wait.until(EC.visibility_of_element_located((By.XPATH, "//li[@data-label='1-Particular']")))
        particular_option.click()
        save_button = wait.until(EC.element_to_be_clickable((By.ID, 'frmEmail:btn_gravar')))
        save_button.click()
        time.sleep(2)
        close_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='ui-icon ui-icon-closethick']")))
        close_button.click()
        email_field.clear()
        email_field.send_keys(f'{new_matr_txt}@tjce.jus.br')
    else:
        email_field.clear()
        email_field.send_keys(f'{new_matr_txt}@tjce.jus.br')
     
    general_save_button = wait.until(EC.element_to_be_clickable((By.ID, 'form:btnGravar_Funcionarios')))
    general_save_button.click()
    time.sleep(5)
    
    # RELATÓRIO DE EXECUÇÃO
    with open('C:/Users/luigi/tjce.jus.br/Acompanhamento De Contratos - Documentos/RH TERCEIRIZAÇÃO 2024/00. CONTROLES/DOCUMENTOS CADASTRAIS - Colabs/_Para Cadastro/Execution Reports/report.csv', 'a') as report:
        report.write(f'{NAME} - {CPF} - {new_matr_txt} - Feito')
    
    
def register(driver, personals_data, contractuals_data):    
    wait = WebDriverWait(driver, 10)
    CPF = personals_data['CPF']
    
    ## JÁ TEM CADASTRO? (como verificar?)
    try:
        cpf_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:table_Funcionarios:j_idt119:filter')))
        cpf_field.clear()
        cpf_field.send_keys(CPF)
        time.sleep(2)
    except Exception as error:
        print("Campo CPF não encontrado")
        print(error)
        pya.alert('Campo CPF não encontrado')
    
    returned_active_value = wait.until(EC.element_to_be_clickable((By.ID, "form:table_Funcionarios_data")))
    returned_active_value_txt = returned_active_value.text
    
    cpf_pattern = r"\b\d{3}\.\d{3}\.\d{3}-\d{2}\b"
    cpf_match = re.search(cpf_pattern, returned_active_value_txt)
    if cpf_match:
        cpf_result = cpf_match.group(0).replace('.','').replace('-','')
        if cpf_result == CPF:
            # ENCERRAR
            return pya.alert('ESTE CPF JÁ POSSUI CADASTRO ATIVO.')
        else:
            print('cpf_result encontrado, mas diferente do CPF')
    
    print('ESTE CPF NÃO POSSUI CADASTRO ATIVO.')
    time.sleep(2)
        
    # BOTÃO DESLIGADOS
    off_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='ui-radiobutton-icon ui-icon ui-icon-blank ui-c']")))
    off_button.click()
    time.sleep(3)
    
    # JÁ TEVE CADASTRO? (como verificar?)
    try:
        cpf_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:table_Funcionarios:j_idt119:filter')))
        cpf_field.clear()
        cpf_field.send_keys(CPF)
        time.sleep(2)
    except Exception as error:
        print("Campo CPF não encontrado")
        print(error)
        pya.alert('Campo CPF não encontrado')
    
    returned_inactive_value = wait.until(EC.element_to_be_clickable((By.ID, "form:table_Funcionarios_data")))
    returned_inactive_value_txt = returned_inactive_value.text
    
    cpf_pattern = r"\b\d{3}\.\d{3}\.\d{3}-\d{2}\b"
    cpf_match = re.search(cpf_pattern, returned_inactive_value_txt)
    if cpf_match:
        cpf_result = cpf_match.group(0).replace('.','').replace('-','')
        if cpf_result == CPF:
            print('ESTE CPF JÁ POSSUI HISTÓRICO INATIVO.')
            matr_value = wait.until(EC.element_to_be_clickable((By.XPATH, "//td[@class='xcp_column_Number']")))
            MATR = matr_value.text.replace('.','')
            # IMPORTAR DE CADASTRO EXISTENTE
            print('Import of existent_register')
            import_of_existent_register(driver, personals_data, contractuals_data, MATR)
    else:
        print('ESTE CPF NÃO POSSUI NENHUM REGISTRO NO TJ.')
        # INCLUIR MANUALMENTE
        include_manually(driver, personals_data, contractuals_data)


def handle_website(driver, personals_data, contractuals_data):
    access_system(driver)
    register(driver, personals_data, contractuals_data)
    
    pya.alert('Encerrando a aplicação. Clique em OK.')
    driver.quit()


def run_application(link_pdf):
    personals_data = get_personals_data(link_pdf)
    contractuals_data = get_contractuals_data(link_pdf)
    
    if not personals_data or not contractuals_data:
        print('Dados não encontrados.')
        pya.alert('Dados não encontrados')
        return
        
    print(f'\nDados Pessoais:\n-------------------------------------------------\n{personals_data}')
    print(f'\nDados Contratuais:\n-------------------------------------------------\n{contractuals_data}')
    
    driver = create_driver()
    handle_website(driver, personals_data, contractuals_data)
    