numero = int(input('Digite o número: '))

unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10

print('A unidade: {}'.format(unidade))
print('A dezena: {}'.format(dezena))
print('A centena: {}'.format(centena))
print('O milhar: {}'.format(milhar))