import pygame
import winsound
import random
import os
import datetime
from tkinter import simpledialog
import tkinter as tk
from tkinter import messagebox
pygame.init()

tamanho = (900,520)
tela =  pygame.display.set_mode( tamanho )
pygame.display.set_caption("Space Marker")
clock = pygame.time.Clock()
space = pygame.image.load("space.png")
pygame.display.set_icon(space)

estrelas = []

def abrir_caixa_de_pergunta(posicao):
    root = tk.Tk()
    root.withdraw()
    resposta = simpledialog.askstring("Pergunta", "Qual é o nome da estrela? \nCaso não saiba clique em Cancel")
    if resposta is None or resposta.strip() == "":
        resposta = "desconhecido"
    resposta += f" ({posicao[0]}, {posicao[1]})"
    estrelas.append((posicao, resposta))

def desenhar_estrelas():
    for posicao, nome in estrelas:
        pygame.draw.circle(tela, (255, 255, 255), posicao, 5)
        fonte = pygame.font.Font(None, 20)
        texto = fonte.render(nome, True, (255, 255, 255))
        tela.blit(texto, (posicao[0] + 10, posicao[1] - 10))

def salvar_pontos_arquivo():
    with open("pontos.txt", "w") as arquivo:
        for posicao, nome in estrelas:
            arquivo.write(f"{posicao[0]},{posicao[1]},{nome}\n")


def desenhar_linhas():
    if len(estrelas) >= 2:
        for i in range(len(estrelas) - 1):
            pygame.draw.line(tela, (255, 255, 255), estrelas[i][0], estrelas[i+1][0], 2)



def jogo():
    branco = (255,255,255)
    preto = (0,0,0)
    fundo = pygame.image.load("fundospace.jpg")
    running = True
    pygame.mixer.music.load("Space_Machine_Power.mp3")
    pygame.mixer.music.play(-1)
    fonte = pygame.font.Font(None, 20)
    texto1 = "Pressione F10 para Salvar os pontos"
    texto_renderizado = fonte.render(texto1, True, branco)
    posicao_texto = (260 // 2 - texto_renderizado.get_width() // 2, 15 // 2 - texto_renderizado.get_height() // 2)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: 
                    abrir_caixa_de_pergunta(event.pos)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F10:
                    salvar_pontos_arquivo()
        


        tela.blit(fundo, (0,0))
        desenhar_linhas()
        desenhar_estrelas()
        tela.blit(texto_renderizado, posicao_texto)
        pygame.display.flip()
        clock.tick(60)







jogo()