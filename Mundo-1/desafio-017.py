from math import hypot
cores = {'limpo': '\033[m',
         'ciano': '\033[1;36m'}
co = float(input('Qual o tamanho do cateto oposto?: '))
ca = float(input('Qual o tamanho do cateto adjacente?: '))
h = hypot(ca, co)
print(f'O valor da hipotenusa é {cores["ciano"]}{h :.2f}{cores["limpo"]}')
