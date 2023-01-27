#Exercício Python 035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas 
#podem ou não formar um triângulo.

ladoA = float(input('Digite o valor do lado A: '))
ladoB = float(input('Digite o valor do lado B: '))
ladoC = float(input('Digite o valor do lado C: '))

if ladoA < ladoB + ladoC and ladoB < ladoA + ladoC and ladoC < ladoA + ladoB:
    print('PODEM FORMAR UM TRIÂNGULO')
else:
    print('NÃO PODEM FORMAR UM TRIÂNGULO')