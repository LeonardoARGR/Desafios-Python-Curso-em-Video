matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matrix[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
maior = str(max(matrix))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        if c == 2:
            if len(maior) <= 5:
                print(f'[{matrix[l][c]:^5}]')
            else:
                print(f'[{matrix[l][c]:^{len(maior)}}]')
        else:
            if len(maior) <= 5:
                print(f'[{matrix[l][c]:^5}]', end='')
            else:
                print(f'[{matrix[l][c]:^{len(maior)}}]', end='')
