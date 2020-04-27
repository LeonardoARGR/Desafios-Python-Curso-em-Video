dados = list()
pessoas = list()
maiornome = list()
menornome = list()
cont = maior = menor = -1
while True:
    dados.append(str(input('Nome: ')).strip())
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    escolha = str(input('Deseja continuar?: [S/N] ')).strip().upper()[0]
    if escolha not in 'SN':
        while escolha not in 'SN':
            escolha = str(input('Opção inválida. Deseja continuar?: [S/N] ')).strip().upper()[0]
    if escolha == 'N':
        break
print('=' * 35)
print(f'Você registrou {len(pessoas)} pessoas.')
print(f'O maior peso é de {maior}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maior:
        print(p[0], end=' ')
print()
print(f'O menor peso é de {menor}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menor:
        print(p[0], end=' ')
