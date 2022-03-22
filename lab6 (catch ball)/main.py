import pygame
from random import randint

pygame.init()

MINRADIUS = 10
MAXRADIUS = 40
WIDTH = 1280
LENGTH = 720
SCORE = 0

FPS = 60
screen = pygame.display.set_mode((WIDTH, LENGTH))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
empty_ball = [0, 0, 0, "BLACK", 0, 0]
Balls = []
Planets = []


def new_ball():
    # Sets the size, colour, position and speed of the ball

    x = randint(MAXRADIUS, WIDTH - MAXRADIUS)
    y = randint(MAXRADIUS, LENGTH - MAXRADIUS)
    r = randint(MINRADIUS, MAXRADIUS)
    speedx = randint(-3, 3)
    speedy = randint(-3, 3)
    color = COLORS[randint(0, 5)]
    return [x, y, r, color, speedx, speedy]


def new_symbol():
    # Sets the size, colour, position and speed of the symbol
    # In this case, the user-selected picture is the symbol

    x1 = randint(100, 500)
    y1 = randint(100, 500)
    r1 = 7
    speedx1 = randint(-3, 3)
    speedy1 = randint(-3, 3)
    return [x1, y1, r1, speedx1, speedy1]


def click(event, ball):
    """
    Checks if the user has clicked on the ball
    :param event: coordinates of user's mouse
    :param ball: coordinates of each ball from the list
    """
    return ((event.pos[1] - ball[1]) ** 2 + (event.pos[0] - ball[0]) ** 2) < ball[2] ** 2


def click_planet(event):
    """
    Checks if the user has clicked on the planet(symbol)
    :param event:  coordinates of user's mouse
    """

    return ((event.pos[1]) ** 2 + (event.pos[0]) ** 2) < 15 * 2


def draw_balls():
    # Draw balls with different parameters: speed, colour, size, coordinates

    for i in Balls:
        pygame.draw.circle(screen, i[3], (i[0], i[1]), i[2], 0)


def draw_planets():
    # Load the picture of the user's symbol
    # Draw balls with different parameters: speed, coordinates

    for i in Planets:
        pygame.draw.circle(screen, i[3], (i[0], i[1]), i[2], 0)
        pygame.image.load("saturn.png")
        background_image = pygame.image.load("saturn.png").convert_alpha()
        screen.blit(background_image, (i[0] - 15, i[1] - 15))


def speed_effect():
    for i in Balls:
        i[0] = i[0] + i[4]
        i[1] = i[1] + i[5]


def speed_effect_planets():
    for i in Planets:
        i[0] = i[0] + i[4]
        # i[1] = i[1] + i[5]


def collision_detection():
    # Check if balls have collided with the walls

    for i in Balls:
        if i[0] < 0 + i[2]:
            i[0] = 0 + i[2]
            i[4] = -i[4]
        if i[0] > WIDTH - i[2]:
            i[0] = WIDTH - i[2]
            i[4] = -i[4]
        if i[1] < 0 + i[2]:
            i[1] = 0 + i[2]
            i[5] = -i[5]
        if i[1] > LENGTH - i[2]:
            i[1] = LENGTH - i[2]
            i[5] = -i[5]


def collision_detection_planets():
    # Check if planets have collided with the walls

    for i in Planets:
        if i[0] < 0 + i[2]:
            i[0] = 0 + i[2]
            i[4] = -i[4]
        if i[0] > WIDTH - i[2]:
            i[0] = WIDTH - i[2]
            i[4] = -i[4]
        if i[1] < 0 + i[2]:
            i[1] = 0 + i[2]
            i[5] = -i[5]
        if i[1] > LENGTH - i[2]:
            i[1] = LENGTH - i[2]
            i[5] = -i[5]


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            my_file = open('list.txt', 'w')
            print("Player_s name ")
            PLAYER_S_NAME = input()
            my_file.write(str(SCORE))
            my_file.write(PLAYER_S_NAME)
            my_file.close()
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(Balls)):
                if click(event, Balls[i]):
                    print("click")
                    SCORE += 10
                    print("Your score is", SCORE)
                    Balls[i] = empty_ball
            for i in range(len(Planets)):
                if click(event, Planets[i]):
                    print("click")
                    SCORE += 100
                    print("Your score is", SCORE)
                    Planets[i] = empty_ball
            # else:
            #    if not click(event, Balls[i]) and not click(event, Planets[i]): //не получается сделать уменьшение очков при не попадании в мишени
            #        print(" :( ")
            #        score -= 10
            #        print("Your score is", score)
    if randint(0, 100) > 95:
        a = new_ball()
        Balls.append(a)
    draw_balls()

    if randint(0, 100) > 95:
        a = new_symbol()
        Planets.append(a)
    draw_planets()

    pygame.display.update()

    speed_effect()
    collision_detection()
    speed_effect_planets()
    collision_detection_planets()
    screen.fill(BLACK)

    f1 = pygame.font.Font(None, 36)
    text1 = f1.render(str(SCORE), True, (180, 0, 0))
    text3 = f1.render(str("Enjoy the game!"), True, (180, 0, 0))
    f1 = pygame.font.Font(None, 20)
    text2 = f1.render(str("To close completely, write the player's name in the terminal"), True, (180, 0, 0))

    screen.blit(text1, (10, 50))
    screen.blit(text2, (5, 5))
    screen.blit(text3, (10, 20))

pygame.quit()
