print(f'{"-=-" * 5}(Progressão Aritmética){"-=-" * 5}')
numero = int(input('Digite um número: '))
razao = int(input('Indique a razão: '))
calculo = numero + (10 - 1) * razao
print(f'Do primeiro ao décimo termo:')
for c in range(numero, calculo+razao, razao):
    print(c, end=' -> ')
print('FIM')
print('-=-' * 17)
