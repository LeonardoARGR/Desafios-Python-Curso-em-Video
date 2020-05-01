import random
import time
cores = {'limpo': '\033[m',
         'azul': '\033[1;34m',
         'verde': '\033[1;32m',
         'vermelho': '\033[1;31m'}
escolha = random.choice([0, 1, 2, 3, 4, 5])
print(f'{cores["azul"]}===========================(JOGO DA ADIVINHAÇÃO)==========================={cores["limpo"]}')
print("""Olá humano! Quer jogar um jogo? Eu vou pensar em um número de 0 a 5 e você 
tem que adivinhar ele, ok? Bom, vamos começar!""")
print(f'{cores["azul"]}==========================================================================={cores["limpo"]}')
print(f'{cores["azul"]}Pensando...{cores["limpo"]}')
time.sleep(2)
número = int(input('Em qual número estou pensando?: '))
print(f'{cores["azul"]}Processando...{cores["limpo"]}')
time.sleep(2)
if número == escolha:
    print(f'{cores["verde"]}Parabéns{cores["limpo"]}, você me venceu!')
else:
    print(f'{cores["vermelho"]}GANHEI!{cores["limpo"]} Eu pensei no número {escolha} e não no {número}.')
print(f'{cores["azul"]}===================================(FIM)==================================={cores["limpo"]}')
