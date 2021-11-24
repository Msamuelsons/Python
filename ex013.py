# Faça um algoritmo que leia o salario de um funcionário e
# mostre seu novo salário, com 15% de aumento.

salario = float(input('Digite seu salário: '))
print('Seu novo salário com 15% de aumento é {:.2f}'.format(salario + (salario * 0.15)))