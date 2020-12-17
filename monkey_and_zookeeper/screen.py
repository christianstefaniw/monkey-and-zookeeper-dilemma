import pygame


class Screen:
    def __init__(self, height, width, colour):
        self.colour = colour
        self.screen = pygame.display.set_mode([width, height])

    def draw_screen(self):
        self.screen.fill(self.colour)
