import sys,pygame
from Design.character.character import *

afios = make_char()
afios_standard_left = afios.set_design("D:\학업자료\pycharm\hell_josun\images\character_design\Afios\Afios_standard_left.jpg")
afios_standard_right = afios.set_design("D:\학업자료\pycharm\hell_josun\images\character_design\Afios\Afios_standard_right.jpg")
afios_standard_forward = afios.set_design("D:\학업자료\pycharm\hell_josun\images\character_design\Afios\Afios_standard_forward.jpg")
afios_standard_back = afios.set_design("D:\학업자료\pycharm\hell_josun\images\character_design\Afios\Afios_standard_back.jpg")
afios.char_name("Afios")