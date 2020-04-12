palavras = 'azul', 'macaco', 'banana', 'caracol', 'vidraça', 'chuva', 'vicio', 'python', 'xbox', \
           'controle'
for p in palavras:
    print(f'Na palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
    print('')
