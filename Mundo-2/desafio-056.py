médiaidade = 0
maioridadehomem = 0
nomevelho = ''
mulheresmaisnovas = 0
for p in range(1, 5):
    print(f'{"=" * 9}{p}ª Pessoa{"=" * 9}')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [H/M]: ')).strip().upper()
    médiaidade += idade
    if p == 1 and sexo == 'H':
        maioridadehomem = idade
        nomevelho = nome
    if sexo == 'H' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo == 'M' and 0 < idade < 20:
        mulheresmaisnovas += 1
print(f'A média de idade deste grupo é de {médiaidade / 4 :.1f}')
print(f'O homem mais velho é o {nomevelho}, e ele tem {maioridadehomem} anos')
print(f'Nesse grupo temos {mulheresmaisnovas} mulheres com menos de 20 anos')
