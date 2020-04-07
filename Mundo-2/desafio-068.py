from random import randint
from time import sleep
bot = 0
user = 0
cont = 0
print('-=-' * 27)
print(''' Olá usuário! Vamos jogar par ou ímpar? Vai ser assim: você vai escolher um número
de 0 a 10, e escolher entre par ou ímpar. Enquanto você ganha, o jogo não para, 
até você perder. Tudo pronto, vamos começar!''')
while True:
    print('-=-' * 27)
    bot = randint(0, 11)
    user = int(input('Qual número você escolhe?: '))
    if user > 10 or user < 0:
        while True:
            user = int(input('Desculpe, esta opção não existe, escolha outro número: '))
            if 0 <= user <= 10:
                break
    escolha = str(input('Qual você escolhe?: [P/I] ')).strip().upper()[0]
    if escolha != 'P' and escolha != 'I':
        while True:
            escolha = str(input('Esta opção não existe. Escolha uma opção: [P/I] ')).upper().strip()[0]
            if escolha == 'P' or escolha == 'I':
                break
    print('Par ', end='')
    sleep(1)
    print('ou ', end='')
    sleep(1)
    print('Ímpar')
    sleep(0.50)
    soma = user + bot
    if soma % 2 == 0:
        print(f'Você escolheu {user} e eu escolhi {bot}. A soma {soma} deu par')
    else:
        print(f'Você escolheu {user} e eu escolhi {bot}. A soma {soma} deu ímpar')
    if soma % 2 == 0 and escolha == 'P' or soma % 2 != 0 and escolha == 'I':
        print('Você ganhou!')
        cont += 1
        print('Vamos jogar outra vez', end='')
        sleep(0.75)
        print('.', end='')
        sleep(0.75)
        print('.', end='')
        sleep(0.75)
        print('.')
        sleep(0.75)
    if soma % 2 == 0 and escolha == 'I' or soma % 2 != 0 and escolha == 'P':
        print('Você perdeu!')
        if cont > 0:
            print(f'Você ganhou {cont} vezes')
        print('-=-' * 27)
        break
