import pygame
import winsound
import random
import os
import datetime
pygame.init()

tamanho = (900,520)
tela =  pygame.display.set_mode( tamanho )
pygame.display.set_caption("Space Marker")
clock = pygame.time.Clock()
space = pygame.image.load("space.png")
pygame.display.set_icon(space)

def jogo():
    branco = (255,255,255)
    preto = (0,0,0)
    fundo = pygame.image.load("fundospace.jpg")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        


        tela.blit(fundo, (0,0))

        pygame.display.flip()

        clock.tick(60)







jogo()