cont = ('zero', 'um', 'dois', 'três', 'quatro',
        'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
        'onze','doze', 'treze', 'quatorze', 'quinze',
        'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um número de 0 a 20: '))
    if 0 <= num <= 20:
        break
    print('Essa resposta não é válida, tente novamente!')
print(f'Você digitou o número {cont[num]}')
while True:
    continua = str(input('Você quer continuar? [S/N]')).strip().upper()[0]
    if 0 <= num <= 20:
        if continua == 'S':
            num = int(input('Digite um número de 0 a 20: '))
        else:
            break
    print(f'Você digitou o número {cont[num]}')
print('FIM DO PROGRAMA, Obrigado por participar!')



