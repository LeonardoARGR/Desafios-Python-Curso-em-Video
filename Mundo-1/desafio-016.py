from math import floor
cores = {'limpo': '\033[m',
         'verde': '\033[1;32m',
         'azul': '\033[1;34m'}
num = float(input('Digite um número: '))
print(f'O número {cores["verde"]}{num}{cores["limpo"]} tem a parte inteira de {cores["azul"]}{floor(num)}{cores["limpo"]}')
