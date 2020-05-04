# Criando uma função que digita uma mensagem no meio de duas linhas.
def escreva(msg):
    # Fazendo com que a linha tenha um tamanho que se adapta a mensagem.
    print('~' * (len(msg)+4))
    print(f'  {msg}')
    print('~' * (len(msg)+4))


# Programa pricipal - Usando a função "escreva" na prática.
escreva('Gustavo Guanabara')
escreva('Curso de Python no YouTube')
escreva('CeV')
