import pygame
from colors import *

class Case:

    def __init__(self, screen, l, c, x, y, case_width):
        self.screen = screen
        self.cw = case_width
        self.l = l
        self.c = c
        self.bomb = False
        self.flag = False
        self.revealed = False
        self.x = x + self.cw * c
        self.y = y + l * self.cw
        self.draw(LIGHT_GREY)

    def draw(self, color):
        self.rect = pygame.draw.rect(self.screen, color, [self.x, self.y, self.cw-1, self.cw-1])