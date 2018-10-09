#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre a mensagem dizendo que foi multado. A multa custará R$7 por cada km acima do limite.

velocidade = float(input('Qual a velocidade do carro?'))
if velocidade > 80:
    print('MULTADO! Você excedeu o limite de 80km/h')
    multa = (velocidade-80) * 7
    print('Por ultrapassar o limite de 80km/h, você foi multado em R$ {:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com segurança')


