cores = {'limpo': '\033[m',
         'vermelho': '\033[1;31m',
         'verde': '\033[1;32m'}
cidade = str(input('Qual a sua cidade?: ')).strip().lower().split()
if not 'santo' in cidade[0]:
    print(f'O nome da cidade começa com a palavra "Santo"?: {cores["vermelho"]}{"santo" in cidade[0]}{cores["limpo"]}')
else:
    print(f'O nome da cidade começa com a palavra "Santo"?: {cores["verde"]}{"santo" in cidade[0]}{cores["limpo"]}')
