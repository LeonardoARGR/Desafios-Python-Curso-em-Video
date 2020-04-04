from datetime import date
anoatual = date.today().year
menores = 0
maiores = 0
for c in range(1, 8):
    ano = int(input(f'Em que ano a {c}ª pessoa nasceu?: '))
    idade = anoatual - ano
    if idade >= 21:
        maiores += 1
    else:
        menores += 1
print(f'''Nesse grupo de pessoas tem {maiores} pessoas que atingiram a 
maioridade e {menores} que ainda vão atingir a maioridade''')
