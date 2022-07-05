from Aula9 import  Animais
from Aula9 import  Cachorros
from Aula9 import  Circulos

animais = Animais(cobertura ='pelo')
cachorros = Cachorros(cobertura ='lisa')
#print(animais.nome)
animais.dar_nome("Rex")
print(animais.nome)
#print(help(animais))
#print(help(cachorros))
print('cachorro: ', cachorros.cobertura)
print("vestimenta: ", animais.cobertura,"\n-------")
animais.trocar("crespo")
cachorros.trocar()
print('cachorro: ', cachorros.cobertura)
print("vestimenta: ", animais.cobertura,"\n-------")

circulo = Circulos()

valor = circulo.calcula_Area()
print(circulo.calcula_Area)
#print(valor + 5000)