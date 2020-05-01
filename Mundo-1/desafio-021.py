from pygame import mixer
cores = {'limpo': '\033[m',
         'roxo': '\033[1;35m'}
mixer.init()
mixer.music.load('Song of Storms (Ocarina of Time).mp3')
mixer.music.play()
input(f'{cores["roxo"]}Pressione ENTER para parar a música{cores["limpo"]}')

