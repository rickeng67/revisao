"""
Faça um programa que leia três numeros inteiros e mostre o maior deles
"""
n1=int(input("Digite o primeiro número"))
n2=int(input("Digite o segundo número"))
n3=int(input("Digite o terceiro número"))
if n1 > n2 and n1>n3:
    print(f"{n1} é o maior")
elif n2> n1 and n2>n3:
    print(f"{n2} é o maior")
else:
    print(f"{n3} é o maior")        
