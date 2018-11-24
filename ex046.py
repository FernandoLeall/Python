#Faça contagem regreesiva de 10 a 0 com pausa de 1 segundo
from time import sleep
for cont in range(10, -1, -1):
    print(cont)
    sleep(0.5)
print('BUM BUM POWWWW')

