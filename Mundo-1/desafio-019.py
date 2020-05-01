from random import choice
cores = {'limpo': '\033[m',
         'vermelho': '\033[1;31m',
         'verde': '\033[1;32m',
         'amarelo': '\033[1;33m',
         'azul': '\033[1;34m'}
a1 = str(input(f'{cores["vermelho"]}Primeiro aluno: {cores["limpo"]}'))
a2 = str(input(f'{cores["verde"]}Segundo aluno: {cores["limpo"]}'))
a3 = str(input(f'{cores["amarelo"]}Terceiro aluno: {cores["limpo"]}'))
a4 = str(input(f'{cores["azul"]}Quarto aluno: {cores["limpo"]}'))
lista = [a1, a2, a3, a4]
escolhido = choice(lista)
if escolhido == a1:
    print(f'O aluno sorteado foi {cores["vermelho"]}{escolhido}{cores["limpo"]}')
if escolhido == a2:
    print(f'O aluno sorteado foi {cores["verde"]}{escolhido}{cores["limpo"]}')
if escolhido == a3:
    print(f'O aluno sorteado foi {cores["amarelo"]}{escolhido}{cores["limpo"]}')
if escolhido == a4:
    print(f'O aluno sorteado foi {cores["azul"]}{escolhido}{cores["limpo"]}')
