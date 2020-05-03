# Definindo uma função para calcular a área de um terreno retangular.
def area(l, c):
    print(f'A área de um terreno {l:.1f}x{c:.1f} é de {l*c:.1f}m².')


# Programa principal - Pedindo a largura e a altura como parâmetros para a função area().
print(f'{" CONTROLE DE TERRENOS ":=^45}')
area(float(input('Largura (m): ')), float(input('Comprimento (m): ')))
print('=' * 45)
