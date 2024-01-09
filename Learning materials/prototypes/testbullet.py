#!/usr/bin/env python3

# Importing Pygame
import pygame
import random

# Initializing Pygame
pygame.init()

# Create the window
screen = pygame.display.set_mode((1920, 1080))
screen_rect = screen.get_rect()

# Color variables to save time
BLACK = (0, 0, 0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
WHITE = (255,255,255)

# Title and Icon
pygame.display.set_caption("NDE Project")
icon = pygame.image.load('skeleton.png')
pygame.display.set_icon(icon)

# Hide mouse cursor
pygame.mouse.set_visible(False)

# creating player
player = pygame.Rect(screen_rect.centerx, screen_rect.bottom, 0, 0)
start = pygame.math.Vector2(player.center)
end = start
length = 50

SPEED = 5

all_bullets = []

# Crosshair
ch = pygame.image.load('crosshair.png')
def crosshair():
    screen.blit(ch, (mpos, mpos))





# Setting up the while loop with an always true variable
running = True
clock = pygame.time.Clock()

# Game loop
while running:
    # Changing the color of the window
    screen.fill((119, 221, 119))

    # tracking mouse pos
    mpos = pygame.mouse.get_pos()

    # Event for loop. Pygame uses events for mouse movement, key presses etc.
    # All events get passed through this loop so that they are executed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        
        if event.type == pygame.MOUSEMOTION:
            mouse = pygame.mouse.get_pos()
            end = start + (mouse -start).normalize() * length
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()

            distance = mouse - start
            position = pygame.math.Vector2(start)
            speed = distance.normalize() * SPEED

            all_bullets.append([position, speed])



    
        # Player movement 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                playerX_change = -0.5
            if event.key == pygame.K_d:
                playerX_change = 0.5
            if event.key == pygame.K_w:
                playerY_change = -0.5
            if event.key == pygame.K_s:
                playerY_change = 0.5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                playerX_change = 0
            if event.key == pygame.K_w or event.key == pygame.K_s:
                playerY_change = 0


    

    crosshair()
    # Updating the display every tick
    pygame.display.update()