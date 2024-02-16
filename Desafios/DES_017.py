import random

nome1 = input('Aluno 1:\n')
nome2 = input('Aluno 2:\n')
nome3 = input('Aluno 3:\n')
nome4 = input('Aluno 4:\n')

lista = [nome1, nome2, nome3, nome4]
random.shuffle(lista) # embaralha a lista

print(f'A ordem de alunos a apresentar é: {lista}')


