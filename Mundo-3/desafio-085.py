lista = [[], []]
for v in range(1, 8):
    valor = int(input(f'Digite o {v}° valor: '))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
print('-=-' * 20)
print(f'Valores pares: {sorted(lista[0])}')
print(f'Valores ímpares: {sorted(lista[1])}')
