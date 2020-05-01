cores = {'limpo': '\033[m',
         'vermelho': '\033[1;31m',
         'verde': '\033[1;32m'}
v = float(input('Velocidade do carro: '))
if v > 80:
    print(f'Parado, você foi {cores["vermelho"]}multado{cores["limpo"]}')
    multa = (v - 80) * 7
    print(f'O valor da multa é de R${multa :.2f}')
print(f'Tenha um bom dia! {cores["verde"]}Dirija com segurança!{cores["limpo"]}')

