import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

pygame.draw.rect(screen, (255, 0, 255), (100, 100, 200, 200))
pygame.draw.rect(screen, (0, 0, 255), (100, 100, 200, 200), 5)
pygame.draw.polygon(screen, (255, 255, 0), [(100,100), (200,50),
                               (300,100), (100,100)])
pygame.draw.polygon(screen, (0, 0, 255), [(100,100), (200,50),
                               (300,100), (100,100)], 5)
pygame.draw.circle(screen, (0, 255, 0), (200, 175), 50)
pygame.draw.circle(screen, (255, 255, 255), (200, 175), 50, 5)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
