#!/usr/bin/env python3

# Importing Pygame
import pygame
import maps

# Initializing Pygame
pygame.init()

# Create the window
screen = pygame.display.set_mode((1920, 1080))

# Color variables to save time
black = (0, 0, 0)
grey = (80,80,80)
# Title and Icon
pygame.display.set_caption("NDE Project")
icon = pygame.image.load('skeleton.png')
pygame.display.set_icon(icon)

# Hide mouse cursor
pygame.mouse.set_visible(False)

# Player
playerImg = pygame.image.load('player.png')
playerX = 81
playerY = 549
playerX_change = 0
playerY_change = 0

# Crosshair
ch = pygame.image.load('crosshair.png')
def crosshair():
    screen.blit(ch, (mpos, mpos))

# Defining a player function so that i can call this code in my while loop.
def player(x,y):
    screen.blit(playerImg, (x, y))

# Defining an npc
def bill(x,y):
    screen.blit(npcImg, (billX,billY))

# Setting up the while loop with an always true variable
running = True

# Game loop
while running:
    # Changing the color of the window
    screen.fill((119,119,119))
    maps.map1()
    # tracking mouse pos
    mpos = pygame.mouse.get_pos()
    print(mpos)
    # Event for loop. Pygame uses events for mouse movement, key presses etc.
    # All events get passed through this loop so that they are executed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
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


    
    
    # player function and movement
    playerY += playerY_change
    playerX += playerX_change
    # These two if statements prevent the player from going off screen 
    if playerX <= -20:
        playerX = -20
    elif playerX >= 1840:
        playerX = 1840
    if playerY <= 5:
        playerY = 5
    elif playerY >= 1000:
        playerY = 1000
    player(playerX,playerY)
    crosshair()
    # Updating the display every tick
    pygame.display.update()