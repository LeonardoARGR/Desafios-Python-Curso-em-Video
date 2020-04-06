from time import sleep
escolha = 0
valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
print('-=-' * 15)
while escolha != 5:
    print('''[1]- Somar
[2]- Multiplicar
[3]- Maior
[4]- Digitar outros números
[5]- Finalizar o código''')
    escolha = int(input('Qual opção você escolhe?: '))
    if escolha == 1:
        print(f'{valor1} + {valor2} = {valor1 + valor2}')
        print('-=-' * 15)
        sleep(1)
    elif escolha == 2:
        print(f'{valor1} x {valor2} = {valor1 * valor2}')
        print('-=-' * 15)
        sleep(1)
    elif escolha == 3:
        if valor1 > valor2:
            print(f'O número {valor1} é o maior')
            print('-=-' * 15)
            sleep(1)
        elif valor1 < valor2:
            print(f'O número {valor2} é o maior')
            print('-=-' * 15)
            sleep(1)
        else:
            print('Os dois são iguais')
            print('-=-' * 15)
            sleep(1)
    elif escolha == 4:
        print('-=-' * 15)
        valor1 = int(input('Digite o primeiro valor: '))
        valor2 = int(input('Digite o segundo valor: '))
    elif escolha == 5:
        print('Finalizando...')
        sleep(1)
        print('Fim do Programa')
        print('-=-' * 15)
    elif escolha not in (1, 5):
        print('Esta opção não existe, tente novamente')
        print('-=-' * 15)
        sleep(1)
