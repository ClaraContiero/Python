larg = float(input('Digite a largura da parede: \n'))
alt = float(input('Digite a altura da parede: \n'))
area = alt * larg
tinta = area // 2

print(f'A área da parede é igual a: {area} m2, e serão necessários {tinta:.0f} baldes de tinta.')
