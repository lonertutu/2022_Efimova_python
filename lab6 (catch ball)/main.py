import pygame
from random import randint

pygame.init()

minradius = 10
maxradius = 40
width = 1280
length = 720
score = 0

FPS = 60
screen = pygame.display.set_mode((width, length))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
empty_ball = [0, 0, 0, "BLACK", 0, 0, 0]
Balls = []
Planets = []


def new_ball():
    x = randint(maxradius, width - maxradius)
    y = randint(maxradius, length - maxradius)
    r = randint(minradius, maxradius)
    speedx = randint(-3, 3)
    speedy = randint(-3, 3)
    color = COLORS[randint(0, 5)]
    return [x, y, r, color, speedx, speedy]


def new_symbol():
    #pygame.image.load("saturn.png")
    #background_image = pygame.image.load("saturn.png").convert_alpha()
    x1 = randint(100, 500)
    y1 = randint(100, 500)
    speedx1 = randint(-3, 3)
    speedy1 = randint(-3, 3)
    #screen.blit(background_image, [x1, y1])
    return [x1, y1, speedx1, speedy1]


def click(event, ball):
    return ((event.pos[1] - ball[1]) ** 2 + (event.pos[0] - ball[0]) ** 2) < ball[2] ** 2

def click_planet(event, planet):
    return ((event.pos[1] - 15) ** 2 + (event.pos[0] - 15) ** 2) < 15 * 2

def draw_balls():
    for i in Balls:
        pygame.draw.circle(screen, i[3], (i[0], i[1]), i[2], 0)

def draw_planets(x1, y1):
    for i in Planets:
        pygame.image.load("saturn.png")
        background_image = pygame.image.load("saturn.png").convert_alpha()
        screen.blit(background_image, [x1, y1])
        pygame.draw.circle(screen, i[3], (i[0], i[1]), i[2], 0)

def speed_effect():
    for i in Balls:
        i[0] = i[0] + i[4]
        i[1] = i[1] + i[5]

def speed_effect_planets():
    for i in Planets:
        i[0] = i[0] + i[4]
        i[1] = i[1] + i[5]



def collision_detection():
    for i in Balls:
        if i[0] < 0 + i[2]:
            i[0] = 0 + i[2]
            i[4] = -i[4]
        if i[0] > width - i[2]:
            i[0] = width - i[2]
            i[4] = -i[4]
        if i[1] < 0 + i[2]:
            i[1] = 0 + i[2]
            i[5] = -i[5]
        if i[1] > length - i[2]:
            i[1] = length - i[2]
            i[5] = -i[5]

def collision_detection_planets():
    for i in Planets:
        if i[0] < 0 + i[2]:
            i[0] = 0 + i[2]
            i[4] = -i[4]
        if i[0] > width - i[2]:
            i[0] = width - i[2]
            i[4] = -i[4]
        if i[1] < 0 + i[2]:
            i[1] = 0 + i[2]
            i[5] = -i[5]
        if i[1] > length - i[2]:
            i[1] = length - i[2]
            i[5] = -i[5]

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(Balls)):
                if click(event, Balls[i]):
                    print("click")
                    score += 10
                    print("Your score is", score)
                    Balls[i] = empty_ball

        elif event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(Planets)):
                if click(event, Planets[i]):
                    print("click")
                    score += 100
                    print("Your score is", score)
                    Planets[i] = empty_ball

    if randint(0, 100) > 95:
        a = new_ball()
        Balls.append(a)
    draw_balls()
    pygame.display.update()
    speed_effect()
    collision_detection()
    screen.fill(BLACK)

pygame.quit()
