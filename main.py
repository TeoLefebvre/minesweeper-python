import pygame
from game import Game
from colors import *

pygame.init()

clock = pygame.time.Clock()
FPS = 60

pygame.display.set_caption('Démineur')
pygame.display.set_icon(pygame.image.load('assets/flag.png'))
width = 730
height = 820
screen = pygame.display.set_mode((width, height))

background = pygame.draw.rect(screen, GREY, [0, 0, width, height])

font = pygame.font.Font('assets/fonts/roboto-bold.ttf', 32)
play_button_background = pygame.draw.rect(screen, LIGHT_GREY, [260, 10, 200, 60])
play_button_text = font.render('PLAY', 1, BLACK)
screen.blit(play_button_text, [320, 23])

running = True

game = Game(screen)

while running:
    
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print('Fermeture du jeu')
        if event.type == pygame.MOUSEBUTTONDOWN and (event.button == 1 or event.button == 3):
            if play_button_background.collidepoint(event.pos):
                game.reset()
            elif game.is_playing:
                for l in range(len(game.quadrillage.cases)):
                    line = game.quadrillage.cases[l]
                    for c in range(len(line)):
                        case = line[c]
                        if case.rect.collidepoint(event.pos):
                            game.quadrillage.click(event.button, l, c)

    if game.started:
        game.update_timer()

    clock.tick(FPS)
