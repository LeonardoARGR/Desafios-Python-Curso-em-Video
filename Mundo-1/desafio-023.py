cores = {'limpo': '\033[m',
         'vermelho': '\033[1;31m',
         'verde': '\033[1;32m',
         'amarelo': '\033[1;33m',
         'azul': '\033[1;34m'}
num = int(input('Digite um número de 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Unidade: {cores["vermelho"]}{u}{cores["limpo"]}\nDezena: {cores["verde"]}{d}{cores["limpo"]}\nCentena: {cores["amarelo"]}{c}{cores["limpo"]} \nMilhar: {cores["azul"]}{m}{cores["limpo"]}')
