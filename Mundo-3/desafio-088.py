from random import randint
from time import sleep

jogos = list()
jogo = list()
print('=' * 45)
print(f'{"JOGA NA MEGA SENA":^45}')
print('=' * 45)
escolha = int(input('Quantos jogos você quer que eu sorteie?: '))
print(f'{f" SORTEANDO {escolha} JOGOS ":=^45}')
for j in range(0, escolha):
    for n in range(0, 6):
        random = randint(1, 60)
        if random not in jogo:
            jogo.append(random)
        else:
            while True:
                random = randint(1, 60)
                if random not in jogo:
                    jogo.append(random)
                    break
    jogo.sort()
    jogos.append(jogo[:])
    jogo.clear()
    print(f'Jogo {j+1}: {jogos[j]}')
    sleep(1)
print(f'{" BOA SORTE! ":=^45}')
