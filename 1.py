"""
Faça um programa que pede duas notas de um aluno. Em seguida
ele deve calcular a média do aluno e dar o resultado
-Aprovado - se a média for maior ou igual a 7
-Reprovado se a média for menor do que 4
e em recuperação para média menor do que 7 e maior ou igual 4
"""
n1= float(input("Digite a primeira nota"))
n2= float(input("Digite a segunda nota"))
media = (n1 + n2)/2
if media >=7:
    print("Aprovado!!!")
elif media <4:
    print("Reprovado!!!")
else:
    print("Recuperação!!!")




