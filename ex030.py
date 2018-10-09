#Faça um programa que leia um número inteiro e mostre na tela ele é PAR ou ÍMPAR.

numero = int(input('Me diga um número: '))
resultado = numero % 2
if resultado ==0:
    print('O número {} é PAR'.format(numero))
else:
    print('O número {} é ÍMPAR'.format(numero))
