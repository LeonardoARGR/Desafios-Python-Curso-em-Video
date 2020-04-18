lista = list()
while True:
    lista.append(int(input('Digite um número: ')))
    escolha = str(input('Quer continuar?: [S/N] ')).strip().upper()[0]
    if escolha not in 'SN':
        while escolha not in 'SN':
            escolha = str(input('Opção inválida. Quer continuar?: [S/N] ')).strip().upper()[0]
    print('=' * 20)
    if escolha == 'N':
        break
print(f'Quantidade de valores: {len(lista)}')
lista.sort(reverse=True)
print(f'Valores na ordem decrescente: {lista}')
if 5 in lista:
    print('O valor 5 está na lista')
else:
    print('O valor 5 não está na lista')
