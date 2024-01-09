import pygame #import the pygame module into the namespace <module>

WIDTH = 640 # define a constant width for our window
HEIGHT = 480 # define a constant height for our window

#create a pygame window, and
#initialize it with our WIDTH and HEIGHT constants
display = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock() # create a game clock

class Sprite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 20))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH / 2
        self.rect.y = HEIGHT / 2
        self.vx = 0
        self.vy = 0

    def update(self):
        self.vx = 0
        self.vy = 0
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.vx = -0.5
        elif key[pygame.K_RIGHT]:
            self.vx = 0.5
        if key[pygame.K_UP]:
            self.vy = -0.5
        elif key[pygame.K_DOWN]:
            self.vy = 0.5
        self.rect.x += self.vx
        self.rect.y += self.vy

# cretae a player sprite
player = Sprite()

# create a group to hold all of our sprites
sprites = pygame.sprite.Group()

# create a group to hold sprites we want to
# test collions against. These sprites will
# still be added to the sprites list
# but we need a seperate group to test for
# collisions against
collision_sprites = pygame.sprite.Group()

# add a sprite to out collison sprite group
# We also add the sprite to our sprites group
# that holds all sprites
tmp = Sprite()
tmp.update = lambda: None
sprites.add(tmp)
collision_sprites.add(tmp)

# add a player sprites to the player group
player.rect.x = 10
sprites.add(player)


running = True # our variable for controlling our game loop
while running:
    for e in pygame.event.get(): # iterate ofver all the events pygame is tracking
        clock.tick(60) # make our clock keep pour game at 60 FPS
        if e.type == pygame.QUIT: # is the user trying to close the window?
            running = False # if so break the loop
            pygame.quit() # quit the pygame module
            quit() # quit is for IDLE friendliness

    sprites.update()

    # here is where we test for collision
    if pygame.sprite.spritecollide(player, collision_sprites, False):
        print("HIT!")

    display.fill((180, 180, 180)) # fill the pygame screen with white
    sprites.draw(display)
    pygame.display.flip() # update the screen