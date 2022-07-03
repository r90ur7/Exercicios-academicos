from mycrud import MyCrud

my_crud = MyCrud('moleza.sqlite3')
my_crud.criar_moleza()
resultados = my_crud.selecao()
Try = 0

try:

    while True:

        resposta = input(f'O que deseja fazer?\ninserir \nalterar \ndeletar \nmostrar  \nsair \nEscreva aqui uma das opções acima: ')
    
        if resposta.lower() == 'inserir':

            id = int(input('ID: '))
            nome = input('Nome: ')
            cpf = int(input('CPF: '))
            lercpf = str(cpf)
    
            if len(lercpf) <= 10 and Try <= 2:
            
                print("O número do CPF está incorreto, insira novamente")
                Try += 1
                continue

            elif Try >= 3:
                print('Suas tentativas se esgotaram')
                my_crud.fechar_moleza()
                Try = 0
                break

            else: 
                my_crud.colocar(id,nome,cpf)
                Try = 0
    
        elif resposta.lower() == 'alterar':
            id = int(input('Prontos para Alterar\n ID: '))
            nome = input('Nome: ')
            cpf = float(input('CPF: '))
            my_crud.mudar(id,nome,cpf)
            Try = 0
    
        elif resposta.lower() == 'mostrar':

            amostra = input('Mostrar Tabela! Digite: Sim, não ou sair: ')
            if amostra.lower() == 'sim':
                for resultado in resultados:
                    print(f'{resultado}')

            elif amostra.lower() == 'mostrar':
                mostrar = []
                while True:
                    amostra = input('ID na qual deseja verificar: ')
                    if amostra.lower == "finalizar":
                            break
                    else:
                        mostrar.append(int(amostra))
            
                for i in mostrar:
                    print(f'{resultados[i-1]}')
        
        elif resposta.lower() == 'deletar':
            id = int(input('Prontos para excluir\nID: '))
            nome = input('Nome: ')
            cpf = float(input('CPF: '))
            my_crud.excluir(id)
            Try = 0
    
        elif resposta.lower() == 'sair':
            my_crud.fechar_moleza()
            break

        else:

            Try += 1
            if Try <= 2:
                print('Impossível compreender o que foi digitado!')
                continue

            else:
                print('Suas tentativas se esgotaram')
                my_crud.fechar_moleza()
                break

except:
    print('SISTEMA PAROU POR ERRO, DESLIGANDO!')
    my_crud.fechar_moleza()


