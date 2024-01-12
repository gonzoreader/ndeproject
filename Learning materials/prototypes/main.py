#!/usr/bin/env python3

import pygame
import logging

pygame.init()

# Initialize the logging module
logging.basicConfig(filename='game_log.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

black = (0, 0, 0)
grey = (80, 80, 80)
game_over = False
font = pygame.font.Font('Grand9K Pixel.ttf', 36)
# creating the screen
screen = pygame.display.set_mode((1920, 1080))
# setting the caption and icon
pygame.display.set_caption("NDE Project")
icon = pygame.image.load('skeleton.png')
pygame.display.set_icon(icon)
# hiding the mouse so I can implement a cursor
pygame.mouse.set_visible(False)
# loading in the sword to be blitted
swordImg = pygame.image.load('sword.png')
# loading in the key to be blitted
keyImg = pygame.image.load('key.png')
# loading in the monster to be blitted
monsterImg = pygame.image.load('monster.png')
bloodImg = pygame.image.load('blood.png')
# loading in the player to be blitted
playerImg = pygame.image.load('player.png')
playerswImg = pygame.image.load('playersw.png')
playerX = 81
playerY = 549
playerX_change = 0
playerY_change = 0
monsterX = 1200
monsterY = 550
monster_speed = 0.6
keyX = 1400
keyY = 550
key_collected = False
swordX = 800
swordY = 800
sword_collected = False
# loading in the cursor
ch = pygame.image.load('crosshair.png')

# defining a function that allows me to display text onto the screen
def display_text(text, color, x, y):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

# defining a cursor function
def crosshair():
    screen.blit(ch, (mpos, mpos))

# creating a sword function
def sword(x, y):
    screen.blit(swordImg, (x, y))

# creating the key function
def key(x, y):
    screen.blit(keyImg, (x, y))

# creating the player function
def player(x, y):
    screen.blit(playerImg, (x, y))

# monster function
def monster(x, y):
    screen.blit(monsterImg, (x, y))

# below are the maps
def map1():
    pygame.draw.rect(screen, grey, pygame.Rect(0, 0, 1920, 400))
    pygame.draw.rect(screen, grey, pygame.Rect(0, 680, 1920, 400))
    pygame.draw.line(screen, grey, (0, 0), (0, 1080), 100)


def map2T():
    pygame.draw.rect(screen, grey, pygame.Rect(0, 0, 700, 400))
    pygame.draw.rect(screen, grey, pygame.Rect(900, 0, 1230, 400))
    pygame.draw.rect(screen, grey, pygame.Rect(0, 680, 1920, 400))


def map3msr():
    pygame.draw.rect(screen, grey, pygame.Rect(0, 0, 200, 400))
    pygame.draw.rect(screen, grey, pygame.Rect(0, 680, 200, 400))
    pygame.draw.rect(screen, grey, pygame.Rect(0, 900, 1920, 400))
    pygame.draw.rect(screen, grey, pygame.Rect(0, 0, 1920, 180))
    pygame.draw.rect(screen, grey, pygame.Rect(1720, 0, 200, 1080))


def map4gate():
    pygame.draw.rect(screen, grey, pygame.Rect(0, 0, 700, 1080))
    pygame.draw.rect(screen, grey, pygame.Rect(900, 0, 1920, 1080))
    pygame.draw.line(screen, grey, (0, 0), (1920, 0), 20)


def map5end():
    pygame.draw.rect(screen, grey, pygame.Rect(0, 0, 700, 1080))
    pygame.draw.rect(screen, grey, pygame.Rect(900, 0, 1920, 1080))


def map6win():
    screen.fill((126, 200, 80))
    display_text('You win! Congratulations! Check "game_log.txt" for a record of wins and losses!', grey, 200, 540)


def map7lose():
    screen.fill((220, 0, 0))
    display_text('You lose! Shrek has eaten you! Check "game_log.txt" for a record of wins and losses!', grey, 200, 540)

# setting up map changing with a list and 'current_level' variable
current_level = 0
maps_data = [map1, map2T, map3msr, map4gate, map5end, map6win, map7lose]

running = True
# main game loop
while running:
    screen.fill((119, 119, 119))
    # tracking mouse movement for debugging
    mpos = pygame.mouse.get_pos()
    print(mpos)
    # event loop (pygame thing) and setting conditions to quit the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            logging.shutdown()
        # movement controls for player
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                playerX_change = -0.8
            if event.key == pygame.K_d:
                playerX_change = 0.8
            if event.key == pygame.K_w:
                playerY_change = -0.8
            if event.key == pygame.K_s:
                playerY_change = 0.8
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                playerX_change = 0
            if event.key == pygame.K_w or event.key == pygame.K_s:
                playerY_change = 0

    if current_level == 0:
        # Displaying text on map1
        display_text("WASD to move", grey, 800, 540)
    if current_level == 1:
        display_text('Kill the monster, get the key, escape the castle', grey, 550, 550)

    playerY += playerY_change
    playerX += playerX_change
    # end map collision
    if current_level == 4:
        if playerX <= 701:
            playerX = 701
        if playerX >= 880:
            playerX = 880
        if playerY >= 1070:
            playerY = 20
            current_level = 1
        if playerY <= 11:
            current_level = 5
    # gate map collision
    if current_level == 3:
        if playerX <= 701:
            playerX = 701
        if playerX >= 880:
            playerX = 880
        if playerY <= 11:
            playerY = 11
        if playerY >= 1070:
            playerY = 20
            current_level = 1
        if not sword_collected:
            sword_rect = pygame.Rect(swordX, swordY, swordImg.get_width(), swordImg.get_height())
            player_rect = pygame.Rect(playerX, playerY, playerImg.get_width(), playerImg.get_height())
            if sword_rect.colliderect(player_rect):
                sword_collected = True
        if not sword_collected:
            sword(swordX, swordY)
        if sword_collected:
            playerImg = playerswImg
    # third map collision
    if current_level == 2:
        if playerX <= 195 and playerY >= 630:
            playerY = 630
        if playerX <= 195 and playerY <= 400:
            playerY = 400
        if playerY <= 390 and playerX <= 201:
            playerX = 201
        if playerY >= 680 and playerX <= 201:
            playerX = 201
        if playerX <= 10:
            current_level = 1
            playerX = 1890
        if playerY >= 850 and playerX >= 201:
            playerY = 850
        if playerY <= 181:
            playerY = 181
        if playerX >= 1699:
            playerX = 1699
        # monster tracking the player
        if playerX > monsterX:
            monsterX += monster_speed
        elif playerX < monsterX:
            monsterX -= monster_speed
        if playerY > monsterY:
            monsterY += monster_speed
        elif playerY < monsterY:
            monsterY -= monster_speed
        # check collision with the key
        if not key_collected:
            key_rect = pygame.Rect(keyX, keyY, keyImg.get_width(), keyImg.get_height())
            player_rect = pygame.Rect(playerX, playerY, playerImg.get_width(), playerImg.get_height())
            if key_rect.colliderect(player_rect):
                key_collected = True
        # draw key if not collected
        if not key_collected:
            key(keyX, keyY)
        if playerX < monsterX + monsterImg.get_width() and \
                playerX + playerImg.get_width() > monsterX and \
                playerY < monsterY + monsterImg.get_height() and \
                playerY + playerImg.get_height() > monsterY:
            if sword_collected:
                # Player has the sword, defeat the monster
                monsterImg = pygame.image.load('blood.png')  # Replace monster image with blood
                monster_speed = 0
            else:
                current_level = 6

    # second map collision
    if current_level == 1:
        if playerX >= 1900:
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
        if playerY <= 10:
            current_level = 3
            playerY = 1060
        if key_collected and playerY <= 12:
            current_level = 4
            playerY = 1060
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
    # displaying the player and monster
    player(playerX, playerY)
    if current_level == 2:
        monster(monsterX, monsterY)
    # map transition code
    current_map = maps_data[current_level]
    current_map()
    if current_level == 5 and not game_over:
        logging.info('Win')
        game_over = True
        logging.shutdown()
    if current_level == 6 and not game_over:
        logging.info('Loss')
        game_over = True
        logging.shutdown()
    crosshair()
    pygame.display.update()

pygame.quit()
