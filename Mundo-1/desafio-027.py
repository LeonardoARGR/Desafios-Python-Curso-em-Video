cores = {'limpo': '\033[m',
         'ciano': '\033[1;36m',
         'azul': '\033[1;34m',
         'roxo': '\033[1;35m'}
nome = str(input('Digite um nome a seguir: ')).strip()
ns = nome.split()
print(f'Olá {cores["ciano"]}{nome}{cores["limpo"]}!')
print(f'Seu primeiro nome é: {cores["roxo"]}{ns[0]}{cores["limpo"]}')
print(f'Seu último nome é: {cores["azul"]}{ns[-1]}{cores["limpo"]}')
