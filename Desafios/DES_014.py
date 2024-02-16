from math import pow, sqrt, hypot

catetoA = float(input('Comprimento do cateto adjacente: \n'))
catetoO = float(input('Comprimento do cateto oposto: \n'))
hipo = sqrt(pow(catetoA, 2) + pow(catetoO,2))

print(f'A hipotenusa é igual a {hipo:.2f}.')

# método hypot calcula direto, é só colocar hypo(catetoO, catetoA)

