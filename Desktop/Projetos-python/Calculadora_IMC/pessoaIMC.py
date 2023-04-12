# Classe Pessoa
class Pessoa:
    def __init__(self, nome, nascimento, peso, altura, imc=False):
        self.nome = nome
        self.nascimento = nascimento
        self.peso = peso
        self.altura = altura
        self.imc = imc

    def calculoImc(self, peso, altura):
        situacao = float(peso / (altura ** 2))
        self.imc = situacao
        return situacao

    def resultImc(self):
        if 16.00 <= self.imc < 16.99:
            print(f" Situação: 16,00 a 16,99 - Baixo peso Grau II")
        elif 17.00 <= self.imc < 18.49:
            print(f" Situação: 17,00 a 18,49 - Baixo peso Grau I")
        elif 18.50 <= self.imc < 24.99:
            print(f" Situação: 18,50 a 24,99 - Peso ideal")
        elif 25.00 <= self.imc < 29.99:
            print(f" Situação: 25,00 a 29,99 - Sobrepeso")
        elif 30.00 <= self.imc < 35.99:
            print(f" Situação: 30,00 a 35,99 - Obesidade Grau I")
        elif 35.00 <= self.imc < 39.99:
            print(f" Situação: 35,00 a 39,99 - Obesidade Grau II")
        else:
            print(
                f" Situação:{self.nome} seu IMC ultapassam a faixa - Obesidade Grau II, procure urgentemente um médico!")

    # def __repr__(self):
    #  return str(self.imc)
