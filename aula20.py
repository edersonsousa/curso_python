primeiro_valor = input('Digite o primeiro valor : ')
segundo_valor = input('Digite o segundo valor : ')



if primeiro_valor > segundo_valor:
    print (
        f'{primeiro_valor=} é maior'
        f' que {segundo_valor=}'
            )
elif segundo_valor > primeiro_valor:
    print (
        f'{segundo_valor=} é maior'
        f' que  {primeiro_valor=}'
        )
else:
    print(f'{primeiro_valor=} e o '
        f'{segundo_valor=} são valores equivalentes....')
