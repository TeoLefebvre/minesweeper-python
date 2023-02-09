import pygame
from .colors import *
from .case import Case
from random import randint

class Quadrillage:

    def __init__(self, game, nc, nl, nb_bomb, case_width):
        self.font = pygame.font.Font('assets/fonts/roboto-bold.ttf', 20)
        self.game = game
        self.x = 10
        self.y = 90
        self.cases = []
        self.nc = nc
        self.nl = nl
        self.nb_bomb = nb_bomb
        self.nb_cases_to_reveal = self.nl * self.nc - self.nb_bomb
        self.nb_cases_revealed = 0
        self.loose = False

        for l in range(nl):
            line = []
            for c in range(nc):
                line.append(Case(game.screen, l, c, self.x, self.y, case_width))
            self.cases.append(line)
        
        for i in range(self.nb_bomb):
            self.choose_bomb()
            
    def choose_bomb(self):
        c = randint(0, self.nc - 1)
        l = randint(0, self.nl - 1)
        case = self.cases[l][c]
        if case.bomb:
            self.choose_bomb()
        else:
            case.bomb = True
    
    def see_bomb(self, case):
        nb_bomb = 0
        neighbours = self.select_neighbours(case)
        for neighbour in neighbours:
            if self.cases[neighbour.l][neighbour.c].bomb: nb_bomb += 1
        return nb_bomb

    def see_flag(self, case):
        nb_flag = 0
        neighbours = self.select_neighbours(case)
        for neighbour in neighbours:
            if self.cases[neighbour.l][neighbour.c].flag: nb_flag += 1
        return nb_flag
    
    def click(self, button, l, c):
        case = self.cases[l][c]
        if button == 1 and not case.flag:
            self.left_click(case)
        elif button == 3:
            self.right_click(case)
    
    def right_click(self, case):
        if case.flag:
            case.draw(LIGHT_GREY)
            case.flag = False
            self.game.update_bomb_counter(1)
        elif not case.revealed:
            case.draw(MIDDLE_GREY)
            flag = pygame.image.load('assets/flag.png')
            flag_rect = flag.get_rect()
            flag_rect.x = case.x
            flag_rect.y = case.y
            self.game.screen.blit(flag, flag_rect)
            self.game.update_bomb_counter(-1)
            case.flag = True

    def left_click(self, case):
        if case.revealed:
            self.spread(case)
        else:
            self.reveal(case)

    def print_number(self, case, nb):
        if nb == 1:
            number = self.font.render(str(nb), 1, BLUE)
        elif nb == 2:
            number = self.font.render(str(nb), 1, DARK_GREEN)
        elif nb == 3:
            number = self.font.render(str(nb), 1, RED)
        else:
            number = self.font.render(str(nb), 1, BLACK)

        self.game.screen.blit(number, [case.x + 9, case.y + 4])

    def reveal(self, case):
        if not case.revealed:
            case.revealed = True
            self.nb_cases_revealed += 1
            if self.nb_cases_revealed == 1:
                self.game.start()
            elif self.nb_cases_revealed == self.nb_cases_to_reveal:
                self.game.game_over()
            case.draw(MIDDLE_GREY)
            if case.bomb:
                bomb = pygame.image.load('assets/bomb.png')
                bomb_rect = bomb.get_rect()
                bomb_rect.x = case.x
                bomb_rect.y = case.y
                self.game.screen.blit(bomb, bomb_rect)
                if not self.loose:
                    self.game_over()
            else:
                nb_bomb = self.see_bomb(case)
                if not nb_bomb == 0:
                    self.print_number(case, nb_bomb)
                else:
                    neighbours = self.select_neighbours(case)
                    for neighbour in neighbours:
                        self.reveal(self.cases[neighbour.l][neighbour.c])

    def spread(self, case):
        if not case.bomb:
            neighbours = self.select_neighbours(case)
            nb_flag = self.see_flag(case)
            nb_bomb = self.see_bomb(case)
            if nb_flag == nb_bomb:
                for neighbour in neighbours:
                    case = self.cases[neighbour.l][neighbour.c]
                    if not case.flag:
                        self.reveal(case)

    def game_over(self):
        self.loose = True
        for l in self.cases:
            for c in l:
                self.reveal(c)
        self.game.game_over()

    def select_neighbours(self, case):
        L = []
        for i in range(3):
            try:
                if case.l-1 >= 0 and case.c-1+i >= 0:
                    neighbour = self.cases[case.l-1][case.c-1+i]
                    L.append(neighbour)
            except IndexError as e:
                pass
            try:
                if case.c-1+i >= 0:
                    neighbour = self.cases[case.l+1][case.c-1+i]
                    L.append(neighbour)
            except IndexError as e:
                pass
        try:
            if case.c-1 >= 0:
                neighbour = self.cases[case.l][case.c-1]
                L.append(neighbour)
        except IndexError as e:
            pass
        try:
            neighbour = self.cases[case.l][case.c+1]
            L.append(neighbour)
        except IndexError as e:
            pass

        return L
