import pygame

from monkey_and_zookeeper.constants import GRAVITY


class Banana:
    def __init__(self, colour, width, point1, point2, screen, x_speed, y_speed, gravity_on):
        self.colour = colour
        self.point1 = point1
        self.point2 = point2
        self.screen = screen
        self.width = width
        self.y_speed = y_speed
        self.x_speed = x_speed
        self.gravity_on = gravity_on

    def draw_banana(self):
        pygame.draw.line(self.screen, self.colour, (self.point1['x'], self.point1['y']),
                         (self.point2['x'], self.point2['y']), width=self.width)

    def launch_banana(self):
        self.point1['x'] += self.x_speed
        self.point2['x'] += self.x_speed

        self.point1['y'] -= self.y_speed
        self.point2['y'] -= self.y_speed

        if self.gravity_on:
            self.y_speed -= GRAVITY
