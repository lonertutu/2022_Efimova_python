import math
from random import choice, randint
import pygame

FPS = 60

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
G = 0.81


class Ball:
    def __init__(self, screen: pygame.Surface, x=40, y=450):
        """ Конструктор класса ball

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
        self.x += self.vx
        self.y -= self.vy
        self.vy -= G
        if self.y > HEIGHT - self.r:
            self.y = HEIGHT - self.r
            self.vy *= -0.7

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )
        pygame.draw.circle(
            self.screen,
            BLACK,
            (self.x, self.y),
            self.r,
            width=1
        )

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if (self.x - obj.x) ** 2 + (self.y - obj.y) ** 2 <= (self.r + obj.r) ** 2:
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

        self.x = 20
        self.y = 450

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event, bullet, balls):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        bullet += 1
        new_ball = Ball(self.screen)
        new_ball.r += 5
        self.an = math.atan2((event.pos[1] - new_ball.y), (event.pos[0] - new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10
        return balls, bullet

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            if event:
                if event.pos[0] - 20:
                    self.an = math.atan((event.pos[1] - 450) / (event.pos[0] - 20))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        width = 10
        coords = [
            (self.x, self.y),
            (self.x + (self.f2_power + 20) * math.cos(self.an),
             self.y + (self.f2_power + 20) * math.sin(self.an)),
            (self.x + (self.f2_power + 20) * math.cos(self.an) + width * math.sin(self.an),
             self.y + (self.f2_power + 20) * math.sin(self.an) - width * math.cos(self.an)),
            (self.x + width * math.sin(self.an), self.y - width * math.cos(self.an))
        ]

        pygame.draw.polygon(self.screen, self.color, coords, width=0)

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY


class Target:
    def __init__(self, type=1):
        self.x = randint(600, 780)
        self.y = randint(300, 550)
        self.r = randint(10, 30)
        self.vx = randint(-7, 7)
        self.vy = randint(-7, 7)
        self.color = GAME_COLORS[randint(0, 5)]
        self.live = type
        self.type = type

    def hit(self, point=1, points=1):
        self.live -= 1
        points += point
        return points

    def draw(self):
        if self.type == 1:
            pygame.draw.circle(
                screen,
                self.color,
                (self.x, self.y),
                self.r
            )
            pygame.draw.circle(
                screen,
                BLACK,
                (self.x, self.y),
                self.r,
                width=1
            )
        elif self.type == 2:
            pygame.draw.rect(
                screen,
                self.color,
                (self.x - self.r, self.y - self.r, self.r * 2, self.r * 2)
            )
            pygame.draw.rect(
                screen,
                BLACK,
                (self.x - self.r, self.y - self.r, self.r * 2, self.r * 2),
                width=1
            )

    def move(self):
        self.x += self.vx
        self.y += self.vy


def collision_situation(obj):
    if obj.x + obj.r > WIDTH:
        obj.vx *= -1
        obj.x = WIDTH - obj.r
    elif obj.y + obj.r > HEIGHT:
        obj.vy *= -1
        obj.x = HEIGHT - obj.r
    elif obj.x - obj.r < 0:
        obj.vx *= -1
        obj.x = obj.r
    elif obj.y - obj.r < 0:
        obj.vy *= -1
        obj.y = obj.r


def drawscore():
    """Вывод очков на экран"""
    f1 = pygame.font.Font(None, 36)
    tbl = 'points: '
    tbl += str(points)
    text1 = f1.render(tbl, True, BLACK)
    screen.blit(text1, (10, 10))


def showtext():
    f1 = pygame.font.Font(None, 36)
    tbl = 'Вы уничтожили цель за '
    tbl += str(bulletshow)
    tbl += ' выстрелов'
    text1 = f1.render(tbl, True, BLACK)
    screen.blit(text1, (180, 250))


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
bulletshow = 0
balls = []
points = 0

clock = pygame.time.Clock()
gun = Gun(screen)
target1 = Target(1)
target2 = Target(2)
finished = False

do_showtext = 0
pause = False

while not finished:
    screen.fill(WHITE)
    gun.draw()
    target1.draw()
    target2.draw()
    for b in balls:
        b.draw()
    drawscore()
    pause = False
    if do_showtext > 0:
        showtext()
        do_showtext -= 1
        pause = True
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not pause:
                gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            if not pause:
                balls, bullet = gun.fire2_end(event, bullet, balls)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)

    for b in balls:
        b.move()
        if b.hittest(target1):
            points = target1.hit()
            if target1.live == 0:
                target1 = Target(1)
                bulletshow = bullet
                bullet = 0
                balls = []
                do_showtext = 100

        if b.hittest(target2):
            points = target2.hit()
            if target2.live == 0:
                target2 = Target(2)
                bulletshow = bullet
                bullet = 0
                balls = []
                do_showtext = 100

    gun.power_up()
    target1.move()
    target2.move()
    collision_situation(target1)
    collision_situation(target2)

pygame.quit()
