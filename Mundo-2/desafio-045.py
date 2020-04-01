from random import choice
from time import sleep
# Introdução e opções
print(f'{"-=-" * 7}JOKENPÔ{"-=-" * 7}')
print('''Olá, vamos jogar jokenpô? Se você não sabe com
funciona, vou te explicar rapidamente: você
escolhe pedra(1), papel(2), ou tesoura(3).
Pedra vence de tesoura, tesoura vence de papel
e papel vence de pedra. Simples não? Bom, agora
vamos começar!''')
print(f'{"-=-" * 16}')
print('''(1)- Pedra
(2)- Papel
(3)- Tesoura''')
# Comandos de determinação das opções do usuário e do bot
escolha = int(input('Qual você escolhe?: '))
botescolha = choice([1, 2, 3])
# Comandos para deixar o programa mais bem trabalhado
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(0.25)
# Comandos para quando o usuário ganha e que mostra a opção dele e a do bot (pedra, papel ou tesoura)
if escolha == 1 and botescolha == 3:
    print('''Parabéns! Você venceu! Eu escolhi tesoura e você
escolheu pedra.''')
elif escolha == 2 and botescolha == 1:
    print('''Parabéns! Você venceu! Eu escolhi pedra e você
escolheu papel''')
elif escolha == 3 and botescolha == 2:
    print('''Parabéns! Você venceu! Eu escolhi papel e você
escolheu tesoura''')
# Comando para quando ocorre empate
elif escolha == botescolha:
    print('''Empate! Nós dois escolhemos a mesma coisa''')
# Comandos para quando o usuário perde e que mostra a opção dele e a do bot (pedra, papel ou tesoura)
elif escolha == 3 and botescolha == 1:
    print('''Eu venci! Eu escolhi pedra e você escolheu
tesoura''')
elif escolha == 1 and botescolha == 2:
    print('''Eu venci! Eu escolhi papel e você escolheu
pedra''')
elif escolha == 2 and botescolha == 3:
    print('''Eu venci! Eu escolhi tesoura e você escolheu
papel''')
# Comando para quando o usuário escolhe algo que não está entre as opções
elif escolha <= 0 or escolha >= 4:
    print('''Esta opção não existe, tente novamente''')
print('-=-' * 16)
