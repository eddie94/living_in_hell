import pygame,sys
from execution import *
from in_game.afios import *

world_size = [280,1000]
height = 720


def quit_op():

    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            sys.exit()

def move_char(size,char):

    pressed = pygame.key.get_pressed()

    up = [0,-2]
    down = [0,2]
    right = [2,0]
    left = [-2,0]

    if pressed[pygame.K_UP]:
        char.image_index = 1
        if char.rect.top > size[1]:
            char.rect = char.rect.move(up)
        elif char.rect.top - 2 < size[1]:
            char.rect.top = size[1]
        else:
            pass
    if pressed[pygame.K_DOWN]:
        char.image_index = 0
        if char.rect.bottom < size[3]:
            char.rect = char.rect.move(down)
        elif char.rect.bottom +2 > size[3]:
            char.rect.bottom = size[3]
        else:
            pass
    if pressed[pygame.K_LEFT]:
        char.image_index = 2
        if char.rect.left > size[0]:
            char.rect = char.rect.move(left)
        elif char.rect.left -2 < size[0]:
            char.rect.left = size[0]
        else:
            pass
    if pressed[pygame.K_RIGHT]:
        char.image_index = 3
        if char.rect.right < size[2]:
            char.rect = char.rect.move(right)
        elif char.rect.right > size[2]:
            char.rect.right = size[2]
        else:
            pass

def blit_alpha(target, source, location, opacity):

    x = location[0]
    y = location[1]
    temp = pygame.Surface((source.get_width(), source.get_height())).convert()
    temp.blit(target, (-x,-y))
    temp.blit(source, (0,0))
    temp.set_alpha(opacity)
    target.blit(temp, location)

def get_char_image(name):

    if name == "Afios":
        image = [afios_standard_forward, afios_standard_back, afios_standard_left, afios_standard_right]
        return image

def get_char(name):

    if name == "Afios":
        mychar = afios
        return mychar


def info(char):

    info_end = True

    money_surface = font.render("my cash : %s" %(char.money), False, (0,0,0))
    str_surface = font.render("my strength : %s" %(char.str), False, (0,0,0))
    charm_surface = font.render("my charm : %s" %(char.charm), False, (0,0,0))
    int_surface = font.render("my intelligence : %s" %(char.int), False, (0,0,0))
    job_surface = font.render("my job : %s" %(char.job), False, (0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_i:
                while not info_end:
                    if event.type == pygame.KEYDOWN:
                        info_end = True
                    pygame.draw.rect(screen, white, (490,210,300,300), 5)
                    screen.blit(money_surface, (520, 220))
                    pygame.display.flip()