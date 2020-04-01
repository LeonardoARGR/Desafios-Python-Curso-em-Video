from datetime import date
ano = int(input('Que ano você nasceu?: '))
gênero = str(input('Você é homem ou mulher?: ')).strip().lower()
idade = date.today().year - ano
print(f'Em {date.today().year}, quem nasceu em {ano} tem {idade} anos')
if gênero == 'homem':
    if idade < 18:
        print(f'Você ainda vai se alistar no exército daqui a {18 - idade}, em {date.today().year + (18 - idade)}')
    elif idade > 18:
        if idade - 18 == 1:
            print(f'Você já se alistou ou já deveria ter se alistado em {date.today().year - (idade - 18)}, à {idade - 18} ano atrás')
        else:
            print(f'Você já se alistou ou já deveria ter se alistado em {date.today().year - (idade - 18)}, à {idade - 18} anos atrás')
    else:
        print('Você terá que se alistar ou se alistou este ano')
elif gênero == 'mulher':
    print('Você não precisa se alistar')
