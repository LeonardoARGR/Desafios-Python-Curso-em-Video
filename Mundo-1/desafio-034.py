cores = {'limpo': '\033[m',
         'verde': '\033[1;32m',
         'azul': '\033[1;34m'}
s = float(input('Qual o salário do funcionário?: R$'))
if s > 1250:
    aumento = s + (s * 10 / 100)
    print(f'Com o aumento de {cores["azul"]}10%{cores["limpo"]}, o novo salário do funcionário é de {cores["azul"]}R${aumento :.2f}{cores["limpo"]}')
else:
    aumento = s + (s * 15 / 100)
    print(f'Com o aumento de {cores["verde"]}15%{cores["limpo"]}, o novo salário do funcionário é de {cores["verde"]}R${aumento :.2f}{cores["limpo"]}')
