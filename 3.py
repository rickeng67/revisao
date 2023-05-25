"""
Faça um programa para o cálculo de uma folha de pagamento, sabendo
que os descontos são do imposto de renda, que depende do 
salário bruto(Conforme tabela abaixo) e 3% para o sindicato e que o
FGTS corresponde a 11% do Salário Bruto, mas não é descontado(é 
a empresa que deposita). O programa deverá pedir ao usuário o valor da sua
hora e a quantidade de horas trabalhadas no mês.

Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5% 
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% imprima na tela
as informações , dispostas confore o exemplo abaixo. No exemplo o
valor da hora é 5 e a quantidade de hora é 220

Salário Bruto:( 5 * 220) : R$ 1100,00
(-)IR (5%)  : r$ 55,00
(-)INSS(10%)  110,00
FGTS (11%)   : R$ 121,00
Total de descontos R$ 165,00
Salário Líquido : R$ 935,00 """
h=int(input("Inserir a quantidade de horas trabalhadas"))
valor=float(input("Inserir o Valor da hora aula"))
salariob= h * valor
fgts= salariob * 0.11
inss= salariob * 0.10
sind= salariob * 0.03
if salariob <=900:
    totaldesc = sind + inss
    salarioliq = salariob - totaldesc 
    print(f"Com o salario de {salariob},Seu desconto total será de:{totaldesc},Seu salário liquido será : {salarioliq}")

elif salariob <=1500:
    ir = salariob * 0.05
    totaldesc = sind + inss + ir
    salarioliq = salariob - totaldesc  
    print(f"Com o salario de {salariob},Seu desconto total será de:{totaldesc},Seu salário liquido será : {salarioliq}")

elif salariob <=2500:
    ir = salariob * 0.1
    totaldesc = sind + inss + ir
    salarioliq = salariob - totaldesc  
    print(f"Com o salario de {salariob},Seu desconto total será de:{totaldesc},Seu salário liquido será : {salarioliq}")
else :
    ir = salariob * 0.2
    totaldesc = sind + inss + ir
    salarioliq = salariob - totaldesc  
    print(f"Com o salario de {salariob},Seu desconto total será de:{totaldesc},Seu salário liquido será : {salarioliq}")    



