import pygame
from pygame.draw import *
pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
screen.fill((198, 195, 181))

pygame.draw.circle(screen, (0, 0, 0), (200, 200), 102, 2)
pygame.draw.circle(screen, (255, 255, 0), (200, 200), 100, 0)
pygame.draw.circle(screen, (255, 0, 0), (155, 170), 25)
pygame.draw.circle(screen, (0, 0, 0), (155, 170), 10)
pygame.draw.circle(screen, (255, 250, 200), (250, 170), 30)
pygame.draw.circle(screen, (255, 0, 0), (250, 170), 32, 2)
pygame.draw.ellipse(screen, (255, 0, 0), (240, 137, 24, 17))
pygame.draw.polygon(screen, (200, 10, 50), [[160, 240], [185, 268], [240, 235]])
pygame.draw.rect(screen, (255, 255, 180), (168, 238, 12, 20))
pygame.draw.polygon(screen, (255, 255, 180), [[195, 248], [202, 260], [210, 254], [198, 246]])




pygame.display.update()

clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

