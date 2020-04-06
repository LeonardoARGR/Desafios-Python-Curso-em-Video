sexo = str(input('Qual é o seu sexo?: [F/M] ')).upper().strip()[0]
while sexo != 'F' and sexo != 'M':
    sexo = str(input('Dados inválidos. Por favor, informe o seu sexo: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso')
