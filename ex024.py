#Faça um programa que verifique se o texto começa com a palavra "Santo".
cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[0:5].upper() == 'SANTO')