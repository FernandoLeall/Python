#Crie um programa que leia quanto dinheiro a pessoa tem na carteira e mostre quantos dólares ela pode comprar.
#Considere o U$$1.00 = R$4.09

real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 4.09
print('Com R${:.2f} você compra U$${:.2f}'.format(real,dolar))


real = float(input('Quanto dinheiro você tem na carteira? R$'))
euro = real / 4.80
print('Com R${:.2f} você compra {:.2f}euros'.format(real, euro))


