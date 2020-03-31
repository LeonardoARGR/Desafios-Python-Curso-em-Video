cores = {'verde': '\033[1;32m',
         'limpo': '\033[m'}
r = float(input('Quantos reais você tem?: R$'))
d = r * 0.305810397553
print(f'Você pode comprar {cores["verde"]}{d :.2f}{cores["limpo"]} dolares')

