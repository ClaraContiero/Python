nome = str(input('Digite seu nome:\n')).strip().title()
divide = nome.split()
count = len(divide)
print(divide)


print(f'Seu primeiro nome é: {divide[0]}\n'
      f'Seu último nome é: {divide[count-1]}')

# eu sou brilhante