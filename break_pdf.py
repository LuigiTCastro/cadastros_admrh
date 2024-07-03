from pdfminer.high_level import extract_text
import PyPDF2
import re
import os

def extract_employee_name(text):
    try:
        pattern = r"NOME\s*:\s*([A-Z\s]+)"
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            result = match.group(1).strip()
            return result
        else:
            pattern = r"EMPREGADO\s*:\s*([A-Z\s]+)"
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                result = match.group(1).strip()
                return result
            else:
                pattern = r'EMPREGADO\s*\n\s*(.+)'
                match = re.findall(pattern, text, re.IGNORECASE)
                if match:
                    result = match[1].strip()
                    return result
                else:
                    return "Funcionario_Desconhecido"
    except Exception as error:
        print("Não foi possível capturar o 'NOME'.")
        print(error)
        return None



def extract_pdf_document(link_pdf):
    try:
        pdf_reader = PyPDF2.PdfReader(link_pdf)
        num_pages = len(pdf_reader.pages)
        
        formatted_texts = []
        
        for i in range(num_pages):
            page_text = extract_text(link_pdf, page_numbers=[i])
            formatted_text = re.sub(":\n\n",": ", page_text).replace("\n\n","\n").replace(" :", ":")
            formatted_texts.append(formatted_text)
        return formatted_texts
        
    except Exception as e:
        print(f"Erro ao abrir o PDF: {e}")
        return None   
        
        

def split_pdf_and_save(link_pdf, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    # RELATÓRIO DE EXECUÇÃO
    with open(r"C:\Users\luigi\tjce.jus.br\Acompanhamento De Contratos - Documentos\RH TERCEIRIZAÇÃO 2024\00. CONTROLES\CONTROLE DE VAGAS E MOVIMENTAÇÕES\Relatórios\_MIGRAÇÕES DE CONTRATOS 2024\02 EDUCAÇÃO\Registros\report.csv", 'w') as report:
        report.write('Relatório de PDFS extraídos nessa execução:\n')
        with open(link_pdf, "rb") as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            num_pages = len(pdf_reader.pages)
            
            formatted_texts = extract_pdf_document(link_pdf)
            
            for i in range(num_pages):
                page_text = formatted_texts[i]
                employee_name = extract_employee_name(page_text)
                
                if employee_name:
                    output_pdf_path = os.path.join(output_dir, f"{employee_name}.pdf")
                    pdf_writer = PyPDF2.PdfWriter()
                    pdf_writer.add_page(pdf_reader.pages[i])
                    
                    with open(output_pdf_path, "wb") as output_pdf_file:
                        pdf_writer.write(output_pdf_file)
                    print(f"Saved {output_pdf_path}")
                    
                    with open(r"C:\Users\luigi\tjce.jus.br\Acompanhamento De Contratos - Documentos\RH TERCEIRIZAÇÃO 2024\00. CONTROLES\CONTROLE DE VAGAS E MOVIMENTAÇÕES\Relatórios\_MIGRAÇÕES DE CONTRATOS 2024\02 EDUCAÇÃO\Registros\report.csv", 'a') as report:
                        report.write(f'{employee_name}\n')
                else:
                    non = f'Não possível extrair o nome da página {i+1}'
                    report.write(f'{non}\n')
                



# LINK_PDF = r
# OUTPUT_DIR = r
# split_pdf_and_save(LINK_PDF, OUTPUT_DIR)
