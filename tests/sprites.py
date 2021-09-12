"""
Sprites als Person Laden

Sprite:

NAME_FRONT
NAME_FRONT_WALK
NAME_RIGHT
NAME_RIGHT_WALK
NAME_LEFT
NAME_LEFT_WALK
NAME_DOWN
NAME_DOWN_WALk
"""

import pygame
from hitbox import Hitbox

from abc import ABC, abstractmethod

class Object(ABC):

    def __init__(self, x, y, speed):
        self.x, self.y = x, y
        self.speed = speed

    def walk_right(self):
        self.x += self.speed

    def walk_left(self):
        self.x -= self.speed

    def walk_up(self):
        self.y -= self.speed

    def walk_down(self):
        self.y += self.speed


class Sprite(Object):

    def __init__(self, name, path_to_folder, x, y, speed, endung=".png"):

        self.name = name
        self.path_to_folder = path_to_folder
        self.endung = endung

        super().__init__(x, y, speed)


        self.up_pics = [pygame.image.load(path_to_folder+name+"_FRONT"+self.endung), pygame.image.load(path_to_folder+name+"_FRONT_WALK"+self.endung)]
        #self.right_pics = [pygame.image.load(path_to_folder+name+"_RIGHT"), pygame.image.load(path_to_folder+name+"_RIGHT_WALK")]
        #self.left_pics = [pygame.image.load(path_to_folder+name+"_LEFT"), pygame.image.load(path_to_folder+name+"_LEFT_WALK")]
        self.down_pics = [pygame.image.load(path_to_folder+name+"_DOWN"+self.endung), pygame.image.load(path_to_folder+name+"_DOWN_WALK"+self.endung)]

        self.direction = "down"

        self.is_walking = False


    def get_current_image(self):

        if self.direction == "down":
            self.current_image = (self.down_pics[0] if not self.is_walking else self.down_pics[1])
        elif self.direction == "up":
            self.current_image = (self.up_pics[0] if not self.is_walking else self.up_pics[1])
        elif self.direction == "right":
            self.current_image = self.right_pics[0]
        elif self.direction == "left":
            self.current_image = self.left_pics[0]

    def walk_up(self):
        super().walk_up()
        self.direction = "up"
        self.walking()

    def walk_down(self):
        super().walk_down()
        self.direction = "down"
        self.walking()

    def walk_right(self):
        super().walk_right()
        self.direction = "right"
        self.walking()

    def walk_left(self):
        super().walk_left()
        self.direction = "left"
        self.walking()

    def walking(self):
        self.is_walking = not self.is_walking

    def draw(self, screen):
        self.get_current_image()
        screen.blit(self.current_image, (self.x, self.y))

class Background(Object):

    def __init__(self, x, y, speed, path):
        super().__init__(x, y, speed)
        self.path = path
        self.img = pygame.image.load(path)

    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))

class Character(Sprite, Hitbox):

    def __init__(self, name, path_to_folder, x, y, speed, width, height, color=(255, 0, 0), endung=".png"):
        Sprite.__init__(self, name, path_to_folder, x, y, speed, endung)
        Hitbox.__init__(self, x, y, width, height, color)
        self.show_hitbox = False
