from Pessoa import Pessoa
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