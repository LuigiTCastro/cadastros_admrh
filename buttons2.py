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
    

def on_submit(link_pdf, box):
    box.destroy()
    run_application(link_pdf)


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
    
    submit_button = tk.Button(new_box, text='Enviar', command=lambda: on_submit(input_field.get(), new_box))
    submit_button.pack(pady=30)
    
    new_box.mainloop()
    

def teste2(box):
    box.destroy()
    print('teste2')


def open_second_box():
    box = tk.Tk()
    box.title('Dialog box')
    box.geometry('300x200')
    center_window(box)
    
    label = tk.Label(box, text='Escolha um dos modos de cadastro abaixo:')
    label.pack(expand=True, pady=1)
    
    button1 = tk.Button(box, text='Inserir PDF', command=partial(open_input_box, box), width=25, height=1)
    button1.pack(pady=10)
    
    button2 = tk.Button(box, text='Iterar Tabela', command=partial(teste2, box), width=25, height=1)
    button2.pack(pady=10)
    
    label = tk.Label(box)
    label.pack(expand=True, pady=1)
    
    box.mainloop()
    

def general_mode_button(box):
    box.destroy()
    print('general_mode_button')
    open_second_box()


def specific_mode_button(box):
    box.destroy()
    print('specific_mode_button')
    
    
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