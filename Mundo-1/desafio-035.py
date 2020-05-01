from math import fabs
cores = {'limpo': '\033[m',
         'vermelho': '\033[1;31m',
         'verde': '\033[1;32m'}
a = float(input('Primeira reta: '))
b = float(input('Segunda reta: '))
c = float(input('Terceira reta: '))
if fabs(a-b) < c < a + b and fabs(a-c) < b < a + c and fabs(b-c) < a < (b + c):
    print(f'Com estas retas, {cores["verde"]}você consegue fazer um triângulo{cores["limpo"]}')
else:
    print(f'Com estas retas, {cores["vermelho"]}você não consegue fazer um triângulo{cores["limpo"]}')
