import pygame
pygame.init()

pygame.display.set_caption("Alien Game")
screen = pygame.display.set_mode((1080, 700))

background = pygame.image.load('assets/bg.jpg')
running  = True

while running:
    screen.blit(background,(0, -200))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()