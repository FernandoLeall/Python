#Ler um angulo e mostrar seno, cosseno e tangente
from math import radians, sin, cos, tan
angulo = float(input("Digite o ângulo: "))
seno = sin(radians(angulo))#Não esquecer de passar para radianos para calculo de seno, cosseno e tangente.
print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
cosseno = cos(radians(angulo))
print('O ângulo de {} tem o COSENO de {:.2f}'.format(angulo, cosseno))
tan = tan(radians(angulo))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(angulo, tan))
