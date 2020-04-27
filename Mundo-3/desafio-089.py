from time import sleep

boletim = list()
while True:
    print('=' * 40)
    aluno = [[]]
    aluno.insert(0, str(input('Nome: ').strip().title()))
    for n in range(0, 2):
        nota = float(input(f'Nota {n+1}: '))
        if nota > 10 or nota < 0:
            while nota > 10 or nota < 0:
                nota = float(input(f'Nota inválida. Nota {n+1}: '))
        if 0 <= nota <= 10:
            aluno[1].append(nota)
    aluno.append((aluno[1][0] + aluno[1][1]) / 2)
    boletim.append(aluno[:])
    escolha = str(input('Quer continuar?: [S/N] ')).strip().upper()[0]
    if escolha not in 'SN':
        while escolha not in 'SN':
            escolha = str(input('Opção inválida. Quer continuar?: [S/N] ')).strip().upper()[0]
    if escolha == 'N':
        break
print('=' * 40)
print(f'{"n°":<5}{"NOME":<20}{"MÉDIA":>5}')
print('=' * 40)
for bol in range(0, len(boletim)):
    print(f'{bol:<5}', end='')
    print(f'{boletim[bol][0]:<20}', end='')
    print(f'{boletim[bol][2]:>5.1f}')
while True:
    print('=' * 40)
    notas = int(input('Mostrar notas de qual aluno? [999 interrompe] '))
    if notas >= len(boletim) and notas != 999 or notas < 0:
        while notas >= len(boletim) and notas != 999 or notas < 0:
            notas = int(input('Aluno selecionado não existe. Mostrar notas de qual aluno? [999 interrompe] '))
    if notas == 999:
        print('Finalizando', end='')
        for p in range(0, 3):
            sleep(1)
            print('.', end='')
        sleep(1)
        break
    print(f'Notas de {boletim[notas][0]} são {boletim[notas][1]}')
print()
print(f'{" VOLTE SEMPRE ":=^40}')
