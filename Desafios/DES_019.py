nome = str(input('Qual seu nome completo?\n'))
maius = nome.upper()
minus = nome.lower()
cont = len(nome.replace(' ', '')) # ou posso fazer len(nome) - nome.count(' ')
# primNome = nome.find(' ')
separa = nome.split()



print(f'\nAnalisando seu nome...\n'
      f'Seu nome em maiúscula: {maius}\n'
      f'Seu nome em minuscula: {minus}\n'
      f'Total de letras: {cont}\n'
      f'Seu primeiro nome tem {len(separa[0])} letras')

