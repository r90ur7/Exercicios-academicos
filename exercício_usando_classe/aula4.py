'''
def soma(a=1, b=1):

    return a + b


resultado = soma(2)
print('resultado: ', resultado)


import math

def hipotenusa(a, b):
    h = math.sqrt(a**2 + b**2)
    return h


resultado = hipotenusa(5, 5)
print('resultado: ', resultado)
resultado = hipotenusa(6, 3)
print('resultado: ', resultado)
resultado = hipotenusa(8, 4)
print('resultado: ', resultado)

vendas = [(5, 5), (6, 3), (8, 4), (2, 9), (6, 2)]
for banana, maca in vendas:
    resultado = hipotenusa(banana, maca)
    print('resultado: ', resultado)

lst = [hipotenusa(a, b) for a, b in vendas]
print(lst)

l = []
for x in vendas:
    l.append(x[1]+3)
print(l)

print(math.pi)
'''
'''
Calcule e exiba a área do círculo (A = pi*r2) de qualquer
raio que for digitado.

import math

r = float(input('Entre com um raio: '))
a = math.pi * r**2
print(f'A área do círculo é {a}')
'''
'''
Calcule o volume do cilindro
de raio 6 cm e altura 5 cm (V = pi*r2*h).
'''
import math

r = float(input('Entre com um raio: '))
h = float(input('Entre com a altura: '))
v = math.pi*r**2*h
print(f'O volume do cilindro é {v:.2f}')