cores = {'limpo': '\033[m',
         'verde': '\033[1;32m',
         'azul': '\033[1;34m'}
km = float(input('Quantos quilômetros de distância tem a viagem?: '))
if km > 200:
    print(f'O preço da passagem é de {cores["verde"]}R${0.45 * km :.2f}{cores["limpo"]}')
else:
    print(f'O preço da passagem é de {cores["azul"]}R${0.50 * km :.2f}{cores["limpo"]}')
print('Tenha uma boa viagem!')
