valor = 0
valores = list()
for v in range(0, 5):
    valor = int(input('Digite um número: '))
    if v == 0 or valor > valores[-1]:
        valores.append(valor)
        print('Adicionado na posição final da lista...')
    else:
        pos = 0
        while pos < len(valores):
            if valor <= valores[pos]:
                valores.insert(pos, valor)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print('=-' * 30)
print(f'Os valores digitados na ordem crescente são {valores}')
