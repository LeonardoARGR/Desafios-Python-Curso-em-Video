expressao = str(input('Digite um expressão numérica: '))
if expressao.count('(') == expressao.count(')'):
    print('Sua expressão está certa')
else:
    print('Sua expressão está errada')
