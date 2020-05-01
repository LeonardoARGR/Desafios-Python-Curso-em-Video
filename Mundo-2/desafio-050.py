s = 0
cont = 0
for c in range(1, 7):
    n1 = int(input(f'Digite o {c}° número: '))
    if n1 % 2 == 0:
        s += n1
        cont += 1
print(f'O resultado da soma de {cont} números pares resulta no número {s}')
