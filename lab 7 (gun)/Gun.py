import math
from random import choice, randint
import pygame, sys

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
DARK_BLUE = (11, 0, 77)
DARK_SKY = (90, 150, 170)
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600
WIDTH_FOR_MENU1 = 800
HEIGHT_FOR_MENU1 = 30

G = 0.81


class Ball:
    def __init__(self, screen: pygame.Surface, x=40, y=450):
        """ Constructor class of ball

        Args:
        x, y - initial position of the ball
        vx, vy - initial velocity of the ball
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
        """
        Transport the ball in piece of time.
        The method is describing transporting of the ball n one redraw frame.
        Updates the values self.x & self.y.

        """
        self.x += self.vx
        self.y -= self.vy
        self.vy -= G
        if self.y > HEIGHT - self.r:
            self.y = HEIGHT - self.r
            self.vy *= -0.7

    def draw(self):
        """ Draw ball with its coordinates."""
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
        """
        The function checks whether the given object collides with the target described in the obj object.

         Args:
             obj: The object to check for collision with.
         returns:
             Returns True if the ball and the target collide. Otherwise, returns False.
        """
        if (self.x - obj.x) ** 2 + (self.y - obj.y) ** 2 <= (self.r + obj.r) ** 2:
            return True
        else:
            return False


class Gun:
    """ Constructor class of gun. """

    def __init__(self, screen):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREY

        self.x = 20
        self.y = 450

    def fire2_start(self, event):
        """ Shows the start of the fire """
        self.f2_on = 1

    def fire2_end(self, event, bullet, balls):
        """
        Shows the start of the fire
        The initial values of the ball velocity components
        vx and vy depend on the position of the mouse.
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
        """ Aiming. Depends on the position of the mouse. """
        if event:
            if event:
                if event.pos[0] - 20:
                    self.an = math.atan((event.pos[1] - 450) / (event.pos[0] - 20))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        """ Draw the gun with its coordinates, width"""
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
        """ Shows the shotgun power """
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY


class Target:
    """ Constructor class of target, draw with its coordinates, size and velocity """

    def __init__(self, type=1):
        self.x = randint(600, 780)
        self.y = randint(300, 550)
        self.r = randint(10, 30)
        self.vx = randint(-7, 7)
        self.vy = randint(-7, 7)
        self.color = GAME_COLORS[randint(0, 5)]
        self.live = type
        self.type = type

    def hit(self, p_point=1, player_points=0):
        """ Check if it was hitting """
        self.live -= 1
        player_points += p_point
        return player_points

    def draw(self):
        """ Draw the target: ball or rectangle """
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
        """ Movement of targets """
        self.x += self.vx
        self.y += self.vy


class Menu:
    """ Constructor class of menu """

    def __init__(self, points=(400, 350)):
        self.points = points

    def render(self, cover, font, num_point):
        """ Draw cover of menu """
        for i in self.points:
            if num_point == i[5]:
                cover.blit(font.render(i[2], 1, YELLOW), (i[0], i[1] - 30))
            else:
                cover.blit(font.render(i[2], 1, i[3]), (i[0], i[1] - 30))

    def menu(self):
        """ Check player's actions """
        done = True
        font_menu = pygame.font.Font(None, 50)
        pygame.key.set_repeat(0, 0)
        pygame.mouse.set_visible(True)
        point = 0
        while done:
            info.fill(DARK_SKY)
            screen.fill(DARK_SKY)

            mp = pygame.mouse.get_pos()
            for i in self.points:
                if mp[0] > i[0] and mp[0] < i[0] + 155 and mp[1] > i[1] and mp[1] < i[1] + 50:
                    point = i[5]
            self.render(screen, font_menu, point)
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        sys.exit()
                    if e.key == pygame.K_UP:
                        if point > 0:
                            point -= 1
                    if e.key == pygame.K_DOWN:
                        if point < len(self.points) - 1:
                            point += 1
                if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                    if point == 0:
                        done = False
                    elif point == 1:
                        exit()
            screen.blit(info, (0, 0))
            screen.blit(screen, (0, 30))
            pygame.display.flip()


def collision_situation(obj):
    """ Check if targets collide with walls """
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


def drawscore(player_points):
    """ Shows the players points """
    f1 = pygame.font.Font(None, 36)
    tbl = 'Your points: '
    tbl += str(player_points)
    text1 = f1.render(tbl, True, BLACK)
    screen.blit(text1, (10, 10))


def showtext():
    f1 = pygame.font.Font(None, 36)
    tbl = 'You have destroyed the target in '
    tbl += str(bulletshow)
    tbl += ' shots '
    text1 = f1.render(tbl, True, BLACK)
    screen.blit(text1, (180, 250))
    return tbl


def start():
    """ Collection of functions for the main call №1 """
    screen.fill(WHITE)
    gun.draw()
    target1.draw()
    target2.draw()


def start1():
    """ Collection of functions for the main call №2 """
    gun.power_up()
    target1.move()
    target2.move()
    collision_situation(target1)
    collision_situation(target2)


def space(bullet, balls):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not pause:
                gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            if not pause:
                balls, bullet = gun.fire2_end(event, bullet, balls)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)
    return bullet, balls


pygame.init()
info = pygame.Surface((WIDTH_FOR_MENU1, HEIGHT_FOR_MENU1))
screen = pygame.display.set_mode((WIDTH, HEIGHT))
points = [(360, 300, u'Play', DARK_BLUE, DARK_BLUE, 0),
          (360, 340, u'Exit', DARK_BLUE, DARK_BLUE, 1)]
game = Menu(points)
game.menu()

bullet = 0
bulletshow = 0
balls = []
player_points = 0
clock = pygame.time.Clock()
gun = Gun(screen)
target1 = Target(1)
target2 = Target(2)
finished = False

do_showtext = 0
pause = False

while not finished:
    start()
    for b in balls:
        b.draw()
    drawscore(player_points)
    pause = False
    if do_showtext > 0:
        showtext()
        do_showtext -= 1
        pause = True
    pygame.display.update()

    clock.tick(FPS)
    space(bullet, balls)

    for b in balls:
        b.move()
        if b.hittest(target1):
            player_points = target1.hit()
            if target1.live == 0:
                target1 = Target(1)
                bulletshow = bullet
                bullet = 0
                balls = []
                do_showtext = 100

        if b.hittest(target2):
            player_points = target2.hit()
            if target2.live == 0:
                target2 = Target(2)
                bulletshow = bullet
                bullet = 0
                balls = []
                do_showtext = 100
    start1()

pygame.quit()
