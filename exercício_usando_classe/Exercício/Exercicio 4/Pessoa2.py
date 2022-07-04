from Pessoa import Pessoa
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