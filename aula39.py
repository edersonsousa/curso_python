"""
    Iterando strings com o while


"""
import time
nome = 'Ederson Sousa' # Iteráveis

tamanho = len(nome)
i = 0

while i <= tamanho:
    time.sleep(1)  # import time
    print(nome[i])
    i += 1

