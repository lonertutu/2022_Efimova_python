import pygame
import pygame.draw as dr

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

dr.circle(screen, (255, 235, 109), (200,200), 100)
dr.circle(screen, (241, 111, 86), (180,180), 15)
dr.circle(screen, (241, 111, 86), (220,180), 15)
dr.circle(screen, (1, 0, 10), (180,180), 7)
dr.circle(screen, (1, 0, 10), (220,180), 7)
dr.line(screen, (1, 0, 10), (165,165), (190,175), 5)
dr.line(screen, (1, 0, 10),  (210,175), (235,165), 5)
dr.line(screen, (1, 0, 10), (160,230), (240,230), 15)

#can copy paste
pygame.display.update()
clock = pygame.time.Clock() #object clock, wait some time
finished = False

while not finished:
    clock.tick(FPS) #programm wait 30 fps
    for event in pygame.event.get(): #probegaem po massiv'u
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()