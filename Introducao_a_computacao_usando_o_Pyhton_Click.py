from tkinter import Tk, Button
from time import strftime, localtime

def clicked():
    'exibe informação de dia e hora'
    hora = strftime('Dia: %d %b %Y\nHora: %H:%M:%S %p\n',
                     localtime())
    print(hora)

raiz = Tk()

# cria botão rotulado com ‘Clique aqui’ e manipulador de evento clicked()
button = Button(raiz,
                text='Clique aqui',     # texto do botão
                command=clicked)     # manipulador do evento clique do botão
button.pack()                          
raiz.mainloop()
