#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porçao inteira. Ex.número 6.127(O número inteiro é 6)
'''from math import trunc
num = float(input("Digite um número real: "))
print("O valor digitado foi {}, e sua porção inteira é {}".format(num, trunc(num)))'''

# Outra maneira de fazer, abaixo:
num = float(input("Digite um número real: "))
print("O valor digitado foi {}, e sua porção inteira é {}".format(num, int(num)))
