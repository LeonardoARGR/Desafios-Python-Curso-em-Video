import math
cores = {'limpo': '\033[m',
         'vermelho': '\033[1;31m',
         'verde': '\033[1;32m',
         'amarelo': '\033[1;33m',
         'azul': '\033[1;34m'}
ang = (float(input('Digite um ângulo: ')))
se = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print(f'O ângulo {cores["vermelho"]}{ang}°{cores["limpo"]} tem o SENO de {cores["verde"]}{se :.2f}{cores["limpo"]}')
print(f'O ângulo {cores["vermelho"]}{ang}°{cores["limpo"]} tem o COSSENO de {cores["amarelo"]}{cos :.2f}{cores["limpo"]}')
print(f'O ângulo {cores["vermelho"]}{ang}°{cores["limpo"]} tem a TANGENTE de {cores["azul"]}{tan :.2f}{cores["limpo"]}')
