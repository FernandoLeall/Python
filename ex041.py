#Leia o ano de nascimento do atleta e identifique em qual categoria ele se classifica, mirim, infantil,junior, senior e master.
from datetime import date
atual = date.today().year
nasc = int(input('Qual o ano de nascimento do atleta? '))
idade = atual - nasc
print('O ano de nascimento do atleta é {}, ele tem {} anos!'.format(nasc, idade))
if idade <= 9:
    print('Ele é um atleta MIRIM)')
elif idade <=14:
    print('Ele é um atleta INFANTIL')
elif idade <=19:
    print('Ele é um atleta JUNIOR')
elif idade <=25:
    print('Ele é um atleta SÊNIOR')
else:
    print('Ele é um atleta MASTER')


