import pygame
from game import Game
pygame.init()

pygame.display.set_caption("Alien Game")
screen = pygame.display.set_mode((1080, 700))

background = pygame.image.load('assets/bg.jpg')
game = Game()
running  = True

while running:
    screen.blit(background,(0, -200))
    screen.blit(game.player.image, game.player.rect)

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print("Deplacement vers la droite")
            elif event.key == pygame.K_LEFT:
                print("Deplacement vers la gauche") 