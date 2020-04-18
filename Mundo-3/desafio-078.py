valores = list()
for v in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {v}: ')))
print(f'Os valores são {valores}')
print(f'O maior valor é o {max(valores)} e ele se localiza na(s) posição(ões)', end='')
for maior in range(0, 5):
    if valores[maior] == max(valores):
        print(f'...{valores.index(valores[maior], maior)}', end='')
print('')
print('-=-' * 20)
print(f'O menor valor é o {min(valores)} e ele se localiza na(s) posição(ões)', end='')
for menor in range(0, 5):
    if valores[menor] == min(valores):
        print(f'...{valores.index(valores[menor], menor)}', end='')
