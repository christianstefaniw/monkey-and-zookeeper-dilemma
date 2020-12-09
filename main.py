import time
import pygame

from monkey_and_zookeeper.monkey import Monkey
from monkey_and_zookeeper.screen import Screen
from monkey_and_zookeeper.banana import Banana
from monkey_and_zookeeper.constants import *


class Engine:
    def __init__(self, gravity):
        self.gravity = gravity
        self.screen = Screen(height=500, width=800, colour=BLACK)
        self.monkey = Monkey(colour=BROWN, width=10, point1={'x': 750, 'y': 0}, point2={'x': 750, 'y': 70},
                             screen=self.screen.screen)
        self.banana = Banana(colour=YELLOW, screen=self.screen.screen, x_speed=30, y_speed=18, width=5,
                             point1={'x': 0, 'y': 500},
                             point2={'x': 0, 'y': 480}, gravity_on=gravity)

    def out_of_bounds(self):
        if self.monkey.point1['y'] >= 500 and self.gravity:
            self.create_objects()

        elif self.banana.point1['x'] >= 800:
            self.create_objects()

    def create_objects(self):
        self.monkey = Monkey(colour=BROWN, width=10, point1={'x': 750, 'y': 0}, point2={'x': 750, 'y': 70},
                             screen=self.screen.screen)
        self.banana = Banana(colour=YELLOW, screen=self.screen.screen, x_speed=30, y_speed=18, width=5,
                             point1={'x': 0, 'y': 500},
                             point2={'x': 0, 'y': 480}, gravity_on=self.gravity)

    def start(self):
        if self.gravity:
            self.monkey.drop_monkey()
        self.banana.launch_banana()

    @staticmethod
    def change_gravity():
        gravity_on()

    def game_loop(self):
        loop = True
        run = False

        while loop:

            self.out_of_bounds()

            self.screen.draw_screen()
            self.monkey.draw_monkey()
            self.banana.draw_banana()

            if self.monkey.point1['y'] <= 500 and run:
                self.start()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    loop = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        run = True

                    if event.key == pygame.K_1:
                        self.change_gravity()
                        del_engine(self)
                        loop = False

            pygame.display.flip()

            time.sleep(0.05)


def del_engine(engine):
    del engine


def gravity_on():
    while True:
        gravity = input("Would you like gravity (y/n)")
        if gravity.lower() == 'n':
            gravity = False
            Engine(gravity=gravity).game_loop()
            break

        if gravity.lower() == 'y':
            gravity = True
            Engine(gravity=gravity).game_loop()
            break


pygame.init()

if __name__ == '__main__':
    gravity_on()
