cores = {'limpo': '\033[m',
         'vermelho': '\033[31m',
         'verde': '\033[32m'}
numero = int(input('Digite um número: '))
tot = 0
for c in range(1, numero+1):
    if numero % c == 0:
        print('\033[32m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print(f'{c} ', end='')
print('\033[m')
print(f'O número {numero} foi divisível {tot} vezes')
if tot == 2:
    print(f'O número {numero} {cores["verde"]}é primo{cores["limpo"]}')
else:
    print(f'O número {numero} {cores["vermelho"]}não é primo{cores["limpo"]}')
