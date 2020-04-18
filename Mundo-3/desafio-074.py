from random import randint
numeros = randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10)
print('=' * 40)
print('Os números sorteados são ', end='')
for seq in range(0, 5):
    if seq < 4:
        print(f'{numeros[seq]}, ', end='')
    else:
        print(f'{numeros[seq]}')
print(f'O maior número é o {max(numeros)}')
print(f'O menor número é o {min(numeros)}')
print('=' * 40)
