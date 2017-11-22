import pygame,sys
from Design.character.character import *
from sub_func import *
from in_game.afios import *
from execution import *

room_floor = object()
room_floor_design=room_floor.set_design("D:\학업자료\pycharm\hell_josun\images\map\Room_floor.jpg")
room_floor_size = room_floor.set_size(440,160,400,400)
wood_floor = pygame.image.load("D:\학업자료\pycharm\hell_josun\images\map\wood_floor.jpg")
#room_floor = pygame.image.load("D:\학업자료\pycharm\hell_josun\images\map\Room_floor.jpg")
black = 0,0,0
size = width, height = 1280,720
screen = pygame.display.set_mode(size)
world_size = [720,720]

map_id=[0]
'''
map_id has the number of each rooms
my room = 0
world map = 1
conv_store = 2
world map 2 = 3
nogada = 4
'''

def stage1(char_list):              #remember char_list[0] is image_list
                                    #         char_list[1] is the CLASS character
    mychar = char_list[1]
    stage_end = False

    while not stage_end:
        #print(image)
        quit_op()
        move_char(room_floor_size,char_list[1])
        info(mychar)

        stage_end = stage1_design(mychar)
        screen.blit(char_list[0][mychar.image_index], mychar.rect)
        #blit_alpha(screen, char_list[0][char_list[1].image_index], char_rect, 500)  #char_list[1].pos

        pygame.display.flip()

def stage1_design(char):

    red_carpet = object()
    red_carpet_design=red_carpet.set_design("D:\학업자료\pycharm\hell_josun\images\map\Red_carpet.gif")
    red_carpet_size=red_carpet.set_size(740,160,100,50)

    # red_carpet_rect = red_carpet_design.get_rect()
    # red _carpet_rect.right = room_floor_size[2]
    # red_carpet_rect.top = room_floor_size[1]

    if char.rect.top == red_carpet.rect.top and char.rect.left >red_carpet.rect.left:
        char.locus = [0,1,0]
        return True

    screen.fill(black)
    screen.blit(room_floor_design, (440, 160))
    screen.blit(red_carpet_design, red_carpet.rect)

def Game_start(mychar):

    quit_op()

    move_rooms(mychar)

def world_map(char_list):
    '''
    :param char_list[0]:캐릭터 이미지 파일 리스트
    :param cjar_list[1]: 클래스 캐릭터
    '''

    stage_end = False

    mychar = char_list[1]

    world_map_floor = object()
    world_map_floor_design = world_map_floor.set_design("D:\학업자료\pycharm\hell_josun\images\map\world_map_floor.jpg")
    world_map_floor_size = world_map_floor.set_size(0,0,1280,720)
    red_carpet = object()
    red_carpet_design = red_carpet.set_design("D:\학업자료\pycharm\hell_josun\images\map\Red_carpet.gif")
    red_carpet_size = red_carpet.set_size(550,670,100,50)

    object_list = [nogada,conv_store]

    while not stage_end:
        quit_op()
        # if not mychar.rect.colliderect(conv_store.rect):
        #     move_char(world_map_floor_size,char_list[1])
        mychar.move(object_list,world_map_floor_size)
        print(mychar.rect)
        #print(mychar.rect.left in range(nogada.rect.left, nogada.rect.right) or mychar.rect.right in range(nogada.rect.left, nogada.rect.right))
        #print(conv_store.rect, nogada.rect)
        screen.blit(world_map_floor_design,(0,0))
        screen.blit(red_carpet_design, red_carpet.rect)
        screen.blit(conv_store_design, (0,0))
        screen.blit(conv_store_carpet_design,(315,312))
        screen.blit(nogada_design, nogada.rect)
        screen.blit(char_list[0][mychar.image_index], mychar.rect)
        pygame.display.flip()

        if mychar.rect.bottom == red_carpet.rect.bottom and mychar.rect.right < red_carpet.rect.right and mychar.rect.left > red_carpet.rect.left:
            mychar.locus = [1,0,0]
            stage_end = True
        if mychar.rect.top == 312 and mychar.rect.left in range(316,392):
            mychar.locus = [1,2,0]
            stage_end = True
        if mychar.rect.right == 1280:
            mychar.locus = [1,3,0]
            stage_end = True


def store(char_list):
    '''
    편의점 map_id : 2
    :return:
    '''
    mychar = char_list[1]
    stage_end = False

    store_floor = object()
    store_floor_design = store_floor.set_design("D:\학업자료\pycharm\hell_josun\images\map\conv_floor.jpg")
    store_floor_size = store_floor.set_size(340,60,600,600)

    fake_object = object()              #move를 위한 더미 오브젝트 추후 수정 필요
    fake_object.set_size(0,0,0,0)

    while not stage_end:
        object_list = [fake_object]
        quit_op()

        mychar.move(object_list,store_floor_size)

        if mychar.rect.bottom == 660 and mychar.rect.left in range(340,408):
            mychar.locus = [2,1,0]
            stage_end = True

        screen.fill(black)
        screen.blit(store_floor_design,store_floor.rect)
        screen.blit(conv_store_carpet_design, (340,610))
        screen.blit(char_list[0][mychar.image_index],mychar.rect)
        pygame.display.flip()

def world_map2():
    '''
    world_map map_id = 3
    :return:
    '''
    pass


def move_rooms(char_list):

    previous_map_id = char_list[1].locus[0]
    next_map_id = char_list[1].locus[1]

    if char_list[1].locus[2] == 1:
        char_list[1].locus[2] = 0
        char_list[1].surface.get_rect(center=(640,360))
        stage1(char_list)
        return 0

    if previous_map_id == 0 and next_map_id == 1:      #from my room to world map
        char_list[1].rect.top = 650
        char_list[1].rect.left = 590
        world_map(char_list)
    elif previous_map_id == 1 and next_map_id == 0:
        char_list[1].rect.top = 200
        char_list[1].rect.left = 775
        stage1(char_list)
    elif previous_map_id == 1 and next_map_id == 2:
        char_list[1].rect.bottom = 640
        char_list[1].rect.left = 370
        store(char_list)
    elif previous_map_id == 2 and next_map_id == 1:
        char_list[1].rect.top = 320
        char_list[1].rect.left = 355
        world_map(char_list)
    elif previous_map_id == 1 and next_map_id == 3:
        char_list[1].rect.left = 0
        world_map(char_list)