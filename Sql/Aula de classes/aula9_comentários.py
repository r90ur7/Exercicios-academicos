# class Animal:

#     def __init__(self, nome=None, cobertura=None):
#         self.nome = nome
#         self.cobertura = cobertura

#     def dar_nome(self, nome):
#         self.nome = nome


# class Cachorros(Animal):
#     def trocar(self):
#         self.cobertura = 'crespo'


# animais = Animal(cobertura='pelada')
# cachorros = Cachorros(cobertura='lisa')
# print(animais.nome)
# animais.dar_nome("Rex")
# print(animais.nome)
# # print(help(animais))
# # print(help(cachorros))
# print('cachorro: ', cachorros.cobertura)
# print("animal: ", animais.cobertura)
# print(cachorros.trocar())
# print('cachorro: ', cachorros.cobertura)
# print("animal: ", animais.cobertura)

# class Circulos:
#     raio = 25.4

#     def calcula_Area(self):
#         return 3.14*(self.raio**2)

#     def calcula_Volume(self, altura):
#         return 3.14*(self.raio**2)*altura


# circulo = Circulos()

# valor = circulo.calcula_Area()
# print(valor + 5000)

# registro = []
# while True:
#     nome = input("Entre com seu nome: ")
#     if nome.upper() == "SAIR":
#         break
#     registro.append(nome)

# print(registro)
