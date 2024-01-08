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
#    for x in range(0, 850, 85):
#        pygame.draw.line(screen, (black), (0,x), (1920,x), 5)
#    for x in range(0, 1920, 120):
#        pygame.draw.line(screen, (black), (x,0), (x,850), 5)

# Player
playerImg = pygame.image.load('player.png')
playerX = 10
playerY = 2
playerX_change = 0
playerY_change = 0
# Npc 
npcImg = pygame.image.load('bill.png')
billX = 40
billY = 2


# Defining a player function so that i can call this code in my while loop.
def player(x,y):
    screen.blit(playerImg, (x, y))

# Attempting to make an npc
def bill():
    screen.blit(npcImg, (billX,billY))

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
    
        # Player movement 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.4
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.4
            if event.key == pygame.K_UP:
                playerY_change = -0.4
            if event.key == pygame.K_DOWN:
                playerY_change = 0.4
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0


    
    # Calling the linesui function
    linesui()
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
    elif playerY >= 770:
        playerY = 770
    player(playerX,playerY)
    bill()
    # Updating the display every tick
    pygame.display.update()

