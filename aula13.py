nome = 'Ed '
altura = 1.77
peso = 67
imc = peso / (altura*altura) # IMC = peso / (altura x altura)? 
linha_1 = f'{nome}, tem {altura:.2f} de altura... '
linha_2 = f'pesa  {peso:.2f} , quilos e seu IMC é '
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)