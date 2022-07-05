matriz = [["1",1,2],["1",3,4],["1",5,6],["1",9]]
linha = len(matriz)
#   0          0 - 4
for l in range(linha):
  #passada : 1
  # matriz[0] = [1,2]
  print(matriz[l])
  #passada : 1
  #coluna = 2
  coluna = len(matriz[l])
  soma = 0
  # passada : 1 , coluna = 2
  for c in range(coluna):
    if matriz[0][0] != 0:
      nome = matriz[0][0]
      matriz[0][0] = 0
  else:
    # 0   =  0   +  matriz[0][2]
     soma = soma + matriz[l][c]
  print(nome,matriz[l][c])