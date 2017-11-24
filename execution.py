import pygame
from Design.character.character import *

pygame.init()
pygame.font.init()

char_size = [31,48]

size = width, height = 1280,720
white = 255,255,255
screen = pygame.display.set_mode(size)

font = pygame.font.SysFont('Arial',40)

conv_store = object()
conv_store_design = pygame.image.load("D:\학업자료\pycharm\hell_josun\images\map\Conv_store.jpg")
conv_store_carpet_design = pygame.image.load("D:\학업자료\pycharm\hell_josun\images\map\Conv_store_carpet.gif")
conv_store.set_size(0,0,579,312)

nogada = object()
nogada_design = nogada.set_design("D:\학업자료\pycharm\hell_josun\images\map\노가다.png")
nogada_size = nogada.set_size(580,0,340,320)

world_map_floor = object()
world_map_floor_design = world_map_floor.set_design("D:\학업자료\pycharm\hell_josun\images\map\world_map_floor.jpg")
world_map_floor_size = world_map_floor.set_size(0,0,1280,720)

fake_object = object()              #move를 위한 더미 오브젝트 추후 수정 필요
fake_object.set_size(0,0,0,0)

nogada_door = object()
nogada_door_design = nogada_door.set_design("D:\학업자료\pycharm\hell_josun\images\map\노가다_문.jpg")
nogada_door_size = nogada_door.set_size(720,260,100,60)

nogada_floor = object()
nogada_floor_design = nogada_floor.set_design("D:\학업자료\pycharm\hell_josun\images\map\노가다_바닥.jpg")
nogada_floor_size = nogada_floor.set_size(340,60,600,600)

nogada_carpet = object()
nogada_carpet_design = nogada_carpet.set_design("D:\학업자료\pycharm\hell_josun\images\map\안전제일.gif")
nogada_carpet_size = nogada_carpet.set_size(340,610,100,50)

stone = object()
stone_design = stone.set_design("D:\학업자료\pycharm\hell_josun\images\stone.png")
stone_size = stone.set_size(500,50,300,300)

nogada_explain = pygame.Surface([524,77])
nogada_explain_design = pygame.image.load("D:\학업자료\pycharm\hell_josun\images\map\노가다\설명.jpg")
nogada_explain_rect = nogada_explain_design.get_rect(top=0, left=378)