preço = float(input('Qual o preço do produto ou das compras?: '))
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
    print(f'O preço do produto dividido 2x no cartão não muda, ainda é R${preço} com parcelas de R${preço / 2}')
elif escolha == 4:
    parcelas = int(input('Quantas parcelas?: '))
    print(f'''O preço do produto dividido em {parcelas}x no cartão é de R${preço + (preço * 20 / 100) :.2f},
e as parcelas irão custar R${(preço + (preço * 20 / 100)) / parcelas :.2f}''')
else:
    print('Esta opção de pagamento não existe')
