from time import sleep
print(f'{"-=-" * 7}[CONTAGEM REGRESSIVA]{"-=-" * 7}')
print('''Vai estourar os fogos de artifício daqui a 10 segundos,
vamos começar a contar!''')
sleep(1)
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('BOOM! POOW! BOOM!')
print('AEEEEEE! OS FOGOS ESTOURARAM!!')
print('-=-' * 20)
