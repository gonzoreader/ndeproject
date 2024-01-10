#!/usr/bin/env python3

import pygame
import maps

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


def map2():
    pygame.draw.rect(screen, grey, pygame.Rect(0, 0, 10, 10))


current_level = 0
maps_data = [
    map1,
    map2,
    # Add more maps as needed
]

running = True

while running:
    screen.fill((119, 119, 119))

    mpos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                playerX_change = -1
            if event.key == pygame.K_d:
                playerX_change = 1
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

    if playerX <= -20:
        playerX = -20
    elif playerX >= 1839:
        playerX = 1839
        current_level = 1
    if playerY <= 5:
        playerY = 5
    elif playerY >= 1000:
        playerY = 1000

    player(playerX, playerY)

    current_map = maps_data[current_level]
    current_map()

    crosshair()
    pygame.display.update()
