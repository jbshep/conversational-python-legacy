import pygame
from pygame.locals import *

pygame.init()

white = (255, 255, 255)
black = (  0,   0,   0)
green = (  0, 255,   0)

screenWidth = 800
screenHeight = 600
screenSize = [screenWidth, screenHeight]
screen = pygame.display.set_mode(screenSize)
pygame.display.set_caption("WINDOW TITLE HERE")

clock = pygame.time.Clock()

done = False

while not done:
    # 1. Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # 2. Program logic, change variables, etc.

    # 3. Draw stuff
    screen.fill(white)
    pygame.draw.line(screen, green, [100, 200], [150, 300], 3)
    pygame.draw.line(screen, green, [150, 300], [200, 200], 3)

    pygame.display.flip()
    clock.tick(20)

pygame.quit()
