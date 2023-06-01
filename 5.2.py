def parimpar(numero):
    x = numero % 2 == 0
    print(x)

    if x:
        return f'{numero} é par'
    return f'{numero} é impar'
print(parimpar(7))
