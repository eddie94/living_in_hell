import pygame,sys
from Design import map
from execution import *
from in_game import afios
from sub_func import *

# size = width, height = 1280,720
# white = 255,255,255
# screen = pygame.display.set_mode(size)
#
# font = pygame.font.SysFont('Arial',40)
text = 'GET THE GAME STARTED'
text2 = 'GO TO HELL'
textsurface1 = font.render(text, False, (0,0,0))
textsurface2 = font.render(text2, False, (0,0,0))

def title():
    done = False
    select_bar_pos = 0
    select_bar = pygame.image.load("D:\학업자료\pycharm\hell_josun\images\select_bar.png")
    title_image = pygame.image.load("D:\학업자료\pycharm\hell_josun\images\Title.png")
    select_bar_rect = select_bar.get_rect()
    select_bar_rect.bottom = height

    while not done:

        for ev in pygame.event.get():
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_RIGHT:
                    select_bar_rect.right=width
                if ev.key == pygame.K_LEFT:
                    select_bar_rect.left=0
                if ev.key == pygame.K_SPACE:
                    if select_bar_rect.left < 30:
                        select_bar_pos = 1
                        done = True
                    elif select_bar_rect.left > 30:
                        select_bar_pos = 0
                        done = True
                    else:
                        pass
                if ev.type == pygame.QUIT:
                    sys.exit()

        screen.fill(white)
        screen.blit(select_bar,select_bar_rect)
        screen.blit(title_image, (425, 30))
        screen.blit(textsurface1, (100,600))
        screen.blit(textsurface2, (900, 600))
        pygame.display.flip()

    return select_bar_pos

def char_select():
    map_base = pygame.image.load("D:\학업자료\pycharm\hell_josun\images\map\map_base.gif")
    arrow_left = pygame.image.load("D:\학업자료\pycharm\hell_josun\images\Arrow_left.jpg")
    arrow_right = pygame.image.load("D:\학업자료\pycharm\hell_josun\images\Arrow_right.jpg")
    char1 = pygame.image.load("D:\학업자료\pycharm\hell_josun\images\character_design\Afios\Afios_standard_left.jpg")

    char_list = [char1]

    pos = 0

    char_name_list = ["Afios"]
    char_name_text_surface = font.render(char_name_list[pos], False, (0,0,0))

    select_done = False

    while not select_done:

        for ev in pygame.event.get():
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_RIGHT:
                    if pos+1 < len(char_list):
                        pos += 1
                    else:
                        pos = 0
                if ev.key == pygame.K_LEFT:
                    if pos-1 > -len(char_list):
                        pos -= 1
                    else:
                        pos = -1
                if ev.key == pygame.K_SPACE:
                    my_char_name = char_name_list[pos]
                    image_list = get_char_image(my_char_name)
                    char_class = get_char(my_char_name)
                    return [image_list, char_class]     #call this char_list
            if ev.type == pygame.QUIT:
                sys.exit()

        screen.fill(white)
        screen.blit(arrow_left,(0,210))
        screen.blit(arrow_right,(980,210))
        # 캐릭터는 항상 640, 360에 둘것

        screen.blit(char_list[pos], (640,360))
        screen.blit(char_name_text_surface,(600,600))
        pygame.display.flip()