# Importando funções e bibliotécas.
from random import randint
from time import sleep


# Definindo uma função que sorteia valores para uma lista.
def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        lista.append(randint(1, 10))
        print(lista[c], end=' ')
        sleep(0.3)
    print('PRONTO!')


# Definindo uma função que soma os valores pares de uma lista.
def somaPar(lista):
    somaPar = 0
    for v in lista:
        if v % 2 == 0:
            somaPar += v
    print(f'Somando os valores pares de {lista}, temos {somaPar}.')


# Programa principal - Criando a lista e testando as funções.
numero = list()
sorteia(numero)
somaPar(numero)
