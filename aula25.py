"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal(ABCDEF01123456789)

"""

nome = 'Luiz'
preco = 1000.95897643
variavel = '%s, o preço é R$ %f' % (nome, preco)

print(variavel)

print('O Hexadecimal de %d é %08X' % (15, 15))