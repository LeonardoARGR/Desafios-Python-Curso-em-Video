print(f'{"=-=" * 10}[ LOJA GAFANHOTOS ]{"=-=" * 10}')
print('Bem vindo a LOJA GAFANHOTOS! Aqui temos vários produtos, então espero que goste!')
cont = totalgasto = barato = produtos1000 = 0
nomebarato = ''
while True:
    cont += 1
    print(f'{"=-=" * 10}=-[ {cont}° PRODUTO ]-={"=-=" * 10}=')
    produto = str(input('Qual é o nome do produto?: ')).strip()
    preçodoproduto = float(input('Qual é o preço do produto: R$'))
    escolha = str(input('Quer continuar comprando?[S/N]: ')).strip().upper()[0]
    totalgasto += preçodoproduto
    if cont == 1 or preçodoproduto < barato:
        barato = preçodoproduto
        nomebarato = produto
    if preçodoproduto > 1000:
        produtos1000 += 1
    if escolha != 'S' and escolha != 'N':
        while True:
            escolha = str(input('Esta opção não existe. Quer continuar comprando?[S/N]: ')).strip().upper()[0]
            if escolha == 'S' or escolha == 'N':
                break
    if escolha == 'N':
        break
print(f'{"=-=" * 10}=-[ FINALIZAÇÃO ]-={"=-=" * 10}')
print(f'Total gasto na compra: R${totalgasto :.2f}')
print(f'Produtos que custam mais de R$1000.00: {produtos1000}')
print(f'Produto mais barato: {nomebarato}')
print(f'Preço do {nomebarato}: {barato}')
print(f'{"=-=" * 26}=')
