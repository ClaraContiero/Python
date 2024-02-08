from math import pow, sqrt

catetoA = float(input('Comprimento do cateto adjacente: \n'))
catetoO = float(input('Comprimento do cateto oposto: \n'))
hipo = sqrt(pow(catetoA, 2) + pow(catetoO,2))

print(f'A hipotenusa é igual a {hipo}.')


