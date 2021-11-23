# -*- coding: utf-8 -*-
# nome = input('Digite seu nome: ')
# print('Prazer em te conhercer {:=^20}'.format(nome))

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
su = n1 - n2
p = pow(n1, n2)
print('A soma é {},\n o produto é {} e a divisão é {:.3f}'.format(s, m, d), end='')
print('A divisão inteira {} e potência {}'.format(di, p), end=' ')
print('A subtração vale {}'.format(su))