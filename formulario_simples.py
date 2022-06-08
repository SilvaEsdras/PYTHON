
from tkinter import Tk, Button, Label, Entry, Listbox
from tkinter import MULTIPLE

window = Tk()
window.title('Title')
window.geometry("500x300")
#window.geometry("500x500+200+200")
#window.maxsize(700,700)
#window.state("zoomed")
#window.state("iconic")
window.iconbitmap('mario.ico')
window['bg'] = 'blue'
window.resizable(True, True)

#elements
btn1 = Button(window, text = "Clique Aqui")
btn1.place(x = 50, y = 50)

lbi1 = Label(window, text = "Seu nome")
lbi1.place(x = 100, y = 100)
ent1 = Entry(window, width = 20)
ent1.place(x = 200, y = 100)

lstbox = Listbox(window, selectmode=MULTIPLE)
lstbox.insert(1,"Python")
lstbox.insert(2,"C")
lstbox.insert(3,"PHP")
lstbox.insert(4,"HTML")
lstbox.place(x = 200, y = 200)

window.mainloop()


