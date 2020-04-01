nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
notafinal = (nota1 + nota2) / 2
print(f'Com estas notas, a média do(a) aluno(a) é {notafinal :.1f}')
if notafinal < 5.0:
    print('O(a) aluno(a) foi REPROVADO(a)')
elif 5.0 <= notafinal <= 6.9:
    print('O(a) aluno(a) ficou de RECUPERAÇÃO')
elif notafinal >= 7.0:
    print('O(a) aluno(a) foi APROVADO(a)')
