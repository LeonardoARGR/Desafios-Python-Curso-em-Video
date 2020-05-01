# Declarando as variáveis.
jogador = dict()
gols = list()

# Adicionando os valores ao dicionário "jogador".
jogador['nome'] = str(input('Nome do jogador: ')).strip().title()
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou?: '))
# Pegando os gols de cada partida utilizando o FOR.
for g in range(0, partidas):
    gols.append(int(input(f'Quantos gols na {g+1}ª partida?: ')))
jogador['gols'] = gols[:]
jogador['total'] = sum(gols)

# Mostrando o dicionário
print('-=-' * 30)
print(jogador)

# Mostrando na tela os valores de cada key do dicionário "jogador".
print('-=-' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')

# Mostrando na tela a quantidade de partidas jogadas e os gols de cada uma, e o total de gols.
print('-=-' * 30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for p in range(0, partidas):
    print(f'   -> Na {p+1}ª partida, fez {jogador["gols"][p]} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
