"""
    Iterando strings com o while


"""
nome = 'Ederson Sousa' # Iteráveis

tamanho = len(nome)
i = 0

while i < tamanho:
    print(nome[i])
    i += 1
print('|')
nome2 = 'Ederson Sousa'  # Iteráveis

indice = 0
novo_nome = ''
while indice < len(nome2):
    letra = nome2[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += '*'
print(novo_nome)