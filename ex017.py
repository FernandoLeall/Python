#Faça um programa que leia o comprimento do cateto oposto e adjcente e calcule a hipotenusa.
from math import hypot #hypot, me da a fórmula pronta da hipotenusa
co = float(input('Qual o comprimento do cateto oposto: '))
ca = float(input('Qual o comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa mede {:.2f}'.format(hi))
