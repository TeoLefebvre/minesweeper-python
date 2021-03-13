import pygame
from quadrillage import Quadrillage
from colors import *
from time import perf_counter

class Game:

    def __init__(self, screen):

        self.font = pygame.font.Font('assets/fonts/roboto-bold.ttf', 25)
        self.is_playing = True
        self.nl = 23 # nb lignes
        self.nc = 23 # nb colonne
        self.screen = screen
        self.nb_bomb = 100
        self.current_bomb = self.nb_bomb

        self.quadrillage = Quadrillage(self, self.nc, self.nl, self.nb_bomb)
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
        bomb_counter_background = pygame.draw.rect(self.screen, LIGHT_GREY, [140, 20, 60, 40])
        bomb_counter_text = self.font.render(f'{self.current_bomb}', 1, RED)
        self.screen.blit(bomb_counter_text, [150, 25])

    def reset_timer(self):
        self.fin = self.debut
        self.refresh_timer()

    def update_timer(self):
        self.fin = perf_counter()
        self.refresh_timer()
    
    def refresh_timer(self):
        timer_background = pygame.draw.rect(self.screen, LIGHT_GREY, [520, 20, 100, 40])
        timer_text = self.font.render(self.get_duree(), 1, RED)
        self.screen.blit(timer_text, [530, 25])

    def get_duree(self):
        return '{0:.1f}'.format(self.fin - self.debut)
