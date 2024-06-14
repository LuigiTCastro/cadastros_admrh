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
from personal_data import get_cpf, get_name, get_father, get_mother, get_birth, get_naturalness, get_civil_status, get_gender, get_instruction, get_fone, get_cep, get_rg
from contractual_data import get_contractuals_data

load_dotenv()
URL_PATH = os.getenv('URL_PATH')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')

# PERSONAL DATA
name_value = get_name()
father_value = get_father()
mother_value = get_mother()
birth_value = get_birth()
naturalness_value = get_naturalness()
civil_status_value = get_civil_status()
gender_value = get_gender()
instruction_value = get_instruction()
phone_value = get_fone()
cep_value = get_cep()
rg_value = get_rg()
race_value = ''
CPF = get_cpf()

# CONTRACTUALS DATA
admissão, função, cod_função, lotação, cod_lotação, contrato, empresa, status_pedido, status_sistema = get_contractuals_data()
MATR = ''
ADMISSION = admissão
FUNCTION_COD = cod_função
PATTERN = 'NAO INFORMADO' # OK
TIME_COD = '1' # OK
CLASS_COD = 'A' # OK
WORKPLACE_COD = cod_lotação
COST_COD = '9' # OK
RELATION_COD = '4' # OK


def create_driver():
    driver = webdriver.Chrome()
    return driver


def access_system(driver):
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


def import_of_existent_register(driver, matr):
    wait = WebDriverWait(driver, 10)
    
    # RELATÓRIO DE EXECUÇÃO
    with open('C:/Users/luigi/tjce.jus.br/Acompanhamento De Contratos - Documentos/RH TERCEIRIZAÇÃO 2024/00. CONTROLES/DOCUMENTOS CADASTRAIS - Colabs/_Para Cadastro/Execution Reports/report.csv', 'w') as report:
        report.write('Relatório de cadastrados realizados nessa execução:\n')
    
    new_button = wait.until(EC.element_to_be_clickable((By.ID, 'form:j_idt75')))
    new_button.click()
    
    existent_register = wait.until(EC.element_to_be_clickable((By.ID, 'form:btn_importar_existente')))
    existent_register.click()
    
    matr_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:lovCpMatricula_txt_cod')))
    matr_field.send_keys(matr)
    pya.press('tab')
    time.sleep(2)
    
    # name_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:lovCpMatricula_txt_desc')))
    # name_field.send_keys()
    
    admission_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:txtAdmissaoCop_c_input')))
    admission_field.clear()
    admission_field.send_keys(ADMISSION)
    pya.press('tab')
    time.sleep(1)
    
    office_cod_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:lovCpCargo_txt_cod')))
    office_cod_field.clear()
    pya.press('tab')
    time.sleep(2)
    office_cod_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:lovCpCargo_txt_cod')))
    office_cod_field.send_keys(FUNCTION_COD)
    pya.press('tab')
    time.sleep(2)
    
    pattern_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:lovCpPadrao_txt_desc')))
    pattern_field.clear()
    pattern_field.send_keys(PATTERN)
    pya.press('tab')
    time.sleep(1)
    
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
    
    class_cod_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:lovNivel_txt_cod')))
    class_cod_field.clear()
    class_cod_field.send_keys(CLASS_COD)
    pya.press('tab')
    time.sleep(1)
    
    workplace_cod_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:lovCpSetor_txt_cod')))
    workplace_cod_field.clear()
    pya.press('tab')
    time.sleep(2)
    workplace_cod_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:lovCpSetor_txt_cod')))
    workplace_cod_field.send_keys(WORKPLACE_COD)
    pya.press('tab')
    time.sleep(2)
    
    function_cod_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:lovCpFuncao_txt_cod')))
    function_cod_field.clear()
    pya.press('tab')
    time.sleep(2)
    function_cod_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:lovCpFuncao_txt_cod')))
    function_cod_field.send_keys(FUNCTION_COD)
    pya.press('tab')
    time.sleep(2)
    
    cost_cod_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:lovCpCcusto_txt_cod')))
    cost_cod_field.clear()
    pya.press('tab')
    time.sleep(1)
    cost_cod_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:lovCpCcusto_txt_cod')))
    cost_cod_field.send_keys(COST_COD)
    pya.press('tab')
    time.sleep(1)
    
    relation_cod_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:lovCpVinculo_txt_cod')))
    relation_cod_field.clear()
    pya.press('tab')
    time.sleep(1)
    relation_cod_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:lovCpVinculo_txt_cod')))
    relation_cod_field.send_keys(RELATION_COD)
    pya.press('tab')
    time.sleep(1)
    
    register_button = wait.until(EC.element_to_be_clickable((By.ID, 'form:btn_confirma_copia_func')))
    register_button.click()
    time.sleep(5)
    
    # PÓS MATRÍCULA
    # ---------------------------------------------------------------------------
    try:
        wait.until(EC.presence_of_element_located((By.ID, 'form:txtMatriculaCabInc_c')))
    except TimeoutException:
        wait.until(EC.presence_of_element_located((By.ID, 'form:txtMatriculaCabInc_c')))
        
    new_matr_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:txtMatriculaCabInc_c')))
    new_matr_text = new_matr_field.text
    
    email_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:tabFuncionarios:txtEmail_c')))
    email_text = email_field.text
    if email_text:
        add_email_button = wait.until(EC.element_to_be_clickable((By.ID, 'form:tabFuncionarios:btnAddMail')))
        add_email_button.click()
        new_email_button = wait.until(EC.element_to_be_clickable((By.ID, 'frmEmails:btnNovoEmail')))
        new_email_button.click()
        new_email_field = wait.until(EC.element_to_be_clickable((By.ID, 'frmEmail:txtEmailF_c')))
        new_email_field.send_keys(email_text)
        type_button = wait.until(EC.element_to_be_clickable((By.ID, 'frmEmail:cboTipoF_c')))
        type_button.click()
        particular_option = wait.until(EC.visibility_of_element_located((By.XPATH, "//li[@data-label='1-Particular']")))
        particular_option.click()
        save_button = wait.until(EC.element_to_be_clickable((By.ID, 'frmEmail:btn_gravar')))
        save_button.click()
        time.sleep(2)
        close_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='ui-icon ui-icon-closethick']")))
        close_button.click()
        email_field.send_keys(f'{new_matr_text}@tjce.jus.br')
    else:
        email_field.send_keys(f'{new_matr_text}@tjce.jus.br')
        
    professional_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[@class='ui-state-default ui-corner-top']")))
    professional_button.click()
    
    covenant_cod_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:tabFuncionarios:lovConvOut_txt_cod')))
    covenant_cod_text = covenant_cod_field.text
    if covenant_cod_text:
        covenant_cod_field.clear()
        covenant_cod_field.send_keys('?')
    pya.press('tab')
    time.sleep(1)
    
    general_save_button = wait.until(EC.element_to_be_clickable((By.ID, 'form:btnGravar_Funcionarios')))
    general_save_button.click()
    time.sleep(5)
    
    # RELATÓRIO DE EXECUÇÃO
    with open('C:/Users/luigi/tjce.jus.br/Acompanhamento De Contratos - Documentos/RH TERCEIRIZAÇÃO 2024/00. CONTROLES/DOCUMENTOS CADASTRAIS - Colabs/_Para Cadastro/Execution Reports/report.csv', 'a') as report:
        report.write(f'{name_value} - {CPF} - {new_matr_text} - Feito')


def include_manually(driver):
    wait = WebDriverWait(driver, 10)
    print('Incluir manualmente')
    
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
    name_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:txtNomeCab_c')))
    name_field.send_keys(name_value)
    
    cpf_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:txtCpf_c')))
    cpf_field.click()
    pya.press('home')
    cpf_field.send_keys(CPF)
    
    admission_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:txtAdmissao_c_input')))
    admission_field.send_keys(ADMISSION)
    
    cep_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:txtCep_empresa_c'))) # TO ANALYZE
    cep_field.click()
    pya.press('home')
    cep_field.send_keys(cep_value)
    pya.press('tab')
    time.sleep(3)
    
    cellphone_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:txtCelular_c')))
    cellphone_field.send_keys(phone_value)
    
    naturalness_cod_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:lovNatural_txt_cod'))) # THIS NEEDS OF THE CODE
    # naturalness_cod_field.send_keys(naturalness_value)
    naturalness_cod_field.send_keys('2304400') # CORRIGIR
    pya.press('tab')
    time.sleep(1)
    
    instruction_cod_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:lovGrauInst_txt_cod'))) # THIS NEEDS OF THE CODE
    # instruction_cod_field.send_keys(instruction_value)
    instruction_cod_field.send_keys('8') # CORRIGIR
    pya.press('tab')
    time.sleep(1)
    
    rg_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:txtIdentidade_c'))) # INCOMPLETE INFORMATION
    rg_field.send_keys(rg_value)
    rg_agency = wait.until(EC.element_to_be_clickable((By.ID, 'form:txtOrgaoexp_c')))
    rg_agency.send_keys('SSPDS')
    rg_uf = wait.until(EC.element_to_be_clickable((By.ID, 'form:cboIdentidadeuf_c_label')))
    rg_uf.click()
    # ce_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[@data-label='CE']")))
    # ce_option.click()
    pya.write('ce')
    pya.press('tab')
    
    birth_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:txtDtnascimento_c_input')))
    birth_field.send_keys(birth_value)
    pya.press('tab')
    time.sleep(1)
    
    gender_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:cboSexo_c_label')))
    gender_field.click()
    time.sleep(1)
    if gender_value == 'F':
        female_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[@data-label='Feminino']")))
        female_option.click()
    elif gender_value == 'M':
        male_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[@data-label='Masculino']")))
        male_option.click()
    else:
        pya.alert('Gênero não reconhecido')
    time.sleep(1)
    
    civil_status_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:cboEC_c_label')))
    civil_status_field.click()
    time.sleep(1)
    if civil_status_value == 'Solteiro':
        single_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[@data-label='SOLTEIRO']")))
        single_option.click()
    elif civil_status_value == 'Casado':
        married_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[@data-label='CASADO']")))
        married_option.click()
    time.sleep(1)
    
    race_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:cboCor_c_label')))
    race_field.click()
    time.sleep(1)
    if race_value == '':
        uninformed_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[@data-label='Não Informado']")))
        uninformed_option.click()
    time.sleep(1) # CORRIGIR
    
    deficiency_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:cboDeficiencias_c_label')))
    deficiency_field.click()
    time.sleep(1)
    not_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[@data-label='Não']")))
    not_option.click()
    time.sleep(1)
    
    next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='ui-button-icon-left ui-icon ui-c ui-icon-arrowthick-1-e']")))
    next_button.click()
    time.sleep(3)
    
    # PROFESSIONAL DATA
    # -----------------------------------------------------------------------------------------------------
    relation_cod_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:lovVinculo_txt_cod')))
    relation_cod_field.send_keys('4')
    pya.press('tab')
    time.sleep(2)
    
    type_adm_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:lovAdmissao_txt_cod')))
    type_adm_field.send_keys('1')
    pya.press('tab')
    time.sleep(2)
    
    time_cod_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:lovHorario_txt_cod')))
    time_cod_field.send_keys('1')
    pya.press('tab')
    time.sleep(2)
    
    covenant_cod_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:lovConvOut_txt_cod')))
    covenant_cod_field.send_keys('314944882') # CORRIGIR
    pya.press('tab')
    time.sleep(2)
    
    workplace_cod_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:lovSetor_txt_cod')))
    workplace_cod_field.send_keys(WORKPLACE_COD)
    pya.press('tab')
    time.sleep(2)
    
    office_cod_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:lovCargo_txt_cod')))
    office_cod_field.send_keys(FUNCTION_COD)
    pya.press('tab')
    time.sleep(2)
    
    function_cod_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:lovFuncao_txt_cod')))
    function_cod_field.send_keys(FUNCTION_COD)
    pya.press('tab')
    time.sleep(2)
    
    cost_cod_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:lovCcusto_txt_cod')))
    cost_cod_field.send_keys(9)
    pya.press('tab')
    time.sleep(2)
    
    pattern_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:lovPadrao_txt_desc')))
    pattern_field.send_keys('NÃO INFORMADO')
    pya.press('tab')
    time.sleep(2)
    
    specie_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:txtModalidadepg_c_label')))
    specie_field.click()
    time.sleep(1)
    pya.write('outros')
    pya.press('tab')
    time.sleep(1)
    
    payment_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:cboTiposalbase_c_label')))
    payment_field.click()
    time.sleep(1)
    pya.write('outros')
    pya.press('tab')
    time.sleep(1)
    
    salary_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:txtSalbase_c')))
    salary_field.send_keys('0')
    pya.press('tab')
    time.sleep(1)
    
    next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='ui-button-icon-left ui-icon ui-c ui-icon-arrowthick-1-e']")))
    next_button.click()
    time.sleep(3)
    
    # DEPENDENTS
    # -----------------------------------------------------------------------------------------------------
    try:
        mother_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='ui-button-icon-left ui-icon ui-c icon-editar']")))
        mother_button.click()
        time.sleep(1)
        
        mother_field = wait.until(EC.element_to_be_clickable((By.ID, "frmDependente:txtNome_c")))
        mother_field.send_keys(mother_value)
        time.sleep(1)
        
        save_button = wait.until(EC.element_to_be_clickable((By.ID, "frmDependente:btn_gravar")))
        save_button.click()
        time.sleep(1)
    except:
        pya.alert("Erro ao cadastrar 'Mãe'.")
        
    try:
        father_button = wait.until(EC.element_to_be_clickable((By.ID, "form:tabDependentes:1:btn_edita_dependente")))
        father_button.click()
        time.sleep(1)
        
        father_field = wait.until(EC.element_to_be_clickable((By.ID, "frmDependente:txtNome_c")))
        father_field.send_keys(father_value)
        time.sleep(1)
        
        save_button = wait.until(EC.element_to_be_clickable((By.ID, "frmDependente:btn_gravar")))
        save_button.click()
        time.sleep(1)
    except:
        pya.alert("Erro ao cadastrar 'Pai'.")

    if civil_status_value == 'Casado':
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
            if gender_value == "M":
                female_option = wait.until(EC.element_to_be_clickable((By.ID, "frmDependente:cboSexo_c_1")))
                female_option.click()
            elif gender_value == "F":
                male_option = wait.until(EC.element_to_be_clickable((By.ID, "frmDependente:cboSexo_c_2")))
                male_option.click()
                
            
            save_button = wait.until(EC.element_to_be_clickable((By.ID, "frmDependente:btn_gravar")))
            save_button.click()
            time.sleep(1)
        except:
            print('Erro ao cadastrar cônjuge')
            pya.alert('Erro ao cadastrar cônjuge')

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

    new_matr_field1 = wait.until(EC.element_to_be_clickable((By.ID, 'form:txtMatriculaCabInc_c')))
    print(f'tentativa 1: {new_matr_field1}')
    
    try:
        new_matr_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:txtMatriculaCabInc')))
        print(f'tentativa 2: {new_matr_field}')
    except:
        new_matr_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:j_idt2179')))
        print(f'tentativa 3: {new_matr_field}')
    
    try:
        new_matr_text = new_matr_field.text
        print(new_matr_text)
    except:
        new_matr_text = new_matr_field.value
        print(new_matr_text)
    
    pya.alert('Observar matrícula')
    
    try:
        email_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:tabFuncionarios:txtEmail_c')))
        print(f'tentativa 1 - text: {email_field.text}')
        print(f'tentativa 1 - value: {email_field.value}')
    except:
        email_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:tabFuncionarios:txtEmail')))
        print(f'tentativa 2 - text: {email_field.text}')
        print(f'tentativa 2 - value: {email_field.value}')
    
    if email_field.text:
        add_email_button = wait.until(EC.element_to_be_clickable((By.ID, 'form:tabFuncionarios:btnAddMail')))
        add_email_button.click()
        new_email_button = wait.until(EC.element_to_be_clickable((By.ID, 'frmEmails:btnNovoEmail')))
        new_email_button.click()
        new_email_field = wait.until(EC.element_to_be_clickable((By.ID, 'frmEmail:txtEmailF_c')))
        new_email_field.send_keys(email_field.text)
        type_button = wait.until(EC.element_to_be_clickable((By.ID, 'frmEmail:cboTipoF_c')))
        type_button.click()
        particular_option = wait.until(EC.visibility_of_element_located((By.XPATH, "//li[@data-label='1-Particular']")))
        particular_option.click()
        save_button = wait.until(EC.element_to_be_clickable((By.ID, 'frmEmail:btn_gravar')))
        save_button.click()
        time.sleep(2)
        close_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='ui-icon ui-icon-closethick']")))
        close_button.click()
        email_field.send_keys(f'{new_matr_text}@tjce.jus.br')
    else:
        email_field.send_keys(f'{new_matr_text}@tjce.jus.br')
     
    general_save_button = wait.until(EC.element_to_be_clickable((By.ID, 'form:btnGravar_Funcionarios')))
    general_save_button.click()
    time.sleep(5)
    
    # RELATÓRIO DE EXECUÇÃO
    with open('C:/Users/luigi/tjce.jus.br/Acompanhamento De Contratos - Documentos/RH TERCEIRIZAÇÃO 2024/00. CONTROLES/DOCUMENTOS CADASTRAIS - Colabs/_Para Cadastro/Execution Reports/report.csv', 'a') as report:
        report.write(f'{name_value} - {CPF} - {new_matr_text} - Feito')
    
    
def to_register(driver):    
    wait = WebDriverWait(driver, 10)
    
    ## JÁ TEM CADASTRO? (como verificar?)
    try:
        cpf_field = wait.until(EC.element_to_be_clickable((By.ID, 'form:table_Funcionarios:j_idt119:filter')))
        cpf_field.clear()
        cpf_field.send_keys(CPF)
        time.sleep(2)
    except:
        pya.alert('Campo CPF não encontrado')
        print("Campo CPF não encontrado")
    
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
    except:
        print("Campo CPF não encontrado")
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
            import_of_existent_register(driver, MATR)
    else:
        print('ESTE CPF NÃO POSSUI NENHUM REGISTRO NO TJ.')
        # INCLUIR MANUALMENTE
        include_manually(driver)


def handle_website(driver):
    access_system(driver)
    to_register(driver)
    
    pya.alert('Encerrando a aplicação. Clique em OK.')
    driver.quit()


driver = create_driver()
handle_website(driver)