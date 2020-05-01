print(f'{"-=-" * 10}(Progressão Aritmética){"-=-" * 10}')
número = int(input('Digite um número: '))
razão = int(input('Digite a razão: '))
contador = 0
escolha = 9
acum = 1
print(f'{número} ', end='')
while escolha != 0:
    while contador != escolha:
        número += razão
        contador += 1
        acum += 1
        print(f'-> {número} ', end='')
    print('')
    escolha = int(input('Quantos outros termos você quer ver?: '))
    contador = 0
print(f'O programa foi finalizado com {acum} termos')
print('-=-' * 28)
