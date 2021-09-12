import pygame
from sprites import *
from hitbox import Hitbox

pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

ende = False

fps = 30

clock = pygame.time.Clock()

bg = Background(0, 0, 10, "background.jpg")

sprites = []

straub = Character("straub", "C:\\Users\\thass\\python\\TRIANGLE\\tests\\straub\\", 0, 0, 10, 128, 128,)
st = Character("straub", "C:\\Users\\thass\\python\\TRIANGLE\\tests\\straub\\", 0, 400, 10, 128, 128,)
sprites.append(straub)
sprites.append(st)
def redraw():

    screen.fill((255 ,255, 255))
    bg.draw(screen)
    for el in sprites:
        el.draw(screen)
        if el.show_hitbox:
            el.draw_hitbox(screen)
    pygame.display.flip()

chosen_sprite = 0

def other_sprite():
    global chosen_sprite
    chosen_sprite += 1
    if chosen_sprite >=len(sprites):
        chosen_sprite = 0

while not ende:

    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ende = True

    pressed = pygame.key.get_pressed()
    m_pressed = pygame.mouse.get_pressed()

    if pressed[pygame.K_RIGHT]:
        pass
    elif pressed[pygame.K_LEFT]:
        pass
    elif pressed[pygame.K_DOWN]:
        sprites[chosen_sprite].walk_down()
    elif pressed[pygame.K_UP]:
        sprites[chosen_sprite].walk_up()

    if m_pressed[0]:
        other_sprite()
    if m_pressed[2]:
        sprites[chosen_sprite].show_hitbox = not sprites[chosen_sprite].show_hitbox

    for el in sprites:
        for x in sprites:
            print(el.is_colliding(x))


    redraw()

pygame.quit()
