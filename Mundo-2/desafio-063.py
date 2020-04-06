print(f'{"-=-" * 9}(Sequência de Fibonacci){"-=-" * 9}')
termos = int(input('Quantos termos você quer ver?: '))
numero1 = 0
numero2 = 1
soma = 0
cont = 0
print(f'{numero1} ', end='')
while cont != termos-1:
    soma = numero1 + numero2
    numero1 = numero2
    numero2 = soma
    print(f'-> {numero1} ', end='')
    cont += 1
print('-> Fim')
print('-=-' * 26)
