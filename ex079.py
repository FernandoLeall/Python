'''Crie um programa onde o usuário deve colocar vário valore numéricos e cadastre-os em uma lista. caso o numero já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados em ordem crescente'''
números = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in números:
        números.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    r = str(input('Quer conrinuar?[S/N] '))
    if r in 'Nn':
        break
print('-=' * 30)
números.sort()
print(f'Você digitou os valores {números}')


