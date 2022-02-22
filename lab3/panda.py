import pygame
import pygame.draw as dr

pi = 3.14
pygame.init()

FPS = 30
screen = pygame.display.set_mode((900, 700))
surf = pygame.Surface((900, 350))
surf.fill((245, 165, 151))
surf.set_alpha(100)
CORAL = (245, 155, 141)
PINKY = (245, 204, 190)
BAMBOO = (54, 117, 50)
WHITE = (255, 238, 249)
REALWHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLACKY = (30, 20, 44)
GREY = (42, 31, 47)
BEIGE = (250, 235, 215)
OLIVE = (107, 142, 35)
BAMBOO2 = (60, 155, 50)
DARKOLIVE = (69, 97, 47)
LIGHTGREEN = (74, 185, 75)

dr.rect(screen, CORAL, (0, 0, 900, 700))  # wallpaper
dr.rect(screen, OLIVE, (0, 350, 900, 700))

dr.ellipse(screen, DARKOLIVE, (210, 455, 250, 70))  # shadows
dr.ellipse(screen, DARKOLIVE, (570, 485, 250, 70))
dr.ellipse(screen, DARKOLIVE, (470, 485, 150, 70))

j = 1

for i in range(80):
    R = 165 + j
    G = 75 + j
    B = 71 + j
    CORALY = (R, G, B)
    dr.aaline(screen, CORALY, [0, 350 - i], [900, 350 - i])
    j += 1

j = 1
for i in range(80):
    R = 165 + j
    G = 75 + j
    B = 91 + j
    CORALY = (R, G, B)
    dr.aaline(screen, CORALY, [0, 0 + i], [900, 0 + i])
    j += 1

j = 1
for i in range(80):
    R = 187 - j
    G = 222 - j
    B = 125 - j
    GROUND = (R, G, B)
    dr.aaline(screen, GROUND, [0, 350 + i], [900, 350 + i])
    j += 1

j = 1
for i in range(80):
    R = 10 + 1.2*j
    G = 20 + 1.525*j  #(107, 142, 35)
    B = 10 + 0.3*j
    GROUND = (R, G, B)
    dr.aaline(screen, GROUND, [0, 700 - i], [900, 700 - i])
    j += 1

dr.polygon(screen, BAMBOO2, [[300, 0], [340, 0], [350, 300], [295, 300]])  # 1backbambootree
dr.polygon(screen, BAMBOO, [[315, 0], [335, 0], [340, 300], [315, 300]])
dr.polygon(screen, LIGHTGREEN, [[305, 0], [310, 0], [315, 300], [305, 300]])

dr.polygon(screen, BAMBOO2, [[540, 0], [560, 0], [570, 300], [530, 300]])
dr.polygon(screen, BAMBOO, [[550, 0], [555, 0], [565, 300], [545, 300]])
dr.polygon(screen, LIGHTGREEN, [[545, 0], [548, 0], [540, 300], [532, 300]])
screen.blit(surf, (0, 0))

dr.polygon(screen, BAMBOO, [[600, 0], [640, 0], [655, 350], [595, 350]])
dr.polygon(screen, DARKOLIVE, [[625, 0], [635, 0], [650, 350], [640, 350]])
dr.polygon(screen, BAMBOO2, [[605, 0], [610, 0], [615, 350], [600, 350]])

dr.line(screen, BAMBOO2, (200, 370), (200, 250), 10)  # first bamboo
dr.line(screen, BAMBOO2, (200, 170), (220, 100), 10)
dr.line(screen, BAMBOO2, (220, 90), (250, 60), 10)
dr.line(screen, BAMBOO2, (200, 235), (200, 180), 10)

dr.line(screen, BAMBOO, (700, 370), (700, 250), 10)  # first bamboo
dr.line(screen, BAMBOO, (700, 170), (720, 100), 10)
dr.line(screen, BAMBOO, (720, 90), (750, 60), 10)
dr.line(screen, BAMBOO, (700, 235), (700, 180), 10)

dr.line(screen, BAMBOO, (180, 410), (180, 250), 15)  # second bamboo
dr.line(screen, BAMBOO, (180, 235), (170, 180), 14)
dr.line(screen, BAMBOO, (170, 170), (140, 130), 12)

dr.ellipse(screen, WHITE, (250, 280, 150, 160))  # body
dr.ellipse(screen, WHITE, (280, 290, 220, 160))

dr.ellipse(screen, BLACK, [430, 350, 60, 130])  # backleg
dr.polygon(screen, BLACK, [[430, 400], [380, 510], [455, 515], [475, 470]])
dr.ellipse(screen, BLACK, [380, 480, 80, 50])

dr.polygon(screen, BLACKY, [[225, 340], [255, 340], [270, 450], [240, 450]])  # frontrightleg
dr.ellipse(screen, BLACKY, [200, 340, 40, 130])
dr.polygon(screen, BLACKY, [[210, 370], [270, 450], [240, 500], [185, 480]])
dr.ellipse(screen, BLACKY, [185, 460, 65, 45])

dr.ellipse(screen, WHITE, (250, 280, 150, 160))

dr.polygon(screen, BLACK, [[300, 270], [365, 290], [360, 420], [295, 400]])  # frontleftleg
dr.polygon(screen, BLACK, [[295, 400], [362, 409], [340, 500], [280, 480]])
dr.polygon(screen, BLACK, [[290, 440], [340, 500], [310, 530], [250, 520]])
dr.ellipse(screen, BLACK, [250, 510, 65, 30])
dr.ellipse(screen, BLACK, [245, 480, 70, 60])

# rightear
dr.rect(screen, BLACK, (215, 215, 23, 45), border_top_right_radius=25, border_bottom_left_radius=40,
        border_bottom_right_radius=40, border_top_left_radius=80)

dr.ellipse(screen, REALWHITE, (205, 245, 120, 100))  # head
dr.ellipse(screen, REALWHITE, [225, 275, 99, 90])
dr.ellipse(screen, REALWHITE, [195, 240, 100, 125])

dr.ellipse(screen, BEIGE, [190, 310, 70, 50])  # face
dr.polygon(screen, BEIGE, [[210, 300], [240, 310], [240, 340], [190, 335]])
dr.rect(screen, BLACK, (230, 295, 30, 30), border_top_right_radius=20, border_bottom_left_radius=20,
        border_bottom_right_radius=7, border_top_left_radius=10)
dr.rect(screen, BLACK, (200, 295, 10, 20), border_top_right_radius=5, border_bottom_left_radius=5,
        border_bottom_right_radius=5, border_top_left_radius=5)
dr.rect(screen, BLACK, (190, 325, 20, 15), border_top_right_radius=5, border_bottom_left_radius=10,
        border_bottom_right_radius=10, border_top_left_radius=5)
dr.rect(screen, BLACK, (200, 345, 25, 15), border_top_right_radius=5, border_bottom_left_radius=20,
        border_bottom_right_radius=25, border_top_left_radius=7)

# leftear
dr.rect(screen, GREY, (270, 230, 25, 35), border_top_right_radius=20, border_bottom_left_radius=25,
        border_bottom_right_radius=25, border_top_left_radius=30)
dr.rect(screen, BLACK, (260, 225, 25, 45), border_top_right_radius=5, border_bottom_left_radius=10,
        border_bottom_right_radius=20, border_top_left_radius=20)

# tree
dr.rect(screen, BAMBOO, (455, 0, 55, 550), border_bottom_left_radius=15, border_bottom_right_radius=15)
dr.rect(screen, DARKOLIVE, (480, 0, 25, 550), border_bottom_left_radius=15, border_bottom_right_radius=15)
dr.rect(screen, BAMBOO2, (460, 0, 10, 550), border_bottom_left_radius=15, border_bottom_right_radius=15)

# ----second panda----#
dr.rect(screen, BLACK, (605, 190, 30, 50), border_top_right_radius=20, border_bottom_left_radius=5,
        border_bottom_right_radius=25, border_top_left_radius=5)
dr.ellipse(screen, REALWHITE, (475, 400, 220, 150))  # body
dr.polygon(screen, REALWHITE, [[495, 350], [625, 300], [690, 450], [475, 480]])
dr.polygon(screen, REALWHITE, [[530, 260], [590, 270], [625, 300], [495, 350]])

dr.ellipse(screen, BLACK, (640, 450, 80, 55))  # backleftleg
dr.rect(screen, BLACK, (680, 460, 60, 50), border_top_right_radius=40, border_bottom_left_radius=5,
        border_bottom_right_radius=25, border_top_left_radius=5)

dr.polygon(screen, BLACKY, [[635, 310], [705, 480], [650, 480], [615, 320]])  # frontleftleg
dr.ellipse(screen, BLACKY, (640, 450, 65, 60))

dr.ellipse(screen, WHITE, (530, 200, 130, 130))

dr.ellipse(screen, BLACK, (505, 480, 100, 80))  # backrightleg
dr.polygon(screen, BLACK, [[565, 480], [660, 510], [660, 550], [545, 560]])
dr.ellipse(screen, BLACK, (610, 500, 60, 60))
dr.polygon(screen, BLACK, [[650, 510], [680, 510], [670, 555], [645, 560]])

dr.polygon(screen, BAMBOO2, [[615, 280], [675, 430], [660, 420], [605, 280]])

dr.rect(screen, BLACK, (625, 250, 10, 25), border_top_right_radius=55, border_bottom_left_radius=40,
        border_bottom_right_radius=25, border_top_left_radius=15)
dr.ellipse(screen, REALWHITE, (585, 250, 45, 50))
dr.rect(screen, BLACK, (605, 280, 24, 15), border_top_right_radius=5, border_bottom_left_radius=25,
        border_bottom_right_radius=25, border_top_left_radius=10)
dr.arc(screen, BLACK, (585, 250, 45, 50), (5 / 4) * pi, (5 / 3) * pi, 4)
dr.rect(screen, BLACK, (580, 250, 20, 30), border_top_right_radius=15, border_bottom_left_radius=10,
        border_bottom_right_radius=25, border_top_left_radius=15)
dr.rect(screen, BLACK, (540, 190, 40, 50), border_top_right_radius=10, border_bottom_left_radius=5,
        border_bottom_right_radius=25, border_top_left_radius=25)

dr.ellipse(screen, BLACK, (485, 320, 110, 110))  # frontrightleg
dr.ellipse(screen, BLACK, (555, 385, 80, 60))
dr.polygon(screen, BLACK, [[525, 425], [580, 340], [630, 400], [585, 445]])
dr.polygon(screen, BLACK, [[600, 365], [660, 345], [670, 395], [610, 440]])
dr.ellipse(screen, BLACK, (630, 345, 50, 60))

pygame.display.update()
clock = pygame.time.Clock()  # object clock, wait some time
finished = False

while not finished:
    clock.tick(FPS)  # programm wait 30 fps
    for event in pygame.event.get():  # probegaem po massiv'u
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
