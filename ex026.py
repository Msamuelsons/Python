frase = str(input('Digite uma frase: ')).strip().lower()

print('A letra A aparece {}'.format(frase.count('a')))
print('A letra A aparece na primeira vez na posição {}'.format(frase.find('a')+1))
print('A letra A aparece em último na posição {}'.format(frase.rfind('a'))+1)