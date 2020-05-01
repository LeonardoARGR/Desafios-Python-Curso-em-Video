cores = {'limpo': '\033[m',
         'verde': '\033[1;32m',
         'vermelho': '\033[1;31m'}
n1 = float(input('Primeira Nota: '))
n2 = float(input('Segunda Nota: '))
m = (n1+n2) / 2
if m < 5:
    print('A sua nota foi {}{}{}'.format(cores['vermelho'], m, cores['limpo']))
else:
    print('A sua nota foi {}{}{}'.format(cores['verde'], m, cores['limpo']))
