#Exercício Python 057: Faça um programa que leia o sexo de
# uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação
#novamente até ter um valor correto.

sexo = str(input('Informe seu sexo: ')).strip().upper()[0]

while sexo not in 'MmFf':
    print('Digite novamente')
    sexo = str(input('Informe seu sexo: ')).strip().upper()[0]
print(f'Seu sexo é {sexo}')