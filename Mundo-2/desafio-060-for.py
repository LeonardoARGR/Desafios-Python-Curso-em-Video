número = int(input('Digite um número: '))
print(f'{número} ', end='')
for c in range(número-1, 0, -1):
    print(f'x {c} ', end='')
    número *= c
print(f'= {número}')
