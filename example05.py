n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))

m = (n1 + n2) / 2
print('Sua média foi {:.1f}'.format(m))

if (m >= 6):
    print('Você passou, pois sua média foi {:.1f}'.format(m))
else:
    print('Você está de recuperação, pois sua média foi {:.1f}'.format(m))