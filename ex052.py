#Números primos
num = int(input('Digite um número: '))
tot = 0
for c in range (1, num + 1):
    if num % c == 0:
        print('\033[33m', end=' ')
        tot = tot +1
    else:
        print('\33[31m', end=' ')
    print('{}'.format(c), end=" ")
print('\n\033[0m O número {} foi divisível {} vezes'.format(num, tot))
if tot == 2:
    print('Ele é primo')
else:
    print('Ele não é primo')

