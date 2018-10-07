from random import randint
from time import sleep
computador = randint(0, 5)
print('-=-' * 19)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 19)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS! VocÊ acertou em qual número eu pensei')
else:
    print('PERDEU! Eu pensei no número {} e não no {}'.format(computador, jogador))