cores = {'limpo': '\033[m',
         'vermelho': '\033[1;31m',
         'verde': '\033[1;32m'}
n = int(input('Digite um número: '))
if n % 2 == 0:
    print(f'Este número é {cores["verde"]}par{cores["limpo"]}')
else:
    print(f'Este número é {cores["vermelho"]}impar{cores["limpo"]}')

