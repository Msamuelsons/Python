from random import shuffle
al1 = input('Informe o noe do primeiro aluno: ')
al2 = input('Informe o noe do segundo aluno: ')
al3 = input('Informe o noe do terceiro aluno: ')
al4 = input('Informe o noe do quarto aluno: ')

lista = [al1, al2, al3, al4]
shuffle(lista)
print('O aluno1 sorteado é {}'.format(lista))
