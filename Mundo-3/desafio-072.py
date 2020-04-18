numero = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',\
         'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito',\
         'dezenove', 'vinte'
escolha = -1
escolha2 = ''
while True:
    escolha = int(input('Digite um número entre 0 e 20: '))
    while escolha > len(numero) or escolha < 0:
        escolha = int(input('Digite um número entre 0 e 20: '))
    print(f'O número {escolha} em extenso é {numero[escolha]}')
    escolha2 = str(input('Quer continuar? [S/N]:')).strip().upper()[0]
    while escolha2 not in 'SN':
        escolha2 = str(input('Quer continuar? [S/N]:')).strip().upper()[0]
    if escolha2 == 'N':
        break
