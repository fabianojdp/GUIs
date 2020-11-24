from tkinter import Tk, Label, PhotoImage

root = Tk()
photo = PhotoImage(file='COM120_Aula18_02_logo.gif')
hello = Label(master = root, image=photo, width=480, height=480)
# hello = Label(master = root, text = 'Olá, veja a tela')
hello.pack()
root.mainloop()
