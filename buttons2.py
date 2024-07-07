import tkinter as tk
from functools import partial
from contractual_data import get_links
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
    

def on_submit1(link_pdf, box):
    box.destroy()
    run_application(link_pdf)   

    
def on_submit2(link_tabela, link_diretorio, box):
    box.destroy()
    get_links(link_tabela, link_diretorio)
    open_second_box()


def open_input_box(box):
    box.destroy()
    new_box = tk.Tk()
    new_box.title('Dialog box')
    new_box.geometry('600x200')
    center_window(new_box)
    
    label = tk.Label(new_box, text='Inserir link do PDF:')
    label.pack(expand=True, pady=1)
    
    input_field = tk.Entry(new_box, width=80)
    input_field.pack(pady=1)
    
    submit_button = tk.Button(new_box, text='Enviar', command=lambda: on_submit1(input_field.get(), new_box))
    submit_button.pack(pady=30)
    
    new_box.mainloop()
    

# DESENVOLVER
def iterate_table(box):
    box.destroy()
    print('iterate_table')


def open_second_box():
    box = tk.Tk()
    box.title('Dialog box')
    box.geometry('300x200')
    center_window(box)
    
    label = tk.Label(box, text='Escolha um dos modos de cadastro abaixo:')
    label.pack(expand=True, pady=1)
    
    button1 = tk.Button(box, text='Inserir PDF', command=partial(open_input_box, box), width=25, height=1)
    button1.pack(pady=10)
    
    button2 = tk.Button(box, text='Iterar Tabela', command=partial(iterate_table, box), width=25, height=1)
    button2.pack(pady=10)
    
    label = tk.Label(box)
    label.pack(expand=True, pady=1)
    
    box.mainloop()
    

def general_mode_button(box):
    box.destroy()
    print('general_mode_button')
    open_second_box()


def open_new_box():
    box = tk.Tk()
    box.title('Dialog box')
    box.geometry('600x250')
    center_window(box)    
    
    tk.Label(box).pack(expand=True, pady=1)
    
    label = tk.Label(box, text='Alterar link da tabela')
    label.pack(expand=True, pady=5)
    input_field1 = tk.Entry(box, width=80)
    input_field1.pack(pady=5)
    
    tk.Label(box).pack(expand=True, pady=1)
    
    label = tk.Label(box, text='Alterar link do diretório de PDFs')
    label.pack(expand=True, pady=5)
    input_field2 = tk.Entry(box, width=80)
    input_field2.pack(pady=5)
    
    tk.Label(box).pack(expand=True, pady=1)
    
    submit_button = tk.Button(box, text='Enviar', command=lambda: on_submit2(input_field1.get(), input_field2.get(), box))
    submit_button.pack(expand=True, pady=10)
    
    tk.Label(box).pack(expand=True, pady=1)
    
    box.mainloop()


def specific_mode_button(box):
    box.destroy()
    print('specific_mode_button')
    open_new_box()
    
    
def initialize_dialog_box():
    box = tk.Tk()
    box.title('Dialog box')
    box.geometry('300x200')
    center_window(box)
    
    label = tk.Label(box, text='Escolha um dos modos de cadastro abaixo:')
    label.pack(expand=True, pady=1)
    
    button1 = tk.Button(box, text='Modo Geral', command=partial(general_mode_button, box), width=25, height=1)
    button1.pack(pady=10)

    button2 = tk.Button(box, text='Modo Específico', command=partial(specific_mode_button, box), width=25, height=1)
    button2.pack(pady=10)
    
    label = tk.Label(box)
    label.pack(expand=True, pady=1)

    box.mainloop()
    
    

initialize_dialog_box()