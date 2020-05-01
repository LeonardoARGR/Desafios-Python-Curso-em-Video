cores = {'limpo': '\033[m',
         'verde': '\033[1;32m',
         'amarelo': '\033[1;33m',
         'azul': '\033[1;34m'}
L = float(input('Largura em metro: '))
A = float(input('Altura em metro: '))
area = L * A
ldt = area / 2
print(f'Sua parede tem a dimensão de {cores["amarelo"]}{L}x{A}{cores["limpo"]}. A área é de {cores["verde"]}{area :.4f}²{cores["limpo"]}, e a quantidade de tinta\nque tem que ser utilizada para preencher ela é de {cores["azul"]}{ldt :.4f}{cores["limpo"]} litros')



