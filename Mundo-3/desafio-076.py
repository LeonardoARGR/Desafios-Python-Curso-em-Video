lista = 'Redmi Airdots', 129.90, 'Controle Xbox One', 200.0, 'Headset Spider Tarantula', 90.0, \
        'Mouse Spider 2', 40.0, 'Pilha Duracell', 9.55, 'Nintendo Switch', 2099.99
print('=' * 61)
print('{:^61}'.format('LISTAGEM DE PREÇOS'))
print('=' * 61)
for lis in range(0, len(lista)):
    if lis % 2 == 0:
        print('{:.<51}R$ '.format(lista[lis]), end='')
    else:
        print('{:>7.2f}'.format(lista[lis]))
print('=' * 61)
