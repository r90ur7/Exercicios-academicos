class Pessoa:
    def __init__(self, nome=None, idade=0, peso=0, altura=0):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        self.idade += 1
        self.crescer()
        return self.idade

    def engordar(self):
        self.peso += 1

    def emagrecer(self):
        self.peso -= 1

    def crescer(self):
        if self.idade < 21:
            self.altura += 0.5
        return self.altura