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