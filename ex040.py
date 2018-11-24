#Escreva um programa que calcule a média do aluno e mostre se ele foi aprovado ou reprovado.

n1 = float(input('Qua a nota da primeira prova? '))
n2 = float(input('Qual a nota da segunda prova? '))
média = (n1 + n2) / 2
if média < 5:
    print('A média do aluno foi {}, portanto ele foi REPROVADO'.format(média))
elif média > 7:
    print('A média do aluno foi de {}, portanto ele foi APROVADO'.format(média))
else:
    print('A média do aluno foi de {}, portanto ele vai para a RECUPERAÇÃO'.format(média))


