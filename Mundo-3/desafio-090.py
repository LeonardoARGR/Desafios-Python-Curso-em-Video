# Declarando e colocando os valores no dicionário.
aluno = dict()
aluno['Nome'] = str(input('Nome: ')).strip().title()
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))

# Calculando a situação do aluno.
if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'
elif 5 <= aluno['Média'] < 7:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado'
print('=' * 30)
# Mostrando as keys e seus valores na tela.
for k, v in aluno.items():
    print(f'{k} é igual a {v}')
