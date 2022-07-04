from Bola import Bola

bola = Bola('azul', 12, 'plastico')
print(bola.Cor, bola.Material, bola.Circuferencia, )
bola.trocaCor('verde')
print(bola.Cor, bola.Material, bola.Circuferencia, )
print(bola.mostraCor())