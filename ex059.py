#Fazer um menu de opções, com entrada de dados de 2 valores, mostrar o resultado baseado nas opçoes escolhidas.

valor1 = int(input('Digite um número: '))
valor2 = int(input('Digite outro número: '))
print('====== ESCOLHA UMA DAS OPÇÕES ABAIXO ======')
opção = 0
while opção != 5:
    print('''    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA''')
    opção = int(input('>>>Qual é a sua opção? '))
    if opção == 1:
        soma = valor1 + valor2
        print('A soma entre {} e {} é de {}'.format(valor1, valor2, soma))
    elif opção == 2:
        multiplica = valor1 * valor2
        print('A multiplicação entre {} e {} é de {}'.format(valor1, valor2, multiplica))
    elif opção == 3:
        if valor1 > valor2:
            maior = valor1
        else:
            maior = valor2
        print('Entre {} e {}, o maior valor é {}'.format(valor1, valor2, maior))
    elif opção == 4:
        print('Digite novos valores')
        valor1 = int(input('Digite um número: '))
        valor2 = int(input('Digite outro número: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção inválida, tente novamente!')
    print('=-=' * 10)
print('Fim do programa, volte sempre!')
