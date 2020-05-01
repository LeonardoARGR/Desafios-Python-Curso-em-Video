print(f'{"-=-" * 5}(TABUADA){"-=-" * 5}')
numero = int(input('Digite um número: '))
for c in range(1, 11):
    if 0 < c < 10:
        if numero * c < 10:
            print(f'{numero} x 0{c} = 0{numero * c}')
        else:
            print(f'{numero} x 0{c} = {numero * c}')
    else:
        print(f'{numero} x {c} = {numero * c}')
print('-=-' * 13)
