from tkinter import Tk, Label, PhotoImage, TOP, BOTTOM

root = Tk()
#photo = PhotoImage(file='COM120_Aula18_03_logo.gif')
photo = PhotoImage(file='COM120_Aula18_03_logo.gif').subsample(2)
#image = Label(master = root, image=photo, width=480, height=480)
image = Label(master = root, image=photo)
image.pack(side=TOP)
text = Label(master = root, font=("Courier", 18), text = 'Olá aluno da Univesp!')
text.pack(side=BOTTOM)
root.mainloop()
