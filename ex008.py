# -*- coding: utf-8 -*-
#Escreva um programa que leia em metros e o exiba em
#centímetros e milímetros

metros = float(input('Digite o tamanho em metros: '))

print('A medida em centímetros é {} \n em milímetros {}' .format((metros / 100), (metros / 1000)))