var = input('Digite algo...\n')
var_tipo = type(var)

print(f'O valor digitado {var} é do tipo {var_tipo}. '
      f'\nÉ numérico? {var.isnumeric()}. '
      f'\nÉ alfabético? {var.isalpha()}'
      f'\nEstá em maiúscula? {var.isupper()}'
      f'\nEstá em minúscula? {var.islower()}')

