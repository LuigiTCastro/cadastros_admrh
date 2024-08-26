# <!-- a desenvolver -->
# [NOVA_LÓGICA_E_LAYOUT]
# Cadastrar
# 	Inserir/Fornecer PDF
# 		Base Padrão [rodar aplicação]
# 		Alterar Base
#           Fornecer novo link [rodar aplicação]

# Recadastrar
# 	Iterar Tabela de Recadastro
# 		Base Padrão [rodar aplicação]
#		Alterar Base
#           Fornecer novo link [rodar aplicação]
  
# [FINALIZAR]
  
import tkinter as tk
from functools import partial
from system_fields import run_application


def center_window(window):
    """Centraliza uma janela na tela."""
    window.update_idletasks()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window_width = window.winfo_reqwidth()
    window_height = window.winfo_reqheight()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    window.geometry(f'+{x}+{y}')

# Em desenvolvimento
def on_submit_base_link(box, base_link, pdf_link=None):
    box.destroy()
    print(f'Link da nova base submetido: {base_link}')
    print('A aplicação será executada')
    # Desenvolver lógica para alterar a base antes de rodar a aplicação
    run_application(pdf_link)


def base_changing_box(pdf_link=None):
    new_box = tk.Tk()
    new_box.title('Dialog box')
    new_box.geometry('600x200')
    center_window(new_box)    
    
    tk.Label(new_box).pack(expand=True, pady=1)
    tk.Label(new_box, text='Alterar link da base de movimentações').pack(expand=True, pady=5)
    
    input_field = tk.Entry(new_box, width=80)
    input_field.pack(pady=5)
        
    submit_button = tk.Button(new_box, text='Enviar', command=lambda: on_submit_base_link(new_box, input_field.get(), pdf_link))
    submit_button.pack(expand=True, pady=10)
    
    tk.Label(new_box).pack(expand=True, pady=1)
    
    new_box.mainloop()


def change_base(box, pdf_link=None):
    print('Alterar base selecionado')
    box.destroy()
    base_changing_box(pdf_link)


def default_base(box, pdf_link=None):
    print('Base padrão selecionada')
    box.destroy()
    print('A aplicação será executada')
    run_application(pdf_link)


def open_new_box(pdf_link=None):
    print('Nova caixa de diálogo aberta')
    new_box = tk.Tk()
    new_box.title('Dialog box')
    new_box.geometry('300x200')
    center_window(new_box)

    label = tk.Label(new_box, text='Escolha um dos modos abaixo:')
    label.pack(expand=True, pady=1)
    
    button1 = tk.Button(new_box, text='Base Padrão', command=partial(default_base, new_box, pdf_link), width=25, height=1)
    button1.pack(pady=10)
    
    button2 = tk.Button(new_box, text='Alterar Base', command=partial(change_base, new_box, pdf_link), width=25, height=1)
    button2.pack(pady=10)
    
    label = tk.Label(new_box)
    label.pack(expand=True, pady=1)
    
    new_box.mainloop()


def on_submit_pdf(box, pdf_link):
    box.destroy()
    print(f'PDF submetido: {pdf_link}')
    open_new_box(pdf_link)


def insert_pdf_box():
    print('Inserir link do PDF')
    new_box = tk.Tk()
    new_box.title('Dialog box')
    new_box.geometry('600x200')
    center_window(new_box)
    
    tk.Label(new_box, text='Inserir link do PDF:').pack(expand=True, pady=1)
    
    input_field = tk.Entry(new_box, width=80)
    input_field.pack(pady=1)
    
    submit_button = tk.Button(new_box, text='Enviar', command=lambda: on_submit_pdf(new_box, input_field.get()))
    submit_button.pack(pady=30)
    
    new_box.mainloop()
    
    
def register_button(box):
    box.destroy()
    print('Botão cadastrar selecionado')
    insert_pdf_box()


def iterate_reregistration_table(box):
    print('Botão de iterar tabela selecionado')
    box.destroy()
    open_new_box()


def reregistration_table_iterate_box():
    print('Iterar tabela')
    new_box = tk.Tk()
    new_box.title('Dialog box')
    new_box.geometry('300x200')
    center_window(new_box)
    
    tk.Label(new_box).pack(expand=True, pady=1)
    
    button1 = tk.Button(new_box, text='Iterar tabela', command=partial(iterate_reregistration_table, new_box), width=25, height=1)
    button1.pack(pady=1)
    
    tk.Label(new_box).pack(expand=True, pady=1)
    
    new_box.mainloop()
    

def re_register_button(box):
    box.destroy()
    print('Botão recadastrar selecionado')
    reregistration_table_iterate_box()
    

def init_dialog_box():
    print('Caixa de diálogo iniciada')
    box = tk.Tk()
    box.title('Dialog box')
    box.geometry('300x200')
    center_window(box)
    
    tk.Label(box, text='Escolha um dos modos de cadastro abaixo:').pack(expand=True, pady=1)
    
    button1 = tk.Button(box, text='Cadastrar', command=partial(register_button, box), width=25, height=1)
    button1.pack(pady=10)
    
    button2 = tk.Button(box, text='Recadastrar', command=partial(re_register_button, box), width=25, height=1)
    button2.pack(pady=10)
    
    tk.Label(box).pack(expand=True, pady=1)
    
    box.mainloop()
    
    ''

init_dialog_box()