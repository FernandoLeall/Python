while True:
    print('-'*30)
    n = int(input('Qual tabuada você quer ver? '))
    print('-'*30)
    if n < 0:
        break
    for c in range (1, 11):
        print(f'{n}X{c} = {n*c}')
    print('-'*30)
print('TABUADA ENCERRADA! VOLTE SEMPRE.')

