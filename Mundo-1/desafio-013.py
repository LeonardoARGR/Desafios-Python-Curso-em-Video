cores = {'limpo': '\033[m',
         'azul': '\033[1;34m',
         'ciano': '\033[1;36m'}
s = float(input('Salário do funcionário: R$'))
sa = s + (s * 15 / 100)
print(f'Ao receber um aumento de {cores["azul"]}R${s * 15 / 100 :.2f}{cores["limpo"]}, o novo salário do funcionário é de {cores["ciano"]}R${sa :.2f}{cores["limpo"]}')
