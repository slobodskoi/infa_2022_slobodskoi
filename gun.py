import math
from random import choice
from random import randint

import pygame

#Сделаны три упражнения, указанные в лабораторной работе. "Задачи для реализации" не делал. 

FPS = 30

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600

k = 0 #k отвечает за изменение направления движения мишени - вверх-вниз. Если k = 0, мишень двигается вниз, если k = 600 - вверх. Подробнее - в методе move() класса Target.

class Ball:
    def __init__(self, screen: pygame.Surface, x=40, y=450):
        """ Конструктор класса Ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 30

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        self.vy -= 10*1/30 #Потому что в секунде 30 кадров. С другой стороны, почему тогда ниже умножается на 1, а не на 1/30? Ну ладно, анимация правдоподобно смотрится.
        self.x += self.vx
        self.y -= self.vy
        

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def hittest(self, obj):
        '''Попадание снаряда в мишень'''
        if (self.x - obj.x)**2 + (self.y - obj.y)**2 <= (self.r + obj.r)**2:
            return True
        else:
            return False 


class Gun:
    def __init__(self, screen):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREY

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.screen)
        new_ball.r += 5
        self.an = math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            if event.pos[0] != 20:
                self.an = math.atan((event.pos[1]-450) / (event.pos[0]-20))
            else:
                self.an = math.atan((event.pos[1] - 450) / (event.pos[0] + 0.001 - 20)) #Чтоб не делить на ноль
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        # рисует пушку
        pygame.draw.polygon(screen, self.color, [[40, 450], [10, 450], [10, 430], [30, 410]])

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY


class Target:
    def __init__(self):
        self.points = 0
        self.live = 1
        self.new_target()
        self.vel = 0 # Вертикальная скорость мишени, изначально = 0

    def new_target(self):
        """ Инициализация новой цели. """
        self.live = 1
        x = self.x = randint(600, 780)
        y = self.y = randint(300, 550)
        r = self.r = randint(10, 50)
        color = self.color = RED
        self.vel = randint(-40, 40)

    def hit(self, points=1):
        """Попадание шарика в цель."""
        self.points += points

    def draw(self):
        '''Рисует цель в случайном месте, определяемом функцией new_target'''
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)


    def move(self):
        'Движение мишеней вверх-вниз'
        global k
        if 5 < self.y < self.r + 5:
            k=0
        if 595 - self.r < self.y < 605:
            k=600
        if k==0:
            self.vel = randint (5, 40)
            self.y += self.vel
        if k==600:
            self.vel = randint (-40, -5)
            self.y += self.vel
       


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
fon = pygame.font.Font(None, 60) #Будем считать очки за попадания в мишень
bullet = 0
balls = []

def Text(obj1, obj2):
    '''Отображает настоящие очки'''
    text = fon.render(str(obj1.points + obj2.points), True, (180, 0, 0))
    screen.blit(text, (10, 10))

clock = pygame.time.Clock()
gun = Gun(screen)
target1 = Target()
target2 = Target()
finished = False


while not finished:
    screen.fill(WHITE)
    gun.draw()
    target1.draw()
    target2.draw()
    Text(target1, target2) 
    for b in balls:
        b.draw()
    pygame.display.update()

    target1.move()
    target2.move()
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)
    
    for b in balls:
        b.move()
        if b.hittest(target1) and target1.live:
            target1.live = 0 #Смысл в этом target.live? Кажется, что он только мешает создавать новую мишень после попадания, поэтому я в функции new_target написал self.live = 1
            target1.hit()
            target1.new_target()
        if b.hittest(target2) and target2.live:
            target2.live = 0 #Смысл в этом target.live? Кажется, что он только мешает создавать новую мишень после попадания, поэтому я в функции new_target написал self.live = 1
            target2.hit()
            target2.new_target()
    gun.power_up()

pygame.quit()

