import pygame
from .quadrillage import Quadrillage
from .colors import *
from time import perf_counter

class Game:

    def __init__(self, screen, nl, nc, nb_bomb, case_width):

        self.font = pygame.font.Font('assets/fonts/roboto-bold.ttf', 25)
        self.is_playing = True
        self.nl = nl # nb lignes
        self.nc = nc # nb colonne
        self.screen = screen
        self.nb_bomb = nb_bomb
        self.current_bomb = self.nb_bomb

        self.quadrillage = Quadrillage(self, self.nc, self.nl, self.nb_bomb, case_width)
        self.update_bomb_counter(0)

        self.debut = 0
        self.fin = 0
        self.refresh_timer()
        self.started = False

    def start(self):
        self.started = True
        self.debut = perf_counter()

    def reset(self):
        self.quadrillage = Quadrillage(self, self.nc, self.nl, self.nb_bomb)
        self.is_playing = True
        self.started = False
        self.current_bomb = self.nb_bomb
        self.update_bomb_counter(0)
        self.reset_timer()

    def game_over(self):
        self.is_playing = False
        self.started = False

    def update_bomb_counter(self, nb):
        self.current_bomb += nb
        self.refresh_bomb_counter()

    def refresh_bomb_counter(self):
        x_play_button = self.screen.get_width()//2 - 100
        bomb_counter_background = pygame.draw.rect(self.screen, LIGHT_GREY, [x_play_button - 80, 20, 60, 40])
        bomb_counter_text = self.font.render(f'{self.current_bomb}', 1, RED)
        self.screen.blit(bomb_counter_text, [x_play_button - 70, 25])

    def reset_timer(self):
        self.fin = self.debut
        self.refresh_timer()

    def update_timer(self):
        self.fin = perf_counter()
        self.refresh_timer()
    
    def refresh_timer(self):
        x_play_button = self.screen.get_width()//2 - 100
        timer_background = pygame.draw.rect(self.screen, LIGHT_GREY, [x_play_button + 220, 20, 100, 40])
        timer_text = self.font.render(self.get_duree(), 1, RED)
        self.screen.blit(timer_text, [x_play_button + 230, 25])

    def get_duree(self):
        return '{0:.1f}'.format(self.fin - self.debut)
