"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

n = input('Digite um número inteiro! : ')

try:
    n_int = int(n)
    if n_int % 2:
        print('Temos um inteiro ímpar aqui !')
    else:
        print('Temos um inteiro par aqui !')
except:
    print('Ei!!  Era pra digitar um número inteiro!')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

h = input('Que horas são ?')
h_int = int(h)
if h_int <= 11 and h_int >= 0:
    print("Bom dia ! ")
elif (h_int>=12 and h_int<=17):
    print("Boa Tarde ! ")
elif (18<=h_int<=23):
    print('Boa Noite ! ')


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input(' Digite seu nome : ')

if len(nome)<=4:
    print('Seu nome é curto...')
elif 5<=len(nome)<=6:
    print("Ok... Você tem um nome normal.")
elif len(nome)>6:
    print('Que nome enorme hein...')