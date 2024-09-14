import tkinter as tk
from tkinter import *



root = tk.Tk()
root.title("")
root.geometry("350x200")
root.resizable(False, False)

# Criando um botão para abrir o PDF
label= Label(root, text='CALC IMC', font='Arial 20 bold', fg='#236e14')
label.place(x=5, y=5)
Entry = Entry(root, width='50', relief='sunken', border='3')
Entry.place(x=5, y=50)


# Iniciando o loop principal do Tkinter
root.mainloop()