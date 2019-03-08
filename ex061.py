#Refazer o exercicio 51, lendo o primeiro termo e a razão de um PR, mostrando os 10 primeiros termos da programação usando WHILE.
print('Gerador de PA')
print('-='*10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} .'.format(termo), end='')
    termo += razão
    cont += 1
print('FIM')
