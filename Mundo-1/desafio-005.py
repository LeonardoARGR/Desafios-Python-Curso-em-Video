cores = {'limpo': '\033[m',
         'vermelho': '\033[31m',
         'azul': '\033[34m',
         'verde': '\033[32m'}
n1 = int(input('Coloque um número: '))
n2 = int(n1-1)
n3 = int(n1+1)
print('{}{}{} < {}{}{} < {}{}{}'.format(cores['vermelho'], n2, cores['limpo'], cores['azul'], n1, cores['limpo'], cores['verde'], n3, cores['limpo']))
