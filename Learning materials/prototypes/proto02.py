#!/usr/bin/env python3
import pygame
pygame.init()


### CONSTANTS ###
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)

RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000

SPEED = 5

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

playerX = 500
playerY = 900
playerX_change = 0
playerY_change = 0
player = pygame.Rect(playerX, playerY, 10, 10)
start = pygame.math.Vector2(player.center)
end = start
length = 50



all_bullets = []

clock = pygame.time.Clock()
running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_a:
                playerX_change = -0.5
            elif event.key == pygame.K_d:
                playerX_change = 0.5
            elif event.key == pygame.K_w:
                playerY_change = -0.5
            elif event.key == pygame.K_s:
                playerY_change = 0.5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                playerX_change = 0
            if event.key == pygame.K_w or event.key == pygame.K_s:
                playerY_change = 0

        elif event.type == pygame.MOUSEMOTION:
            mouse = pygame.mouse.get_pos()
            end = start + (mouse - start).normalize() * length
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()

            distance = mouse - start

            position = pygame.math.Vector2(start) # duplicate # start position in start of canon
            #position = pygame.math.Vector2(end)   # duplicate # start position in end of canon
            speed = distance.normalize() * SPEED
            
            all_bullets.append([position, speed])
        
    for position, speed in all_bullets:
        position += speed

    
    screen.fill(WHITE)

    pygame.draw.line(screen, RED, start, end)

    for position, speed in all_bullets:
        # need to convert `float` to `int` because `screen` use only `int` values
        pos_x = int(position.x)
        pos_y = int(position.y)
        pygame.draw.line(screen, (0,255,0), (pos_x, pos_y), (pos_x, pos_y))
    playerY += playerY_change
    playerX += playerX_change    
    pygame.display.update()

    # --- FPS ---

    clock.tick(25)

# --- the end ---

pygame.quit()
            
