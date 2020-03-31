from math import fabs
a = float(input('Primeira reta: '))
b = float(input('Segunda reta: '))
c = float(input('Terceira reta: '))
if fabs(a-b) < c < a + b and fabs(a-c) < b < a + c and fabs(b-c) < a < (b + c):
    print('Com estas retas, você consegue fazer um triângulo')
    if a == b and b == c:
        print('O triângulo formado é EQUILÁTERO')
    elif a == b and a != c or c == b and c != a or c == a and c != b:
        print('O triângulo formado é ISÓSCELES')
    elif a != b and a != c and c != b:
        print('O triângulo formado é ESCALENO')
else:
    print('Com estas retas, você não consegue fazer um triângulo')
