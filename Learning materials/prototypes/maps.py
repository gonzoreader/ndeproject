#!/usr/bin/env python3
import pygame
pygame.init()

SC_WIDTH = 1920
SC_HEIGHT = 1080
black = (0,0,0)
grey = (80,80,80)
screen = pygame.display.set_mode((SC_WIDTH,SC_HEIGHT))

def map1():
    pygame.draw.rect(screen, (grey), pygame.Rect(0, 0, 1920, 400), )
    pygame.draw.rect(screen, (grey), pygame.Rect(0, 680, 1920, 400), )
    pygame.draw.line(screen, (grey), (0, 0), (0, 1080), 100)
    
def map2():
    pygame.draw.rect(screen, (grey), pygame.Rect(0, 0, 500, 400))   
    pygame.draw.rect(screen, (grey), pygame.Rect(1920, 0, -500, 400))





def main():
    running = True

    while running:
        screen.fill((black))
        # Event for loop. Pygame uses events for mouse movement, key presses etc.
        # All events get passed through this loop so that they are executed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        map1()
        pygame.display.flip()

if __name__ == '__main__': 
    main()