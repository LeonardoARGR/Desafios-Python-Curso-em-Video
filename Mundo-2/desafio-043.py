peso = float(input('Qual é o seu peso?: '))
altura = float(input('Qual é a sua altura?: '))
imc = peso / (altura * altura)
if imc < 18.5:
    print('Você está abaixo do peso')
elif 18.5 <= imc <= 25:
    print('Você tem o peso ideal')
elif 25 < imc <= 30:
    print('Você está no sobrepeso')
elif 30 < imc <= 40:
    print('Você está com obesidade')
else:
    print('Você está com obesidade mórbida')
