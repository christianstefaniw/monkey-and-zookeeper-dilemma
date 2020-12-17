import pygame

from monkey_and_zookeeper.constants import GRAVITY


class Monkey:
    def __init__(self, colour, width, point1, point2, screen):
        self.colour = colour
        self.point1 = point1
        self.point2 = point2
        self.screen = screen
        self.gravity_speed = 0
        self.width = width

    def draw_monkey(self):
        pygame.draw.line(self.screen, self.colour, (self.point1['x'], self.point1['y']),
                         (self.point2['x'], self.point2['y']), width=self.width)

    def drop_monkey(self):
        self.gravity_speed += GRAVITY
        self.point1['y'] += self.gravity_speed
        self.point2['y'] += self.gravity_speed
