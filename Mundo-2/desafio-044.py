preço = float(input('Qual o preço do produto?: '))
print('Escolha a forma de pagamento:')
print('''1- À vista com dinheiro/cheque (10% de desconto)
2- À vista no cartão (5% de desconto)
3- 2x no cartão (preço normal)
4- 3x ou mais no cartão (20% de juros)''')
escolha = int(input('Qual forma de pagamento você escolhe?: '))
if escolha == 1:
    print(f'O preço do produto à vista com dinheiro/cheque é de R${preço - (preço * 10 / 100)}')
elif escolha == 2:
    print(f'O preço do produto à vista no cartão é de R${preço - (preço * 5 / 100)}')
elif escolha == 3:
    print(f'O preço do produto dividido 2x no cartão não muda, ainda é R${preço}')
elif escolha == 4:
    print(f'O preço do produto dividido 3x ou mais no cartão é de R${preço + (preço * 20 / 100)}')
