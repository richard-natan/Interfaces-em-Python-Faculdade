import tkinter as tk
import tkinter.font as tkFont

from unicodedata import name


class App:
    def __init__(self, root):
        #setando titulo
        root.title("Cálculo IMC - Índice de Massa Corporal")
        #setando tamanho da tela
        width=456
        height=241
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        nomeLabel=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        nomeLabel["font"] = ft
        nomeLabel["fg"] = "#333333"
        nomeLabel["justify"] = "left"
        nomeLabel["text"] = "Nome do Paciente: "
        nomeLabel.place(x=20,y=20,width=124,height=30)

        enderecoLabel=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        enderecoLabel["font"] = ft
        enderecoLabel["fg"] = "#333333"
        enderecoLabel["justify"] = "left"
        enderecoLabel["text"] = "Endereço Completo: "
        enderecoLabel.place(x=20,y=50,width=127,height=30)

        alturaLabel=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        alturaLabel["font"] = ft
        alturaLabel["fg"] = "#333333"
        alturaLabel["justify"] = "left"
        alturaLabel["text"] = "  Altura (cm)"
        alturaLabel.place(x=20,y=80,width=70,height=25)

        pesoLabel=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        pesoLabel["font"] = ft
        pesoLabel["fg"] = "#333333"
        pesoLabel["justify"] = "left"
        pesoLabel["text"] = "Peso (kg)"
        pesoLabel.place(x=20,y=110,width=70,height=25)

        nameInput=tk.Entry(root)
        nameInput["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        nameInput["font"] = ft
        nameInput["fg"] = "#333333"
        nameInput["justify"] = "center"
        nameInput["text"] = ""
        nameInput["relief"] = "solid"
        nameInput.place(x=140,y=20,width=301,height=30)

        enderecoInput=tk.Entry(root)
        enderecoInput["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        enderecoInput["font"] = ft
        enderecoInput["fg"] = "#333333"
        enderecoInput["justify"] = "center"
        enderecoInput["text"] = ""
        enderecoInput["relief"] = "solid"
        enderecoInput.place(x=140,y=50,width=301,height=30)

        alturaInput=tk.Entry(root)
        alturaInput["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        alturaInput["font"] = ft
        alturaInput["fg"] = "#333333"
        alturaInput["justify"] = "center"
        alturaInput["text"] = ""
        alturaInput["relief"] = "solid"
        alturaInput.place(x=140,y=80,width=133,height=30)

        pesoInput=tk.Entry(root)
        pesoInput["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        pesoInput["font"] = ft
        pesoInput["fg"] = "#333333"
        pesoInput["justify"] = "center"
        pesoInput["text"] = ""
        pesoInput["relief"] = "solid"
        pesoInput.place(x=140,y=110,width=133,height=30)

        resultado=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        resultado["font"] = ft
        resultado["fg"] = "#333333"
        resultado["justify"] = "left"
        resultado["text"] = "Resultado"
        resultado["padx"] = "0"
        resultado["relief"] = "solid"
        resultado.place(x=270,y=80,width=173,height=115)

        def calcButton_command():
            altura = float(alturaInput.get())
            peso = float(pesoInput.get()) * 1000
            imc = peso / (altura * altura) * 10

            if(imc < 17):
                resultado["text"] = "Muito abaixo do peso"

            if(imc > 17 and imc < 18):
                resultado["text"] = "Abaixo do peso"

            if(imc > 19 and imc < 24):
                resultado["text"] = "Peso normal"

            if (imc > 25 and imc < 30):
                resultado["text"] = "Acima do peso"

            if (imc > 30 and imc < 35):
                resultado["text"] = "Obesidade I"

            if (imc > 35 and imc < 40):
                resultado["text"] = "Obesidade II"

            if (imc > 40):
                resultado["text"] = "Obesidade III"

        calcButton=tk.Button(root)
        calcButton["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        calcButton["font"] = ft
        calcButton["fg"] = "#000000"
        calcButton["justify"] = "center"
        calcButton["text"] = "Calcular"
        calcButton.place(x=110,y=200,width=86,height=30)
        calcButton["command"] = calcButton_command

        def reiniciarButton_command():
            nameInput.delete(0, 999)
            enderecoInput.delete(0, 999)
            alturaInput.delete(0, 999)
            pesoInput.delete(0, 999)

        reiniciarButton=tk.Button(root)
        reiniciarButton["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        reiniciarButton["font"] = ft
        reiniciarButton["fg"] = "#000000"
        reiniciarButton["justify"] = "center"
        reiniciarButton["text"] = "Reiniciar"
        reiniciarButton.place(x=200,y=200,width=88,height=30)
        reiniciarButton["command"] = reiniciarButton_command

        sairButton=tk.Button(root)
        sairButton["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        sairButton["font"] = ft
        sairButton["fg"] = "#000000"
        sairButton["justify"] = "center"
        sairButton["text"] = "Sair"
        sairButton.place(x=350,y=200,width=90,height=30)
        sairButton["command"] = self.sairButton_command

    def sairButton_command(self):
        root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
