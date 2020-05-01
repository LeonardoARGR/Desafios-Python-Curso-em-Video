cores = {'limpo': '\033[m',
         'vermelho': '\033[1;31m',
         'verde': '\033[1;32m'}
nome = str(input('Digite o nome: ')).lower().strip()
if not 'silva' in nome:
    print(f'O nome contém "Silva" nele?: {cores["vermelho"]}{"silva" in nome}{cores["limpo"]}')
else:
    print(f'O nome contém "Silva" nele?: {cores["verde"]}{"silva" in nome}{cores["limpo"]}')
