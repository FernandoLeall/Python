#Melhorar o jogo do desafio 28 onde o cumputador var pensar em um número entre 0 e 10. Mas, agora o jogador vai tentar adivinhar até acertar.
from random import randint
computador = randint(0, 10)
print('Sou o seu computador, acabei de pensar em um número de 0 a 10.')
print('Será que você consegue advinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('MAIS...Tente mais uma vez.')
        elif jogador > computador:
            print('MENOS...Tente mais uma vez.')
print('Parabéns, você acertou com {} tentativas!'.format(palpites))



