lista = list()
listapar = list()
listaimpar = list()
while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    if num % 2 == 0:
        listapar.append(num)
    else:
        listaimpar.append(num)
    escolha = str(input('Quer continuar?: [S/N] ')).strip().upper()[0]
    if escolha not in 'SN':
        while escolha not in 'SN':
            escolha = str(input('Opção inválida. Quer continuar?: [S/N] ')).strip().upper()[0]
    print('=-' * 30)
    if escolha == 'N':
        break
print(f'Números digitados: {lista}')
print(f'Números pares: {listapar}')
print(f'Números ímpares: {listaimpar}')
