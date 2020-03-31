cores = {'limpo': '\033[m',
         'vermelho': '\033[1;31m',
         'verde': '\033[1;32m',
         'azul': '\033[1;34m'}
frase = str(input('Digite uma frase: ')).strip().lower()
print(f'Quantas vezes aparece a letra A? {cores["vermelho"]}{frase.count("a")}{cores["limpo"]}')
print(f'Onde aparece a letra A pela primeira vez?: {cores["verde"]}{frase.find("a")+1}{cores["limpo"]}')
print(f'Onde aparece a letra A pela última vez?: {cores["azul"]}{frase.rfind("a")+1}{cores["limpo"]}')
