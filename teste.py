from tkinter import *
from tkinter import ttk
from tipo import classificar   # importa a função

def enviar():
    descricao = entrada.get()
    classe, confianca = classificar(descricao)

    label_tipo.config(text=f"{classe} {int(confianca)} %")

def enviarCorreto():
    descricao = entrada.get()
    label_correto = labelCorreto.get()

    with open("duvidas_erros.csv", "a", encoding="utf-8") as f:
        f.write(f"\n{descricao};{label_correto}")

    labelCorreto.delete(0, END)


root = Tk()
root.title("Classificação de Descrição")

frm = ttk.Frame(root, padding=10)
frm.grid()

ttk.Label(frm, text="Digite sua descrição").grid(column=0, row=0, columnspan=2)

entrada = ttk.Entry(frm, width=50)
entrada.grid(column=0, row=1, columnspan=2)
entrada.focus()

ttk.Button(frm, text="Enviar", command=enviar).grid(column=1, row=1)

entrada.bind("<Return>", lambda event: enviar())

ttk.Label(frm, text="Tipo que sua descrição se encaixa:").grid(column=0, row=3)

label_tipo = ttk.Label(frm, text="")
label_tipo.grid(column=1, row=3)

ttk.Label(frm, text="").grid(column=0, row=4)
ttk.Label(frm, text="Digite o label correto").grid(column=0, row=5, columnspan=2)

labelCorreto = ttk.Entry(frm, width=50)
labelCorreto.grid(column=0, row=6)

ttk.Button(frm, text="Enviar Certo", command=enviarCorreto).grid(column=1, row=6)

root.mainloop()