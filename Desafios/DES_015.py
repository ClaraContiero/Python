import math

angulo = int(input('Digite um ângulo qualquer: \n'))
radiano = math.radians(angulo)
seno = math.sin(radiano)
coss = math.cos(radiano)
tang = math.tan(radiano)

print(f'O seno de {angulo} é igual a {seno}\n'
      f'O cosseno de {angulo} é igual a {coss}\n'
      f'A tangente de {angulo} é igual a {tang}')
