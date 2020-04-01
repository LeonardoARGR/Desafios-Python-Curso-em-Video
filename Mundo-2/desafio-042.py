from math import fabs
a = float(input('Primeira reta: '))
b = float(input('Segunda reta: '))
c = float(input('Terceira reta: '))
if fabs(a-b) < c < a + b and fabs(a-c) < b < a + c and fabs(b-c) < a < (b + c):
    print('Com estas retas, você consegue fazer um triângulo')
    if a == b == c:
        print('O triângulo formado é EQUILÁTERO')
    elif a != b != c != a:
        print('O triângulo formado é ESCALENO')
    else:
        print('O triângulo formado é ISÓSCELES')
else:
    print('Com estas retas, você não consegue fazer um triângulo')
