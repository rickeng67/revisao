
#x,y, *resto = 1, 2, 3, 4
#print(x, y, resto)


def soma(*args):
    total = 1
    for numero in args:
        total*= numero
        #total = total + numero
    return total

soma_1_2_3_4 = soma(1, 2, 3, 4)
print(soma_1_2_3_4)

soma_4_5_6 = soma (4, 5, 6)
print(soma_4_5_6)

numeros = 1, 2, 5, 10, 20, 25



