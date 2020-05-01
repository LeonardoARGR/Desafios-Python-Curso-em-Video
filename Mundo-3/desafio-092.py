# Importando bibliotécas e funções.
from datetime import date

# Declarando o dicionário.
pessoa = dict()

# Adicionado valores ao dicionário.
pessoa['nome'] = str(input('Nome: ')).strip().title()
pessoa['idade'] = date.today().year - int(input('Ano de nascimento: '))
pessoa['ctps'] = int(input('Carteira de trabalho [0 não tem]: '))
# Analisando se a pessoa trabalha ou não.
if pessoa['ctps'] != 0:
    pessoa['contratação'] = int(input('Ano de contratação: '))
    pessoa['salário'] = float(input('Salário: R$'))
    pessoa['aposentadoria'] = (35 - (date.today().year - pessoa['contratação']) + pessoa['idade'])

# Mostrando os valores na tela
print('=' * 30)
for k, v in pessoa.items():
    print(f'{k.title()} tem o valor {v}')
