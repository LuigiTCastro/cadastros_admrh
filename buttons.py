import fitz
import tkinter as tk
from functools import partial

from personal_data import get_pdf_document, get_personals_data
from system_fields import create_driver, handle_website


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


def on_button_click1(box):
    box.destroy()
    new_box = tk.Tk()
    new_box.title('Dialog box')
    new_box.geometry('300x200')
    center_window(new_box)
    
    tk.Label(new_box).pack(expand=True, pady=4)
    
    label = tk.Label(new_box, text='Inserir link do PDF:')
    label.pack(expand=True, pady=4)
    link_pdf = tk.Entry(new_box, width=40)
    link_pdf.pack(pady=4)
    
    submit_button = tk.Button(new_box, text='Enviar', command=lambda: on_submit(link_pdf, new_box))
    submit_button.pack(pady=10)
    
    tk.Label(new_box).pack(expand=True, pady=4)
    
    new_box.mainloop()


def on_button_click2(box):
    box.destroy()
    open_second_box()
        

def teste1():
    pass

def teste2():
    pass


def open_second_box():
    second_box = tk.Tk()
    second_box.title('Dialog box')
    second_box.geometry('300x200')
    center_window(second_box)
    
    label = tk.Label(second_box, text='Escolha uma das opções abaixo:')
    label.pack(expand=True, pady=1)
    
    button1 = tk.Button(second_box, text='Tabela modelo padrão', command=partial(teste1, second_box), width=25, height=1)
    button1.pack(pady=10)

    button2 = tk.Button(second_box, text='Tabela alternativa', command=partial(teste2, second_box), width=25, height=1)
    button2.pack(pady=10)

    label = tk.Label(second_box)
    label.pack(expand=True, pady=1)

    second_box.mainloop()

    
# PEGAR O LINK INSERIDO
def get_link_pdf(link_pdf, box):
    link_pdf = link_pdf.get()
    print(link_pdf)
    if "\\" in link_pdf:
        link_pdf = link_pdf.replace("\\", "/").strip('\'"')
    box.destroy()
    return link_pdf


def show_box():
    box = tk.Tk()
    box.title('Dialog box')
    box.geometry('300x200')
    center_window(box)
    # box.withdraw()
    # box.config(padx=10, pady=1)

    label = tk.Label(box, text='Escolha uma das opções abaixo:')
    label.pack(expand=True, pady=1)
    
    button1 = tk.Button(box, text='Ler PDF', command=partial(on_button_click1, box), width=25, height=1)
    button1.pack(pady=10)

    button2 = tk.Button(box, text='Iterar tabela', command=partial(on_button_click2, box), width=25, height=1)
    button2.pack(pady=10)

    label = tk.Label(box)
    label.pack(expand=True, pady=1)

    box.mainloop()
    
    
def on_submit(link_pdf, box):
    pdf_document = get_link_pdf(link_pdf, box)
    if pdf_document is not None:
        print(pdf_document)
        result_text = get_pdf_document(pdf_document)
        if result_text:
            personals_data = get_personals_data(result_text)
        # driver = create_driver()
        # handle_website(driver)
    
    return personals_data


   
show_box()