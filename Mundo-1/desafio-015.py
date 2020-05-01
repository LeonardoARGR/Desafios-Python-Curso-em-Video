cores = {'limpo': '\033[m',
         'verde': '\033[1;32m'}
dias = int(input('Quantos dias você está com o carro alugado?: '))
km = float(input('Quantos km você andou com o carro?: '))
p = (dias * 60) + (km * 0.15)
print(f'O preço a pagar pelo carro alugado é de {cores["verde"]}R${p :.2f}{cores["limpo"]}')

