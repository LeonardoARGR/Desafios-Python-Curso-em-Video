import datetime
ano = int(input('Que ano o atleta nasceu?: '))
idade = datetime.date.today().year - ano
if 0 < idade <= 9:
    print('Atleta MIRIM')
elif 9 < idade <= 14:
    print('Atleta INFANTIL')
elif 14 < idade <= 19:
    print('Atleta JUNIOR')
elif idade == 20:
    print('Atleta SÊNIOR')
elif 20 < idade:
    print('Atleta MASTER')
