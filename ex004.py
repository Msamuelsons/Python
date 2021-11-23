# -*- coding: utf-8 -*-
# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo
# Primitivo e todas as informações possíveis sobre ela.

x = input("Digite algo: ")
print('O tipo primitivo desse valor é: {}'.format(type(x)))
print('Só tem espaçamentos? {}'.format(x.isspace()))
print('É um número? {}'.format(x.isnumeric()))
print('É alfabético? {}'.format(x.isalpha()))
print('É alfanumérico? {}'.format(x.isalnum()))
print('Está em maiúsculas? {}'.format(x.isupper()))
print('Está em minúsculas? {}'.format(x.islower()))
print('Está capitalizada? {}'.format(x.istitle()))