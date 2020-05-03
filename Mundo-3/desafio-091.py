# Importando funções.
from random import randint
from time import sleep
from operator import itemgetter

# Declarando os dicionários.
jogadores = dict()
colocacao = list()

# Colocando os jogadores e seus valores no dicionário, e mostrando eles na tela.
for r in range(1, 5):
    jogadores[f'jogador{r}'] = randint(1, 6)
    print(f'O jogador{r} tirou {jogadores[f"jogador{r}"]} no dado.')
    sleep(0.5)

# Criando uma linha para organizar o programa.
print('=' * 25)
print(f'{"Ranking dos Jogadores":^25}')
print('=' * 25)

# Criando e mostrando na tela a colocação em ordem.
colocacao = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(colocacao):
    print(f'{i+1}° lugar - {v[0]} com {v[1]}')
