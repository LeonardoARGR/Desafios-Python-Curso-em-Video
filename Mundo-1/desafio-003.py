cores = {'verde': '\033[1;32m',
         'ciano': '\033[1;36m',
         'limpo': '\033[m'}
n1 = int(input('digite um número: '))
n2 = int(input('digite outro número: '))
s: int = n1 + n2
print('A soma entre {}{}{} e {}{}{} vale {}{}' .format(cores['verde'], n1, cores['limpo'], cores['verde'], n2, cores['limpo'], cores['ciano'], s))
