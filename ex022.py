#Crie um programa que leia um nome ocmpleto e diga: Nome com todas as letras maiusculas e minusculas
#Quantas letras ao todo, sem espaços
#Qunatas letras tem o primeiro nome

nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando sem nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))



