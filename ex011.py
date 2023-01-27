# Pense em um programa que leia a largura e a altura de uma
# parede em metros, calcule sua área e a quantidade de
# tinta necessária parapinta-la, sabendo que cada
# litro de tinta, pinta uma área de 2m²

w = float(input('Digite o valor da largura: '))
h = float(input('Digite o valor da altura: '))

area = w * h
print('A quantidade de tinta necessária: {}'.format(area / 2))
