print('=' * 37)
print('{:^37}'.format('BANCO CEV'))
print('=' * 37)
valor = int(input('Que valor você quer sacar?: R$'))
c50 = c20 = c10 = c1 = 0
if valor >= 50:
    while True:
        valor -= 50
        c50 += 1
        if valor < 50:
            break
    print(f'{c50} cédulas de R$50.00')
if valor >= 20:
    while True:
        valor -= 20
        c20 += 1
        if valor < 20:
            break
    print(f'{c20} cédulas de R$20.00')
if valor >= 10:
    while True:
        valor -= 10
        c10 += 1
        if valor < 10:
            break
    print(f'{c10} cédulas de R$10.00')
if valor >= 1:
    while True:
        valor -= 1
        c1 += 1
        if valor < 1:
            break
    print(f'{c1} cédulas de R$01.00')
print('=' * 37)
