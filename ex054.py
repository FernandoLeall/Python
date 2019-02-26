#Crie um programa que leia o ano de nascimento de 7 pessoas. No final, diga quantas pessoas são maiores e menores de iddade.
from datetime import date
atual=date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(pess)))
    idade = atual - nasc
    print('Essa pessoa tem {}'.format(idade))
    if idade >= 18:
        totmaior +=1
    else:
        totmenor +=1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('Ao todo tivemos {} pessoas menores de idade'.format(totmenor))


