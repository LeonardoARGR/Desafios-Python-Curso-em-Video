# Importando funções e bibliotécas.
from time import sleep


# Definindo a função "maior" sem usar tupla, listas ou dicionários.
def maior(*num):
    print('-=' * 30)
    print('Analizando os valores passados...')
    # Criando uma variável para pegar o maior valor.
    maior = cont = 0
    for n in num:
        print(n, end=' ')
        sleep(0.3)
        if cont == 0:
            maior = n
        else:
            if n > maior:
                maior = n
        cont += 1
    print(f'Foram digitados {len(num)} valores ao todo.')
    print(f'O maior valor foi o {maior}')


# Programa principal - Testando a função "maior".
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
