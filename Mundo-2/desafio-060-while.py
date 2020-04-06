número = int(input('Digite um número: '))
multiplicador = número - 1
print(f'{número} ', end='')
while multiplicador != 0:
    print(f'x {multiplicador} ', end='')
    número *= multiplicador
    multiplicador -= 1
print(f'= {número}')
