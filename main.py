from Design.design import *
import execution
from Design.map import *

size = width, height = 1280,720
screen = pygame.display.set_mode(size)

done = False
game_done = False

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    title_select = title()

    if title_select == 1:
        mychar=char_select()
    elif title_select == 0:
        sys.exit()
    else:
        pass

    while not game_done:
        Game_start(mychar)