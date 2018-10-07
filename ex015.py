#Calcule o valor a pagar levando em consideração os dias de aluguel e km percorridos. O carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.
dias = int(input('Quantos dias alugados? '))
km = int(input('Quantos km rodados? '))
preço = (dias * 60) + (km * 0.15)
print ('O valor total do aluguel é de R${:.2f}'.format(preço))

