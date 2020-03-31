#As funções bin, oct e hex transformam o número escolhido em binário, octal e hexadecimal.
número = int(input('Digite um número inteiro: '))
print('Escolha o formato de conversão:\n1- Binário\n2- Octal\n3- Hexadecimal')
escolha = int(input('Qual a sua escolha?: '))
if escolha == 1:
    print(f'{número} em Binário é igual à {bin(número) [2:]}')
elif escolha == 2:
    print(f'{número} em Octal é igual à {oct(número) [2:]}')
elif escolha == 3:
    print(f'{número} em Hexadecimal é igual à {hex(número) [2:]}')
else:
    print('Desculpe, essa opção não existe')

