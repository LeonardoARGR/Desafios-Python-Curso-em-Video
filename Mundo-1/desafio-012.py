cores = {'limpo': '\033[m',
         'roxo': '\033[1;35m'}
valor = float(input('Valor original do produto: R$'))
desconto = valor - (valor * 5 / 100)
print(f'O valor final com desconto é de {cores["roxo"]}R${desconto :.2f}{cores["limpo"]}')

