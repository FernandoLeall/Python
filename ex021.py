#Crie um programa que toque uma música em mp3
import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()

#Não funcionou pelo pygame conforme ensinado pelo guanabara no exercício 21

