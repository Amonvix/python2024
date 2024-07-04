nome = input("Digite seu nome: ")
idade = input('Digite sua idade: ')
n= len(nome)

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')    
    if ' ' in nome:
        print(f'Existem espaços em {nome}')
    else:
        print(f'Não existem espaços')

    print(f'Seu nome tem {n} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')        
    print(f'A ultima letra do seu nome é {nome[-1]}')        
    
else:
    print(f'DESCULPE, VOCE DEIXOU ALGUM CAMPO VAZIO')
    