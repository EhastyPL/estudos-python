
from random import randint
from time import sleep


jogo =  {
    'Jogador1': randint(1, 20),
    'Jogador2': randint(1, 20),
    'Jogador3': randint(1, 20),
    'Jogador4': randint(1, 20)} 
print("valores sorteados")
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep (0.25)
    if  v == 20 :
        print("critico")
        sleep(3)
    if v<15:
        print("dano fraco")
        sleep(3)
    elif v>15: 
        print("dano forte")
        sleep(3)
    else: 
        print("Fraco")
        