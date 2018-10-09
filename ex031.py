#Perguntar a distância de uma viagem em km e calcular o preço da passagem, cobrando R$ 0,50 por km para viagens de até 200km e R$ 0,45 para viagens mais longas.

distância = int(input('Qual a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}km'.format(distância))
if distância <= 200:
    preço = distância * 0.50
    print('Sua viagem custará R$ {:.2f}'.format(preço))
else:
    preço = distância * 0.45
    print('Sua viagem custará R$ {:.2f}'.format(preço))
