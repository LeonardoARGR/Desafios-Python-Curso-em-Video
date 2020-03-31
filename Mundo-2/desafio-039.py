ano = int(input('Que ano você nasceu?: '))
idade = 2020 - ano
print(f'Em 2020, quem nasceu em {ano} tem {idade} anos')
if idade < 18:
    print(f'Você ainda vai se alistar no exército daqui a {18 - idade}, em {2020 + (18 - idade)}')
elif idade > 18:
    print(f'Você já se alistou ou já deveria ter se alistado em {2020 - (idade - 18)}, à {idade - 18} anos atrás')
elif idade == 18:
    print('Você terá que se alistar ou se alistou este ano')
