cores = {'limpo': '\033[m',
         'vermelho': '\033[31m',
         'verde': '\033[32m',
         'amarelo': '\033[33m',
         'azul': '\033[34m',
         'roxo': '\033[35m',
         'ciano': '\033[36m'}
m = float(input('Metro: '))
km = m/1000
hm = m/100
dam = m/10
dm = m*10
cm = m*100
mm = m*1000
print('{}{}km{}\n{}{}hm{}\n{}{}dam{}\n{}{}dm{}\n{}{}cm{}\n{}{}mm{}'.format(cores['vermelho'], km, cores['limpo'], cores['verde'], hm, cores['limpo'], cores['amarelo'], dam, cores['limpo'], cores['azul'], dm, cores['limpo'], cores['roxo'], cm, cores['limpo'], cores['ciano'], mm, cores['limpo']))
