valor = float(input('Qual o valor do imóvel? '))
salario = float(input('Qual é o seu salário? '))
tempo = int(input('Quantos anos de financiamento? '))
prestação = valor / (tempo * 12)
minimo = salario * 30 / 100
print('Para pagar um a casa de R${:.2f}, em {} anos, a prestação será de R${:.2f}'.format(valor, tempo, prestação), end=' ')
if prestação <= minimo:
    print('Empréstimo pode ser CONCEDIDO')
else:
    print('Empréstimo NEGADO!')