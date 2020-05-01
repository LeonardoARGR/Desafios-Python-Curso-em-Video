print('-=-' * 17)
valor = cont = maior = menor = acum =0
opção = ''
while opção != 'N':
    valor = int(input('Digite um valor: '))
    cont += 1
    acum += valor
    if cont == 1:
        maior = valor
        menor = valor
    else:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor
    opção = str(input('Quer contituar? [S/N]: ')).strip().upper()[0]
print(f'Você digitou {cont} números')
print(f'A média de todos os valores resulta em {acum / cont :.1f}')
print(f'O maior valor entre os números acima é o {maior}')
print(f'O menor valor entre os números acima é o {menor}')
print('-=-' * 17)
