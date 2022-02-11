from tkinter import *

class Conta:

    def __init__(self):
        print("Contruindo objeto... {}".format(self))
        self.__numero = recebe_numero
        self.__titular = recebe_titular
        self.__saldo = recebe_saldo
        self.__limite = recebe_limite
        print("Conta: {} \nTitular: {} \nSaldo: {} \nLimite: {}" .format(self.__numero, self.__titular, self.__saldo, self.__limite))

    def extrato(self):
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_saca(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__limite + self.__saldo
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saca(self, valor):
        if(self.__pode_saca(valor)):
            self.__saldo -= valor
        else:
            print("o valor {} ultrapassou o limite" .format(valor))

    def tranfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {'BB':'001', 'Caixa':'104', 'Bradesco':'237'}



janela = Tk()
janela.title("conta bancaria")

texto_orientacao = Label(janela, text = "Insira o seus dados para acessar sua conta")
texto_orientacao.grid(column=0, row=0)

#numero------
texto_numero = Label(janela, text = "Número")
texto_numero.grid(column=0, row=1)
recebe_numero = Entry(janela)
recebe_numero.grid(column=1, row=1)


#nome-------
texto_nome = Label(janela, text = "Titular")
texto_nome.grid(column=0, row=2)
recebe_titular = Entry(janela)
recebe_titular.grid(column=1, row=2)

#saldo--
texto_saldo = Label(janela, text = "Saldo")
texto_saldo.grid(column=0, row=3)
recebe_saldo = Entry(janela)
recebe_saldo.grid(column=1, row=3)

#limite---
texto_limite = Label(janela, text = "Limite")
texto_limite.grid(column=0, row=4)
recebe_limite = Entry(janela)
recebe_limite.grid(column=1, row=4)

botão = Button(janela, text="Entrar", command=Conta)
botão.grid(column=1, row=5)

janela.mainloop()