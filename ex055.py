#Faça um programa que leia o peso da 5 pessoas e mostre o maior e menor peso lidos
maior = 0
menor = 0
for pess in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(pess)))
    if pess ==1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso80
print('O maior peso lido foi de {}Kg'.format(maior))
print('O menor peso lido foi de {}Kg'.format(menor))