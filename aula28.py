"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""
nome = input('Digite seu nome: ')
idade = input('Digite a sua idade: ')
espaco = " "

if (nome and idade):

    print('Seu nome é : %s' % (nome))
    print('Sua idade é : %s' % (idade))
    if espaco in nome:
        print("Teu nome contém espaço!")
    else:
        print("Não... Seu nome não contem espaço")


    print("Seu nome tem ",len(nome), " letras...")
    print("A primeira letra de seu nome é :", nome[0])
    print("A última letra de seu nome é :", nome[-1])

    print("Teu nome invertido é .... ",nome[::-1])

else:
    print("Desculpe você deixou campos vaziosssss....")