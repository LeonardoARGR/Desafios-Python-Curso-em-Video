frase = str(input('Digite uma frase: ')).strip().lower()
fraseseparada = frase.split()
frasejunta = ''.join(fraseseparada)
inverso = ''
for letra in range(len(frasejunta) - 1, -1, -1):
    inverso += frasejunta[letra]
print(f'O inverso de {frasejunta} é {inverso}')
if frasejunta == inverso:
    print('A frase é um palíndromo')
else:
    print('A frase não é palíndromo')
