cores = {'limpo': '\033[m',
         'verde': '\033[32m',
         'vermelho': '\033[31m',
         'azul': '\033[34m'}
n = str(input('Digite algo: '))
if type(n) == str:
    print('Tipo primitivo: {}{}{}'.format(cores['azul'], 'str', cores['limpo']))
    if not n.isspace():
        print('Só tem espaço?: {}{}{}'.format(cores['vermelho'], n.isspace(), cores['limpo']))
    else:
        print('Só tem espaço?: {}{}{}'.format(cores['verde'], n.isspace(), cores['limpo']))
    if not n.isnumeric():
        print('É um número?: {}{}{}'.format(cores['vermelho'], n.isnumeric(), cores['limpo']))
    else:
        print('É um número?: {}{}{}'.format(cores['verde'], n.isnumeric(), cores['limpo']))
    if not n.isalpha():
        print('É alfabético?: {}{}{}'.format(cores['vermelho'], n.isalpha(), cores['limpo']))
    else:
        print('É alfabético?: {}{}{}'.format(cores['verde'], n.isalpha(), cores['limpo']))
    if not n.isalnum():
        print('É alfanumérico?: {}{}{}'.format(cores['vermelho'], n.isalnum(), cores['limpo']))
    else:
        print('É alfanumérico?: {}{}{}'.format(cores['verde'], n.isalnum(), cores['limpo']))
    if not n.isupper():
        print('Está em maiúsculo?: {}{}{}'.format(cores['vermelho'], n.isupper(), cores['limpo']))
    else:
        print('Está em maiúsculo?: {}{}{}'.format(cores['verde'], n.isupper(), cores['limpo']))
    if not n.islower():
        print('Está em minúsculo?: {}{}{}'.format(cores['vermelho'], n.islower(), cores['limpo']))
    else:
        print('Está em minúsculo?: {}{}{}'.format(cores['verde'], n.islower(), cores['limpo']))
    if not n.istitle():
        print('Está capitalizada?: {}{}{}'.format(cores['vermelho'], n.istitle(), cores['limpo']))
    else:
        print('Está capitalizada?: {}{}{}'.format(cores['verde'], n.istitle(), cores['limpo']))
if type(n) == int:
    print('Tipo primitivo: {}{}{}'.format(cores['azul'], 'int', cores['limpo']))
if type(n) == bool:
    print('Tipo primitivo: {}{}{}'.format(cores['azul'], 'bool', cores['limpo']))
if type(n) == float:
    print('Tipo primitivo: {}{}{}'.format(cores['azul'], 'float', cores['limpo']))