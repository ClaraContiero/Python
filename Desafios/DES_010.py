preco = float(input('Digite o preço do produto: \n'))
novo_preco = preco - (preco*(5/100))

print(f'O produto que custava R${preco:.2f}, agora custa R${novo_preco:.2f}')
