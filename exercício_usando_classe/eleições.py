# Construa um algoritmo de votação para a Prefeitura Municipal de Volta Redonda. Os votos serão
#  computados da seguinte maneira:
eleitores = True
samuca=0
neto=0
baltazar=0
branco=0
nulo=0
maior = samuca
while (eleitores == True):
    voto = int(input("Digite 0 para branco,vote 1 para baltazar, aperte 2 para neto, 3 para samuca, e 4 para anular seu voto"))
    if (voto == 0): 
        branco = branco +1
    elif(voto == 1):
        samuca = samuca + 1
    elif( voto == 2):
        neto = neto +1
    elif (voto == 3):
        baltazar = baltazar +1
    elif ( voto >=4):
        nulo = nulo + 1
    elif voto == -1:
        eleitores = False
        print('Sair da votação')
        break 
    if neto > samuca and neto > baltazar:
       maior = 2
    elif baltazar > samuca and baltazar > neto:
        maior = 3 
    else:
        maior = 1
print('qual candidato venceu:',maior)
print('votos em branco',branco)
print('votos nulo', nulo)
