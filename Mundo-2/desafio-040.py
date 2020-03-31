nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
notafinal = (nota1 + nota2) / 2
if notafinal < 5.0:
    print('O aluno foi REPROVADO')
elif 5.0 <= notafinal <= 6.9:
    print('O aluno ficou de RECUPERAÇÃO')
elif notafinal >= 7.0:
    print('O aluno foi APROVADO')
