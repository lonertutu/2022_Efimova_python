import pygame
import pygame.draw as dr

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 600))

CORAL = (245, 155, 141)
BAMBOO = (54, 117, 50)
WHITE = (255, 238, 249)
REALWHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (42, 31, 47)
BEIGE = (250, 235, 215)

dr.rect(screen, CORAL, (0, 0, 600, 600)) #wallpaper

dr.line(screen, BAMBOO, (280,350),(280,250), 10) #first bamboo
dr.line(screen, BAMBOO, (280,170),(300, 100), 10)
dr.line(screen, BAMBOO, (300,90),(330, 60), 10)
dr.line(screen, BAMBOO, (280,235),(280,180), 10)

dr.line(screen, BAMBOO, (220,350),(220,250), 15) #second bamboo
dr.line(screen, BAMBOO, (220,235),(210,180), 14)
dr.line(screen, BAMBOO, (210,170),(180,130), 12)

#dr.arc(screen,(54, 117, 50), 35, 75, 40, 60)

dr.ellipse(screen, WHITE, (250, 280, 150, 160)) #body
dr.ellipse(screen, WHITE, (280, 290, 220, 160))

dr.ellipse(screen, BLACK, [430, 350, 60, 130]) #backleg
dr.polygon(screen, BLACK, [[430,400], [380,510], [455,515], [475,470]])
dr.ellipse(screen, BLACK, [380, 480, 80, 50])

dr.polygon(screen, BLACK, [[225,340], [255,340], [270,450], [240,450]]) #frontrightleg
dr.ellipse(screen,BLACK, [200,340, 40, 130])
dr.polygon(screen, BLACK, [[210,370], [270,450], [240,500], [185,480]])
dr.ellipse(screen,BLACK, [185, 460, 65, 45])

dr.ellipse(screen, WHITE, (250, 280, 150, 160))

dr.polygon(screen, BLACK, [[350,280], [365,290], [360,420], [295,400]]) #frontleftleg
dr.polygon(screen, BLACK, [[295,400], [362,409], [340,500], [280,480]])
dr.polygon(screen, BLACK, [[290,440], [340,500], [310,530], [250,520]])
dr.ellipse(screen, BLACK, [250, 510, 65,30])
dr.ellipse(screen, BLACK, [245, 480, 70, 60])

#rightear
dr.rect(screen, BLACK, (210, 215, 23 , 45), border_top_right_radius = 25, border_bottom_left_radius = 40, border_bottom_right_radius = 40, border_top_left_radius = 80)

dr.ellipse(screen, REALWHITE, (205, 245, 120, 100)) #head
#dr.polygon(screen, REALWHITE, [[205,270], [240, 365], [280, 365], [300,270]])
dr.ellipse(screen, REALWHITE, [225,275, 99,90])
dr.ellipse(screen, REALWHITE, [195,240, 100,125])

dr.ellipse(screen, BEIGE, [190, 310, 70, 50]) #face
dr.polygon(screen, BEIGE, [[210, 300],[240,310],[240, 340],[190,335]])
dr.rect(screen, BLACK, (230, 295, 30, 30), border_top_right_radius = 20, border_bottom_left_radius = 20, border_bottom_right_radius = 7, border_top_left_radius = 10)
dr.rect(screen, BLACK, (200,295, 10,20), border_top_right_radius = 5, border_bottom_left_radius = 5, border_bottom_right_radius = 5, border_top_left_radius = 5)
dr.rect(screen, BLACK, (190, 325, 20 , 15), border_top_right_radius = 5, border_bottom_left_radius = 10, border_bottom_right_radius = 10, border_top_left_radius = 5)
dr.rect(screen, BLACK, (200, 345, 25 , 15), border_top_right_radius = 5, border_bottom_left_radius = 20, border_bottom_right_radius = 25, border_top_left_radius = 7)

#leftear
dr.rect(screen, GREY, (270, 230, 25 , 35), border_top_right_radius = 20, border_bottom_left_radius = 25, border_bottom_right_radius = 25, border_top_left_radius = 30)
dr.rect(screen, BLACK, (260, 225, 25 , 45), border_top_right_radius = 5, border_bottom_left_radius = 10, border_bottom_right_radius = 20, border_top_left_radius = 20)


pygame.display.update()
clock = pygame.time.Clock() #object clock, wait some time
finished = False

while not finished:
    clock.tick(FPS) #programm wait 30 fps
    for event in pygame.event.get(): #probegaem po massiv'u
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()