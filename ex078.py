'''Faça um programa que leia 5 valores numéricos e guarde-os em um lista. No final, mostre qual foi o menor e o maior valor e em qual posição ele está posicionao'''
listanum = []
maior = 0
menor = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor na posição {c}: ')))
    if c == 0:
        maior = menor = listanum[c]
    else:
        if listanum[c] > maior:
            maior = listanum[c]
        if listanum[c] < menor:
            menor = listanum[c]
print('=-' * 30)
print(f'Você digitou os seguintes valores {listanum}')
print(f"O maior valor digitado foi {maior} nas posições ", end='')
for i, v in enumerate(listanum):
    if v == maior:
        print(f'{i}...', end='')
print(f'O menor valor digitado foi {menor} nas posições: ', end='')
for i, v in enumerate(listanum):
    if v == menor:
        print(f'{i}...', end='')
print()




