# Faça um algoritmo que leia o preço de um produto e mostre o seu
# novo preço, com 5% de desconto.

produto = float(input('Qual preço do produto? '))
print('O preço aplicado 5% de desconto {:.2f}'.format(produto - (produto * 0.05)))