import pygame
from json import load
from src.game import Game
from src.colors import *

pygame.init()

clock = pygame.time.Clock()
FPS = 60

pygame.display.set_caption('Minesweeper')
pygame.display.set_icon(pygame.image.load('assets/flag.png'))

settings_file = open("settings.json", "r")
settings = load(settings_file)
nl = settings["nb_lines"]
nc = settings["nb_colons"]
nb_bomb = settings["nb_bombs"]
case_width = settings["case_width"]
settings_file.close()

width = nc*case_width + 20
height = nl*case_width + 100
screen = pygame.display.set_mode((width, height))

background = pygame.draw.rect(screen, GREY, [0, 0, width, height])

font = pygame.font.Font('assets/fonts/roboto-bold.ttf', 32)
play_button_background = pygame.draw.rect(screen, LIGHT_GREY, [width//2-100, 10, 200, 60])
play_button_text = font.render('PLAY', 1, BLACK)
screen.blit(play_button_text, [width//2 - 100 + 60, 23])

running = True

game = Game(screen, nl, nc, nb_bomb, case_width)

while running:
    pygame.display.flip()
    clock.tick(FPS)
    if game.started:
        game.update_timer()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print('Game closed')
        if event.type == pygame.MOUSEBUTTONDOWN and (event.button == 1 or event.button == 3):
            if play_button_background.collidepoint(event.pos):
                game.reset()
            elif game.is_playing:
                for l in range(len(game.grid.cases)):
                    line = game.grid.cases[l]
                    for c in range(len(line)):
                        case = line[c]
                        if case.rect.collidepoint(event.pos):
                            game.grid.click(event.button, l, c)
