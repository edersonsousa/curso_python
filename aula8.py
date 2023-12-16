nome = 'Ed'
sobrenome = 'Rocha'
idade = 41
altura = 1.77
ano_nascimento = 2023 - idade
maior_de_idade = idade >= 18


print('Nome: ', nome, sobrenome)
#print('Nome: ', sobrenome)
print('Idade: ', idade, ' anos.')

print('Ano de nascimento: ', ano_nascimento)
print('Maior de idade:  ', end=' ' )
if maior_de_idade:
    print('Sim!')
else:
    print('Não')

print('Altura em metros: ', altura)