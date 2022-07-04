'''
1. Classe Bola: Crie uma classe que modele uma bola:
a. Atributos: Cor, circunferência, material
b. Métodos: trocaCor e mostraCor

class Bola:

    def __init__(self, cor=None, circunferencia=None, material=None):
        self.Cor = cor
        self.Circuferencia = circunferencia
        self.Material = material

    def trocaCor(self, novaCor):
        self.Cor = novaCor

    def mostraCor(self):
        return self.Cor


bola = Bola('azul', 12, 'plastico')
print(bola.Cor, bola.Material, bola.Circuferencia, )
bola.trocaCor('verde')
print(bola.Cor, bola.Material, bola.Circuferencia, )
print(bola.mostraCor())
'''

'''
2. Classe Quadrado: Crie uma classe que modele um quadrado:
a. Atributos: Tamanho do lado
b. Métodos: Mudar valor do Lado, retornar valor do Lado e calcular Área;

class Quadrado:

    def __init__(self, tamanho_lado=0.0):
        self.tamanho_lado = tamanho_lado

    def mudar_valor_lado(self, valor_lado):
        self.tamanho_lado = float(valor_lado)

    def retornar_valor_lado(self):
        return self.tamanho_lado

    def calcular_area(self):
        area = self.tamanho_lado**2
        return area


quadrado = Quadrado()
print(quadrado.retornar_valor_lado())
print(quadrado.calcular_area())
quadrado.mudar_valor_lado(5)
print(quadrado.retornar_valor_lado())
print(quadrado.calcular_area())
'''

'''
3. Classe Retangulo: Crie uma classe que modele um retângulo:
a. Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
b. Métodos: Mudar valor dos lados, retornar valor dos lados, calcular Área e calcular Perímetro;
c. Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidas de
  um local. Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de
  rodapés necessárias para o local.

class Retangulo:

    def __init__(self, comprimento=0, largura=0):
        self.Comprimento = comprimento
        self.Largura = largura

    def ChangeValues(self, comprimento, largura):
        self.Comprimento = comprimento
        self.Largura = largura

    def GetValues(self):
        resultList = []
        resultList.append(self.Comprimento)
        resultList.append(self.Largura)
        return resultList

    def CalcArea(self):
        return float(self.Comprimento * self.Largura)

    def CalcPerimetro(self):
        return float(2 * (self.Comprimento + self.Largura))

    def calcular_quantidade_piso(self):
        ###


retangulo = Retangulo()
print(retangulo.GetValues())
print(retangulo.CalcArea())
print(retangulo.CalcPerimetro())
retangulo.ChangeValues(5, 5)
print(retangulo.GetValues())
print(retangulo.CalcArea())
print(retangulo.CalcPerimetro())
'''
'''
4. Classe Pessoa: Crie uma classe que modele uma pessoa:
a. Atributos: nome, idade, peso e altura
b. Métodos: envelhecer, engordar, emagrecer, crescer. Obs: Por padrão,
a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos,
ela deve crescer 0,5 cm.
'''


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


'''
pessoa = Pessoa('andre', 19, 125, 180)
print(pessoa.nome, pessoa.idade, pessoa.peso, pessoa.altura)
pessoa.emagrecer()
print(pessoa.crescer())

print(pessoa.nome, pessoa.idade, pessoa.peso, pessoa.altura)
pessoa.engordar()
pessoa.envelhecer()
print(pessoa.nome, pessoa.idade, pessoa.peso, pessoa.altura)
pessoa.envelhecer()
print(pessoa.nome, pessoa.idade, pessoa.peso, pessoa.altura)
pessoa.envelhecer()
print(pessoa.nome, pessoa.idade, pessoa.peso, pessoa.altura)
'''
'''
pessoa = Pessoa('andre', 19, 125, 180)
lst = [pessoa.nome, pessoa.idade, pessoa.peso, pessoa.altura]

titulo = ['nome;', 'idade;', 'peso;', 'altura\n']
l = []
for i in lst:
    l.append(f'{i};')
arquivo = open('aula11.txt', 'w')
arquivo.writelines(titulo)
arquivo.writelines(l)
arquivo.close()
'''
# --------------------------------
arquivo = open('aula11.txt', 'r')
print(arquivo.readline())
results = arquivo.readlines()
arquivo.close()


print(results)
resultados = []
for i in results:
    print(i.replace('\n', ''), len(i.replace('\n', '').strip()))
    linha = i.replace('\n', '').strip().split(';')
    resultados.append(linha[:-1])


print(resultados)
for j in resultados:
    print(j[1:])
