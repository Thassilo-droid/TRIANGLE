import pygame

class Hitbox:

    def __init__(self, x, y, width, height, color=(255, 0, 0)):
        self.x, self.y, self.width, self.height = x, y, width, height
        self.color = color

    def is_colliding(self, other):

        if (self.x+self.width >= other.x and self.x+self.width <= other.x+other.width \
            and self.y >= other.y and self.y <= other.y+other.height) or \
            (self.x+self.width >= other.x and self.x+self.width <= other.x+other.width \
                and self.y+self.height >= other.y and self.y+self.height <= other.y+other.height) or\
            (self.x>= other.x and self.x <= other.x+other.width \
                and self.y >= other.y and self.y <= other.y+other.height) or\
            (self.x >= other.x and self.x <= other.x+other.width \
                and self.y+self.height >= other.y and self.y+self.height <= other.y+other.height):
            return True
        else:
            return False

    def draw_hitbox(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 1)
