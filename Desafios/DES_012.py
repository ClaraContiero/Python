km = float(input('Digite a quantidade de km rodados: \n'))
dias = int(input('Digite a quantidade de dias alugados: \n'))
preco = (60*dias) + (0.15*km)

print('*=*=*= ALUGUEL DE VEÍCULOS =*=*=*\n')
print(f'O preço a ser pago é igual a: R${preco:.2f}')
print('\nAgradecemos sua preferência :)')
