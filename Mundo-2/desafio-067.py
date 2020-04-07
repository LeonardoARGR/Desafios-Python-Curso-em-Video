while True:
    número = int(input('Que valor você quer ver a tabuáda?: '))
    produto = 0
    cont = 1
    if número < 0:
        break
    print('-=-' * 14)
    while cont <= 10:
        produto = número * cont
        print(f'{número} x {cont :2} = {produto :2}')
        cont += 1
    print('-=-' * 14)
print('Fim do programa')
print('-=-' * 14)
