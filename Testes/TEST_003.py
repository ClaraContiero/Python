# import math
from math import sqrt, ceil

"""
Usando só o import:

num = int(input('Digite um número:\n'))
raiz = math.sqrt(num)
print(f'A raiz de {num} é igual a {math.ceil(raiz)}.')

"""

num = int(input('Digite um número:\n'))
raiz = sqrt(num)

print(f'A raiz de {num} é igual a {ceil(raiz)}.')

