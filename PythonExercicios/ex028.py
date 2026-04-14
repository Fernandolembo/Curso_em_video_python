from random import randint
from time import sleep
computador = randint(0,5) # Faz o computador "PENSAR"
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
jogador = int(input('Em que numero eu pensei? ')) # Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print("PARABÉNS, você conseguiu me vencer!!!")
else:
    print(f"GANHEI, eu pensei no número {computador} e não {jogador}")
