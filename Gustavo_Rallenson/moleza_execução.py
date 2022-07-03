from MolezaCrud import MyCrud
my_crud = MyCrud('Moleza.sqlite3')
my_crud.criarmoleza()
resultados = my_crud.selecionar()
Try = 0
try:
    
    while True:
  
        resposta = input(f'o que deseja fazer?\n-----\ninserir:\nalterar:\ndeletar:\nmostar\nsair:\n-----\ncomando:  ')
        if resposta.lower() == 'inserir':
                
                id = int(input('qual id?: ' ))
                nome = input('qual o nome será inserido? ' )
                cpf = int(input("numero: "))
                cpflen = str(cpf)
                
                if len(cpflen) <= 10  and Try <= 2:
            
                    print("insira um cpf valido,tente novamente")
                    Try += 1
                    continue
            
                elif Try >= 3:
            
                    print('limite de tentativas exedido,cpf invalido')
                    my_crud.fecharmoleza()
                    Try = 0
                    break
            
                else:
                    
                    my_crud.inserir(id,nome,cpf)
                    Try = 0
        
        elif resposta.lower() == 'alterar':
    
                id = int(input('qual id?: ' ))
                nome = input('qual o nome será inserido? ' )
                cpf = float(input('informe o cpf: '))
                my_crud.alterar(id,nome, cpf)
                Try = 0
                
        elif resposta.lower() == 'deletar':
            
                id = int(input('qual id?: ' ))
                my_crud.deletar(id)
                Try = 0

        elif resposta.lower() == 'mostrar':
            
            user = input('desejar mostrar todos da tabela?\n-----\nsim,não,sair:\n-----\ncomando:  ')
            if user.lower() == 'sim':
                for resultado in resultados:
                    print(f'{resultado}')
                    print(f'------------')
                    
            elif user.lower() == 'não':

                mostrar = []
                while True:
                    user = (input('digite qual id deseja ver,por favor, digite apenas 1 por vez, digite "finalizar" ao acabar: ' ))
                    if user.lower() == "finalizar":
                        break
                    else:
                        mostrar.append(int(user))

                for index in mostrar:
                        print(f'{resultados[index-1]}')
                        

        elif resposta.lower() == 'sair':

                my_crud.fecharmoleza()
                break

        else:
                
            Try += 1
            if Try <= 2:
                    
                print('não foi possivel entender seu comando,tente novamente')
                continue
            else:
    
                print('não foi possivel entender seu comando,limite de tentativas exedido,tente novamente mais tarde')
                my_crud.fecharmoleza()
                break
            
except:
    print('erro no sistema,fechando a operação...')
    my_crud.fecharmoleza()




    
    
    



