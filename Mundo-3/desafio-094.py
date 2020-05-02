# 1- Declarando variáveis.
grupo_de_pessoas = list()
pessoa = dict()
escolha = ''
ultima_mulher = ''
soma_de_idades = 0

# 2- Adicionando valores ao dicionário "pessoa".
while True:
    print('-=-' * 30)
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: ')).strip().title()
    pessoa['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
    # 2.1- Fazendo com que "sexo" só possa receber "M" ou "F".
    if pessoa['sexo'] not in 'MF':
        while pessoa['sexo'] not in 'MF':
            pessoa['sexo'] = str(input('Opção inválida. Sexo: [M/F] ')).strip().upper()[0]
    pessoa['idade'] = int(input('Idade: '))
    # 2.2- Adicionando "pessoa" ao "grupo_de_pessoas".
    grupo_de_pessoas.append(pessoa.copy())

    # 3- Somando as idades.
    soma_de_idades += pessoa['idade']
    # 4- Pegando o nome da última mulher.
    if pessoa['sexo'] == 'F':
        ultima_mulher = pessoa['nome']

    # 5- Criando uma escolha entre continuar o programa ou não.
    escolha = str(input('Quer continuar?: [S/N] ')).strip().upper()[0]
    # 5.1- Fazendo com que "escolha" só possa receber "S" ou "N".
    if escolha not in 'SN':
        while escolha not in 'SN':
            escolha = str(input('Opção inválida. Quer continuar?: [S/N] ')).strip().upper()[0]
    # 5.2- Fechando o programa.
    if escolha == 'N':
        break

# 6- Mostrando resultados na tela.
print('-=-' * 30)
# 6.1- Mostrando a quantidade de pessoas registradas.
print(f'O grupo tem {len(grupo_de_pessoas)} pessoas.')

# 6.2- Mostrando a média de idade do grupo.
print(f'A média de idade do grupo é de {soma_de_idades / len(grupo_de_pessoas):.2f}.')

# 6.3- Mostrando as mulheres cadastradas.
print(f'As mulheres cadastradas foram ', end='')
for p in grupo_de_pessoas:
    if p['sexo'] == 'F':
        if p['nome'] == ultima_mulher:
            print(f'{p["nome"]}.')
        else:
            print(f'{p["nome"]}, ', end='')

# 6.4- Mostrando as pessoas com idade acima da média de idade.
print('Lista de pessoas acima da média:')
for p in grupo_de_pessoas:
    if p['idade'] > soma_de_idades / len(grupo_de_pessoas):
        print('   ->', end='')
        for k, v in p.items():
            print(f' {k.title()}: {v}', end='')
            if k != 'idade':
                print(';', end='')
        print('.')
print('-=-' * 30)
