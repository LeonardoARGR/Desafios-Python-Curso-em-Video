cores = {'limpo': '\033[m',
         'vermelho': '\033[1;31m',
         'verde': '\033[1;32m',
         'azul': '\033[1;34m'}
C = float(input('Indique a temperatura em °C: '))
F = 9 * C / 5 + 32
if C > 32:
    print(f'A temperatura {cores["vermelho"]}{C}°C{cores["limpo"]} é igual à {cores["vermelho"]}{F}°F{cores["limpo"]}')
if C < 13:
    print(f'A temperatura {cores["azul"]}{C}°C{cores["limpo"]} é igual à {cores["azul"]}{F}°F{cores["limpo"]}')
else:
    print(f'A temperatura {cores["verde"]}{C}°C{cores["limpo"]} é igual à {cores["verde"]}{F}°F{cores["limpo"]}')


