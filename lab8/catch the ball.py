import pygame
from pygame.draw import *
from random import randint
pygame.init()

#Сделал три задания из указанных в конце лабораторной работы. Однако нахождение на экране нескольких шариков плохо получилось: очки за попадания в шарики начисляются далеко не для каждого шарика.
FPS = 2
screen = pygame.display.set_mode((1100, 500))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

fon = pygame.font.Font(None, 30) 
'''шрифт для подсчета очков'''


def new_ball():
    '''рисует новый шарик, случайным образом выбирая его координату, радиус и цвет'''
    global c
    c = []
    c.append(randint(100, 1000))
    c.append(randint(100, 400))
    c.append(randint(10, 100))
    color = COLORS[randint(0, 5)]
    circle(screen, color, (c[0], c[1]), c[2])


def click(event):
    'Возвращает координаты и радиус шарика, который находится на экране'
    return c

def Text(point):
    '''Отображает настоящие очки'''
    text = fon.render(str(point), True, (180, 0, 0))
    screen.blit(text, (10, 10))

pygame.display.update()
clock = pygame.time.Clock()
finished = False


point=0

while finished==False:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print('Click!')
            for i in range (0, len(c), 3):
                # Этот цикл начисления очков работает не так, как хочется: очки начисляются не за каждый шарик. Не хватает времени пробежаться по всему массиву?
                if (event.pos[0] - click(event)[i + 0])**2 + (event.pos[1] - click(event)[i + 1])**2 <= click(event)[i + 2]**2:
                    point += 1 
    for k in range (randint(1, 5)):
        new_ball()
    Text(point)
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()