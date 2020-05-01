from random import randint
from time import sleep
sn = ''
print(f'{"-=-" * 10}(JOGO DA ADIVINHAÇÃO){"-=-" * 10}')
print('''Olá humano! Quer jogar um jogo? Eu vou pensar em um número de 0 a 10 e você 
tem que adivinhar ele, ok? Bom, vamos começar!''')
while sn != 'N':
    computador = randint(0, 10)
    valor = 11
    tentativas = 0
    print('-=-' * 27)
    print('Pensando...')
    sleep(1.5)
    while valor != computador:
        valor = int(input('Em que número estou pensando?: '))
        if valor < computador:
            print('Opa, o valor que você digitou é menor do que o que eu estou pensando')
        elif valor > computador:
            print('Opa, o valor que você digitou é maior do que o que eu estou pensando')
        tentativas += 1
    if tentativas == 1:
        print(f'PARABÉNS! Você acertou DE PRIMEIRA! Eu realmente estava pensando no número {computador}')
    else:
        print(f'Parabéns, você acertou! Eu realmente estava pensando no número {computador}')
        print(f'Número de tentativas: {tentativas}')
    sn = str(input('Jogar novamente? [S/N]: ')).upper().strip()
    if sn == 'N':
        print('-=-' * 27)
