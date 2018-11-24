#Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela a
#seguinte mensagem: - O primeiro valor é MAIOR/ - O segundo valor é MAIOR/ - Não existe valor maior, os dois são iguais.

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
if n1 < n2:
    print('O primeiro número {} é MENOR que o segundo número {}'.format(n1, n2))
elif n1 > n2:
    print('O primeiro número {} é MAIOR que o segundo número {}'.format(n1, n2))
else:
    print('Não existe valor MAIOR ou MENOR, ambos são iguais!!')
