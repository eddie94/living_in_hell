import pygame
from execution import *

def nogada_effect(char):
    nogada_stone = object()
    nogada_stone_design = nogada_stone.set_design("D:\학업자료\pycharm\hell_josun\images\map\노가다\stone.png")
    stone_surface = pygame.Surface([30,30])
    stone_rect1 = stone_surface.get_rect(center = char.rect.center)
    stone_rect2 = stone_surface.get_rect(center = char.rect.center)
    stone_rect3 = stone_surface.get_rect(center = char.rect.center)
    stone_rect4 = stone_surface.get_rect(center = char.rect.center)

    for i in range(50):
        stone_rect1 = stone_rect1.move([0,-2])
        stone_rect2 = stone_rect2.move([0,2])
        stone_rect3 = stone_rect3.move([2,0])
        stone_rect4 = stone_rect4.move([-2,0])
        screen.blit(nogada_stone_design, stone_rect1)
        screen.blit(nogada_stone_design, stone_rect2)
        screen.blit(nogada_stone_design, stone_rect3)
        screen.blit(nogada_stone_design, stone_rect4)
        pygame.display.flip()