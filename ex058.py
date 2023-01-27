#Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
tentativas = 1
numero_sorteado = randint(0, 10)

meu_numero = int(input('Digite um número: '))

while meu_numero != numero_sorteado:
    if meu_numero != numero_sorteado:
        tentativas+=1
    if meu_numero > numero_sorteado:
        print('Um número menor')
    else:
        print('Um número maior')
    print(f'Meu número: {meu_numero}')
    meu_numero = int(input('Digite outro número: '))
print(f'Você acertou o número sorteado foi {numero_sorteado}')
print(f'O total de tentativas foi de {tentativas}')