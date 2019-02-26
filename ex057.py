#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'm' ou 'f'. Caso esteja errado, digite novamente qté acertar a resposta.
sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo corretamente')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))
