#Crie um programa que verifique se há "Silva" no nome de uma pessoa
nome = str(input('Digite o seu nome: ')).strip()
print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))


