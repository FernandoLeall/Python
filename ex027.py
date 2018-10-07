#Faça um programa que leia um nome completo, e mostre o primeiro e último nome separadamento
n = str(input('Digite sem nome completo: ')).strip()
nome = n.split()
print('Muito prazer me te conhecer!')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))



