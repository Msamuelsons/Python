'''
Exercício Python 029: Escreva um programa que leia a velocidade de
um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo 
que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.
'''

from time import sleep

km = int(input('Você estava a quantos KM/h ? '))

print('Seu carro passou no radar 🚗...')
sleep(3)

if km > 80:
    print('Você será multado em R$ {:.2f}'.format((km - 80) * 7.0))
else:
    print('Vá em paz, dirija com segurança')