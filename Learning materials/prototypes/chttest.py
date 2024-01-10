#!/usr/bin/env python3

import pygame

pygame.init()

screen = pygame.display.set_mode((1920, 1080))
black = (0, 0, 0)
grey = (80, 80, 80)
pygame.display.set_caption("NDE Project")
icon = pygame.image.load('skeleton.png')
pygame.display.set_icon(icon)
pygame.mouse.set_visible(False)

playerImg = pygame.image.load('player.png')
playerX = 81
playerY = 549
playerX_change = 0
playerY_change = 0

ch = pygame.image.load('crosshair.png')


def crosshair():
    screen.blit(ch, (mpos, mpos))


def player(x, y):
    screen.blit(playerImg, (x, y))


def map1():
    pygame.draw.rect(screen, grey, pygame.Rect(0, 0, 1920, 400))
    pygame.draw.rect(screen, grey, pygame.Rect(0, 680, 1920, 400))
    pygame.draw.line(screen, grey, (0, 0), (0, 1080), 100)


def map2T():
    pygame.draw.rect(screen, grey, pygame.Rect(0, 0, 700, 400))
    pygame.draw.rect(screen, (grey), pygame.Rect(900, 0, 1230, 400))
    pygame.draw.rect(screen, grey, pygame.Rect(0, 680, 1920, 400))


current_level = 0
maps_data = [
    map1,
    map2T,
    # Add more maps as needed
]

running = True

while running:
    screen.fill((119, 119, 119))

    mpos = pygame.mouse.get_pos()
    print(mpos)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                playerX_change = -1
            if event.key == pygame.K_d:
                playerX_change = 2
            if event.key == pygame.K_w:
                playerY_change = -1
            if event.key == pygame.K_s:
                playerY_change = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                playerX_change = 0
            if event.key == pygame.K_w or event.key == pygame.K_s:
                playerY_change = 0
    #if playerX >= 1839:





    playerY += playerY_change
    playerX += playerX_change
    # second map collision
    if current_level == 1:
        if playerX >= 1839:
            playerX = 30
            current_level = 2
        elif playerY >= 630:
            playerY = 630
        if playerY <= 400 and playerX <= 690:
            playerY = 400
        if playerX <= 700 and playerY <= 390:
            playerX = 700
        if playerX >= 890 and playerY <= 400:
            playerY = 400
        if playerY <= 390 and playerX >= 877:
            playerX = 877
        if playerX <= 5:
            current_level = 0
            playerX = 1899
    # first map collision
    if current_level == 0:
        if playerX <= 51:
            playerX = 51
        elif playerX >= 1900:
            playerX = 10
            current_level = 1
        if playerY <= 401:
            playerY = 401
        elif playerY >= 630:
            playerY = 630

    player(playerX, playerY)

    current_map = maps_data[current_level]
    current_map()

    crosshair()
    pygame.display.update()
