cores = {'limpo': '\033[m',
         'vermelho': '\033[1;31m',
         'verde': '\033[1;32m'}
a = int(input('Primeiro número: '))
b = int(input('Segundo número: '))
c = int(input('Terceiro número: '))
# Eu coloco o A como maior e menor sempre, mas se o B ou o C forem menor, os if vão colocar
# eles como menor ou maior
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'O {cores["verde"]}maior{cores["limpo"]} número é o {cores["verde"]}{maior}{cores["limpo"]}\nO {cores["vermelho"]}menor{cores["limpo"]} número é o {cores["vermelho"]}{menor}{cores["limpo"]}')
