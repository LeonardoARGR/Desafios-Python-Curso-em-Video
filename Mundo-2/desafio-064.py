print('-=-' * 17)
valor = cont = acum = 0
while valor != 999:
    valor = int(input('Digite um número [999 para parar]: '))
    if valor != 999:
        acum += valor
        cont += 1
print(f'Você digitou {cont} valores e a soma deles resulta no número {acum}')
print('-=-' * 17)
