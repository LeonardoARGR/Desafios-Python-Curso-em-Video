matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = somacoluna3 = 0
for l in range(0, 3):
    for c in range(0, 3):
        matrix[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matrix[l][c] % 2 == 0:
            somapar += matrix[l][c]
        if c == 2:
            somacoluna3 += matrix[l][c]
maior = str(max(matrix))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        if len(maior) > 5:
            print(f'[{matrix[l][c]:^{len(maior)}}]', end='')
        else:
            print(f'[{matrix[l][c]:^5}]', end='')
    print()
print('-=' * 30)
print(f'A soma dos valores pares é {somapar}')
print(f'A soma dos valores da terceira coluna é {somacoluna3}')
print(f'O maior valor da segunda linha é {max(matrix[1])}')
