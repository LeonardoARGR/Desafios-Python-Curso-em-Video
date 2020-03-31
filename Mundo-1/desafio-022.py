cores = {'limpo': '\033[m',
         'vermelho': '\033[1;31m',
         'verde': '\033[1;32m',
         'amarelo': '\033[1;33m',
         'azul': '\033[1;34m'}
nome = str(input('Digite o seu nome completo: ')).strip()
ns = nome.split()
print(f'Nome com todas as letras em maiúsculo: {cores["vermelho"]}{nome.upper()}{cores["limpo"]}')
print(f'Nome com todas as letras em minúsculo: {cores["verde"]}{nome.lower()}{cores["limpo"]}')
print(f'Quantidade de letras: {cores["amarelo"]}{len(nome) - nome.count(" ")}{cores["limpo"]}')
print(f'Quantidade de letras do primeiro nome: {cores["azul"]}{len(ns[0])}{cores["limpo"]}')
