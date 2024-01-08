#!/user/bin/env python3

# Importing Pygame
import pygame

# Initializing Pygame
pygame.init()

# Create the window
screen = pygame.display.set_mode((1920, 1080))

# Color variables to save time
black = (0, 0, 0)

# Title and Icon
pygame.display.set_caption("NDE Project")
icon = pygame.image.load('skeleton.png')
pygame.display.set_icon(icon)

# Defining a function that will create the grid and ui lines
def linesui():
    pygame.draw.line(screen, (black), (0,0), (0,1080), 6)
    pygame.draw.line(screen, (black), (1920,1080), (1920,0), 6)
    pygame.draw.line(screen, (black), (0,0), (1920,0), 6)
    pygame.draw.line(screen, (black), (0,1080), (1080,1920), 6)
    pygame.draw.line(screen, (black), (0,850), (1920, 850), 6)
    pygame.draw.line(screen, (black), (400,850), (400, 1080), 6)
    pygame.draw.line(screen, (black), (1000, 850), (1000, 1080), 6)
    for x in range(0, 850, 85):
        pygame.draw.line(screen, (black), (0,x), (1920,x), 5)
    for x in range(0, 1920, 120):
        pygame.draw.line(screen, (black), (x,0), (x,850), 5)

# Player
playerImg = pygame.image.load('player.png')
playerX = 10
playerY = 2

# Defining a player function so that i can call this code in my while loop
def player():
    screen.blit(playerImg, (playerX, playerY))

# Setting up the while loop with an always true variable
running = True

# Game loop
while running:
    # Changing the color of the window
    screen.fill((110, 110, 110))
    # Event for loop. Pygame uses events for mouse movement, key presses etc.
    # All events get passed through this loop so that they are executed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Calling the linesui function
    linesui()
    # Calling the player function
    player()
    # Updating the display every tick
    pygame.display.update()

