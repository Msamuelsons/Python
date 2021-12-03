tempo = int(input('Quantos anos têm seu carro ? '))

if tempo <= 3:
    print('Seu carro é novo pois tem {} anos'.format(tempo))
else:
    print('Seu carro é velho pois tem {} anos'.format(tempo))
print('---fim---')

print('Você é novo' if tempo<=50 else 'Você é velho') 


nome = str(input('Qual seu nome: '))
if nome == "Samuel":
    print('Que nome lindo você têm')
else:
    print('Seu nome é tão normal')
print('Bom dia {}'.format(nome))