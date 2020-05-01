from time import sleep
numero1 = int(input('Digite um número inteiro: '))
numero2 = int(input('Digite outro número inteiro: '))
print('Analizando os números...')
sleep(1)
if numero1 > numero2:
    print('O primeiro número é maior que o segundo número')
elif numero1 < numero2:
    print('O segundo número é maior que o primeiro número')
else:
    print('Os dois números são iguais')
