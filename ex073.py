'''Crie uma TUPLA preenchida com os 20 PRIMEIROS colocados da tabela do CAMPEONATO BRASILEIRO DE FUTEBOL na ordem de colocação, depois mostre:
A) os 5 primeiros
B) Os últimos 4 colocados
C) Times em ordem alfabética
D) Em que posição está o time do fluminense'''

times = ('palmeiras','flamengo', 'internacional','grêmio',
         'são paulo','atlético mg','cruzeiro', 'botafogo',
         'santos','bahia','fluminense', 'corinthians',
         'chapecoense','ceará', 'vasco', 'sport',
         'américa mg', 'vitória', 'paraná')
print('-=' * 30)
print(f'Lista de times do Brasileirão: {times}')
print('-=' * 30)
print(f'Os 5 primeiros são {times[0:5]}')
print('-=' * 30)
print(f'Os 4 últimos colocados são: {times[15:]}')
print('-=' * 30)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 30)
print(f'O fluminense está na {times.index("fluminense")+1}ª posição')
