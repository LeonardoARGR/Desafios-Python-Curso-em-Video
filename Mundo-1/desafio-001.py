print('=======DESAFIO 1=======')
cores = {'vazio': '\033[m',
         'ciano': '\033[1;36m'}
nome = input('Qual o seu nome?: ')
print('Olá {}{}{}! Seja bem vindo!'.format(cores['ciano'], nome, cores['vazio']))
