brasileirao2018 = 'Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo', \
                  'Atlético MG', 'Athletico PR', 'Cruzeiro', 'Botafogo', 'Santos', \
                  'Bahia', 'Fluminense', 'Corinthians', 'Chapecoense', 'Ceará', \
                  'Vasco', 'Sport', 'América-MG', 'Vitória', 'Paraná'
brasileiraoabc = sorted(brasileirao2018)
poschape = 0

print('=' * 30)
print('{:^30}'.format('BRASILEIRÃO 2018'))
print('=' * 30)
print('Lista do Brasileirão 2018:')
for lista in range(0, 20):
    if lista < 9:
        print(f'0{lista + 1}° colocado - {brasileirao2018[lista]}')
    else:
        print(f'{lista + 1}° colocado - {brasileirao2018[lista]}')
print('=' * 30)
print(f'Os 5 Primeiros Colocados:')
for pri in range(0, 5):
    print(f'0{pri+1}° colocado - {brasileirao2018[pri]}')
print('=' * 30)
print('Os 4 últimos colocados:')
for ult in range(16, 20):
    print(f'{ult + 1}° colocado - {brasileirao2018[ult]}')
print('=' * 30)
print('Os times em ordem alfabética:')
for abcd in range(0, 20):
    if abcd < 9:
        print(f'0{abcd + 1}- {brasileiraoabc[abcd]}')
    else:
        print(f'{abcd + 1}- {brasileiraoabc[abcd]}')
print('=' * 30)
print(f'Posição da Chapecoense: {brasileirao2018.index("Chapecoense") + 1}°')
print('=' * 30)
print('{:^30}'.format('FIM DO PROGRAMA'))
print('=' * 30)
