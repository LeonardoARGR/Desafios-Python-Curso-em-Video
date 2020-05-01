valordacasa = float(input('Qual é o valor da casa?: R$'))
salário = float(input('Qual o seu salário?: R$'))
anos = int(input('Por quantos anos você vai pagar a casa?: '))
print(f'Para pagar uma casa de R${valordacasa :.2f} em {anos} anos, a prestação mensal será de R${valordacasa / anos / 12 :.2f}')
if valordacasa / anos / 12 > salário * 30 / 100:
    print(f'Desculpe, mas você não pode financiar essa casa, emprestimo NEGADO.')
elif valordacasa / anos / 12 <= salário * 30 / 100:
    print(f'Você pode financiar a casa, emprestimo APROVADO.')
