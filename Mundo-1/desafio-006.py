cores = {'limpo': '\033[m',
         'verde': '\033[32m',
         'azul': '\033[34m',
         'roxo': '\033[35m',
         'amarelo': '\033[33m'}
n1 = float(input('Coloque um número: '))
d = n1*2
t = n1*3
r = n1**(1/2)
print('Número: {}{}{} \nDobro: {}{}{} \nTriplo: {}{}{} \nRaiz Quadrada: {}{}{}'.format(cores['verde'], n1, cores['limpo'], cores['azul'], d, cores['limpo'], cores['roxo'], t, cores['limpo'], cores['amarelo'], r, cores['limpo']))
