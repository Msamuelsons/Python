#Exercício Python 028: Escreva um programa que faça
#o computador "pensar" em um número inteiro
#entre 0 e 5 e peça para o usuário tentar descobrir qual foi o 
#escolhido pelo computador. O programa deverá 
#escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

numeroSorteado = randint(0, 5)
meuNumero = int(input('Digite um número inteiro entre 0 e 5: '))

print('PROCESSANDO...')
sleep(3)

if numeroSorteado == meuNumero:
    print('Você venceu !')
    print('Número digitado {}'.format(meuNumero))
    print('Número premiado {}'.format(numeroSorteado))
else:
    print('Você perdeu !')
    print('Número digitado {}'.format(meuNumero))
    print('Número premiado {}'.format(numeroSorteado))

