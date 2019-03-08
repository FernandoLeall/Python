# ler vario numeros. O programa para quando o usuário digita 999. NO final diga quantos nomeros foram digitados e qual foi a soma entre eles
num = cont = soma = 0
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    soma = soma + num
    cont +=1
    num = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma entre eles foi {}.'.format(cont, soma))

