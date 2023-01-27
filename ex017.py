import math

b = float(input('Qual o valor do cateto oposto ? '))
c = float(input('Qual o valor do cateto adjacente ? '))

a1 = math.pow(b, 2) + math.pow(c, 2)

print('O valor da hipotenusa é {:.2f}'.format(math.sqrt(a1)))