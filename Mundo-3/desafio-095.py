# Declarando variáveis.
jogador = dict()
gols = list()
jogadores = list()

while True:
    print('-=-' * 20)
    jogador.clear()
    # Pegando valores para o dicionário "jogador" e para a lista "jogadores".
    jogador['nome'] = str(input('Nome do jogador: ')).strip().title()
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou?: '))
    for part in range(0, partidas):
        gols.append(int(input(f'  -> Quantos gols na {part+1}ª partida?: ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    gols.clear()
    jogadores.append(jogador.copy())

    # Criando uma escolha entre continuar digitando ou não.
    escolha = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if escolha not in 'SN':
        while escolha not in 'SN':
            escolha = str(input('Opção inválida! Quer continuar? [S/N] ')).strip().upper()[0]
    if escolha == 'N':
        break

# Mostrando uma tabela com os jogadores e seus dados.
print('-=-' * 20)
print('=' * 56)
print(f'{"N°":<5}{"Nome":<15}{"Gols":<30}{"Total":>5}')
print('=' * 56)
for j in range(0, len(jogadores)):
    print(f'{j:<5}', end='')
    print(f'{jogadores[j]["nome"]:<15}', end='')
    print(f'{str(jogadores[j]["gols"]):<30}', end='')
    print(f'{jogadores[j]["total"]:>5}')
print('=' * 56)

# Mostrando o levantamento de um jogador escolhido.
while True:
    busc = int(input('Mostrar dados de qual jogador? [999 para parar] '))
    if busc == 999:
        break
    if busc >= len(jogadores):
        print('Opção inválida! ', end='')
    else:
        print(f'   LEVANTAMENTO DO JOGADOR {jogadores[busc]["nome"].upper()}')
        for p, g in enumerate(jogadores[busc]['gols']):
            print(f'   -> Na {p+1}ª partida, {jogadores[busc]["nome"]} fez {g} gols')
        print('=' * 56)
