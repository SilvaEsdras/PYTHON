
import tkinter as tk


def criarnovajanela():
    novajanela = tk.Toplevel(app)

app = tk.Tk()
botao = tk.Button(app, text = "Criar janela", command = criarnovajanela)
#app.state("zoomed")
app.geometry('500x600')
botao.pack()

app.mainloop()


