num = int(input('Digite um número: ')), \
      int(input('Digite outro número: ')), \
      int(input('Digite mais um número: ')), \
      int(input('Digite o último número: '))
if 9 in num:
    if num.count(9) == 1:
        print(f'O valor 9 apareceu {num.count(9)} vez')
    else:
        print(f'O valor 9 apareceu {num.count(9)} vezes')
else:
    print(f'O valor 9 não apareceu')
if 3 in num:
    print(f'O primeiro valor 3 apareceu na posição {num.index(3) + 1}')
else:
    print('O valor 3 não apareceu')
print(f'Os valores pares são: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
