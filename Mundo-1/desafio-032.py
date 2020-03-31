cores = {'limpo': '\033[m',
         'verde': '\033[1;32m',
         'vermelho': '\033[1;31m'}
ano = int(input('Digite um ano: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} {cores["verde"]}é bissesto{cores["limpo"]}')
else:
    print(f'O ano {ano} {cores["vermelho"]}não é bissesto{cores["limpo"]}')
