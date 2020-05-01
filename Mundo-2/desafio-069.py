contH = contM20 = cont18 = 0
while True:
    print('=' * 25)
    print('{:^25}'.format('   REGISTRE UMA PESSOA   '))
    print('=' * 25)
    idade = int(input('Qual é a sua idade?: '))
    sexo = str(input('Qual é o seu sexo?: [M/F] ')).strip().upper()[0]
    if sexo != 'M' and sexo != 'F':
        while True:
            sexo = str(input('Opção inválida. Digite o seu sexo: [M/F] ')).strip().upper()[0]
            if sexo == 'M' or sexo == 'F':
                break
    if sexo == 'M':
        contH += 1
    if idade > 18:
        cont18 += 1
    if sexo == 'F' and idade < 20:
        contM20 += 1
    print('=' * 25)
    escolha = str(input('Quer continuar?: [S/N] ')).strip().upper()[0]
    if escolha != 'S' and escolha != 'N':
        while True:
            escolha = str(input('Opção inválida. Quer continuar?: [S/N] ')).strip().upper()[0]
            if escolha == 'S' or escolha == 'N':
                break
    if escolha == 'N':
        break
if cont18 == 1:
    print(f'Apenas {cont18} pessoa é maior de 18')
elif cont18 == 0:
    print(f'Ninguém é maior de 18')
else:
    print(f'{cont18} pessoas são maiores de 18')
if contH == 1:
    print(f'Apenas {contH} pessoa é um homem')
elif contH == 0:
    print('Não há homens')
else:
    print(f'{contH} pessoas são homens')
if contM20 == 1:
    print(f'Apenas {contM20} pessoa é uma mulher menor de 20 anos')
elif contM20 == 0:
    print(f'Não há mulheres menores de 20 anos')
else:
    print(f'{contM20} pessoas são mulheres menores de 20 anos')
