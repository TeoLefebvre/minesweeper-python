import pygame
from colors import *

class Case:

    def __init__(self, screen, l, c, x, y):
        self.screen = screen
        self.l = l
        self.c = c
        self.bomb = False
        self.flag = False
        self.revealed = False
        self.x = x + 31 * c
        self.y = y + l * 31
        self.draw(LIGHT_GREY)

    def draw(self, color):
        self.rect = pygame.draw.rect(self.screen, color, [self.x, self.y, 30, 30])