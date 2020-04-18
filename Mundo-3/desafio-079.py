print('=-=' * 20)
valores = list()
while True:
    valor = int(input('Digite um valor: '))
    if valor not in valores:
        valores.append(valor)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não vou adicionar')
    escolha = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if escolha not in 'SN':
        while escolha not in 'SN':
            escolha = str(input('Opção inválida. Quer continuar?: [S/N] ')).strip().upper()[0]
            if escolha in 'SN':
                break
    print('=-=' * 20)
    if escolha == 'N':
        break
print(f'Você digitou os valores {sorted(valores)}')
