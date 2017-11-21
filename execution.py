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