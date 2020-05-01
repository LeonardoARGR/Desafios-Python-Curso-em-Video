print(f'{"-=-" * 10}(Progressão Aritmética){"-=-" * 10}')
número = int(input('Digite um número: '))
razão = int(input('Digite a razão: '))
limite = número + (10 - 1) * razão
print(f'{número} ', end='')
while número != limite:
    número += razão
    print(f'-> {número} ', end='')
print('-> Acabou')
print('-=-' * 28)
