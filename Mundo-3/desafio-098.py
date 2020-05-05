# Importando a função sleep.
from time import sleep


# Criando a função "contador".
def contador(inicio, fim, passo):
    print('-=' * 20)
    # Explicação do código abaixo: eu criei uma forma de converter o sinal do
    # "passo" quando ele for digitado com o sinal errado, corrigindo possíveis
    # bugs. Por exemplo: se eu fizer uma contagem do 1 até o 10, só que de -1
    # em -1, o programa vai identificar este erro e vai converter de -1 para 1.

    # Conversão para positivo.
    if inicio < fim:
        # Trocando 0 por 1.
        if passo == 0:
            print(f'Contagem de {inicio} até {fim} de 1 em 1')
            sleep(2.5)
            for n in range(inicio, fim + 1, 1):
                print(n, end=' ')
                sleep(0.3)
            print('FIM!')
        elif passo < 0:
            print(f'Contagem de {inicio} até {fim} de {-passo} em {-passo}')
            sleep(2.5)
            for n in range(inicio, fim + 1, -passo):
                print(n, end=' ')
                sleep(0.3)
            print('FIM!')
        else:
            print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
            sleep(2.5)
            for n in range(inicio, fim + 1, passo):
                print(n, end=' ')
                sleep(0.3)
            print('FIM!')

    # Conversão para negativo.
    elif inicio > fim:
        # Trocando o 0 por -1.
        if passo == 0:
            print(f'Contagem de {inicio} até {fim} de 1 em 1')
            sleep(2.5)
            for n in range(inicio, fim - 1, -1):
                print(n, end=' ')
                sleep(0.3)
            print('FIM!')
        elif passo > 0:
            print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
            sleep(2.5)
            for n in range(inicio, fim - 1, -passo):
                print(n, end=' ')
                sleep(0.3)
            print('FIM!')
        else:
            print(f'Contagem de {inicio} até {fim} de {-passo} em {-passo}')
            sleep(2.5)
            for n in range(inicio, fim - 1, passo):
                print(n, end=' ')
                sleep(0.3)
            print('FIM!')


# Programa principal: mostrando algumas contagens e uma contagem personalizada.
contador(1, 10, 1)
contador(10, 0, -2)
print('-=' * 20)
print('Agora é a sua vez de personalizar a contagem!')
contador(int(input('Início: ')), int(input('Fim: ')), int(input('Passo: ')))
