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

# def move_char(char, size):  # size는 width, height로 구성된 리스트

    # up=[0,-char.speed]
    # down=[0,char.speed]
    # right=[char.speed,0]
    # left=[-char.speed,0]
    #
    # pressed = pygame.key.get_pressed()
    #
    # if pressed[pygame.K_UP]:
    #     if char.pos[1] + up[1] > size[1]:
    #         char.pos[1] += up[1]
    #     elif char.pos[1] + up[1] < size[3]:
    #         char.pos[1] = size[1]
    #     else:
    #         pass
    #     char.image_index = 1
    # if pressed[pygame.K_DOWN]:
    #     if char.pos[1] + char.size[1] + down[1] <= size[3]:
    #         char.pos[1] += down[1]
    #     elif char.pos[1] + char.size[1] + down[1] > size[3]:
    #         char.pos[1] = size[3] - char.size[1]
    #     else:
    #         pass
    #     char.image_index = 0
    # if pressed[pygame.K_RIGHT]:
    #     if char.pos[0] + char.size[0] + right[0] <= size[2]:
    #         char.pos[0] += right[0]
    #     elif char.pos[0] + char.size[0] + right[0] > size[1]:
    #         char.pos[0] = size[2] - char.size[0]
    #     else:
    #         pass
    #     char.image_index = 3
    # if pressed[pygame.K_LEFT]:
    #     if char.pos[0] + left[0] > size[0]:
    #         char.pos[0] += left[0]
    #     elif char.pos[0] + left[0] < size[0]:
    #         char.pos[0] = size[0]
    #     else:
    #         pass
    #     char.image_index = 2



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

def collision_range(size):
    '''
    size is a list that contains the axis of the obstacle
    '''

    x_range = range(size[0],size[2])
    y_range = range(size[1],size[3])

    return [x_range,y_range]

def collision_check(char_rect, object):
    '''
    check if the character's position is in the range of an obstacle
    '''
    if char_rect.colliderect(object):
        return True
    else:
        return False