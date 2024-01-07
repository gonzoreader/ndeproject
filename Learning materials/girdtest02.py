#!/usr/bin/env python3
import pygame
pygame.init()
# create a screen
#size = 500
screen = pygame.display.set_mode((600,600))
play = True

# color
c = (255,255,255)

# main loop
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
    for x in range(0,600,50):
        pygame.draw.line(screen,c,(1,x), (600,x), 2)
        pygame.draw.line(screen,c,(x,1), (x,600), 2)
        pygame.display.update()
