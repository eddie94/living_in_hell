import pygame
'''
make_char() 클래스의 locus(이후 궤적)는 캐릭터가 방을 이동할때의 정보를 담고있다.
궤적의 첫번째 요소는 자기가 있었던 방의 id,
       두번째 요소는 자기가 이동할 방의 id
       세번째 요소는 캐릭터를 처음 생성했을때 생기는 이벤트 용이다
궤적을 사용할 때는 방이동을 하는 오브젝트에 부딛혔을때 
다음방의 정보를 덮어쓰면 된다.
마찬가지로 방에 들어오게 되면 첫번째 요소의 값을 덮어쓰면 된다
'''

pygame.font.init()

size = width, height = 1280,720
white = 255,255,255
screen = pygame.display.set_mode(size)
font = pygame.font.SysFont('Arial',40)

char_size = [31,48]

up = [0, -2]
down = [0, 2]
right = [2, 0]
left = [-2, 0]
stay = [0,0]

class make_char():

    def __init__(self):

        self.money = 0
        self.str = 0
        self.charm = 0
        self.int = 0
        self.job = ''
        self.speed = 2
        self.name = ''
        self.size = [31,48]
        self.image_index = 0
        self.locus = [0,1,1]
        self.surface = pygame.Surface(char_size)
        self.rect = self.surface.get_rect(center=(640,360))

    def set_design(self,file_name):

        char = pygame.image.load(file_name)

        return char

    def char_name(self,name):

        self.name = name

    def char_rect(self,image):
        return image.get_rect()

    def check_collision(self,obstacle):

        if self.rect.colliderect(obstacle):

            move_up = self.rect.move(up)
            move_down = self.rect.move(down)
            move_left = self.rect.move(left)
            move_right = self.rect.move(right)

            check_top = move_up.top < obstacle.bottom
            check_bot= move_down.bottom > obstacle.top
            check_left=move_left.left < obstacle.right
            check_right=move_right.right > obstacle.left

            if check_top and not(check_bot and check_left and check_right):
                self.rect = self.rect.move(stay)
            elif check_bot and not(check_right and check_left and check_top):
                self.rect = self.rect.move(stay)

    def move(self,object_list,size):

        pressed = pygame.key.get_pressed()

        money_surface = font.render("my cash : %s" % (self.money), False, (0, 0, 0))
        str_surface = font.render("my strength : %s" % (self.str), False, (0, 0, 0))
        charm_surface = font.render("my charm : %s" % (self.charm), False, (0, 0, 0))
        int_surface = font.render("my intelligence : %s" % (self.int), False, (0, 0, 0))
        job_surface = font.render("my job : %s" % (self.job), False, (0, 0, 0))

        if pressed[pygame.K_UP]:
            self.image_index = 1
            next_move = self.rect.move(up)
            if self.rect.top > size[1]:
                ok=[]
                for ob in object_list:
                    if next_move.colliderect(ob):
                        ok.append(1)
                    else:
                        ok.append(0)
                if sum(ok)==0:
                    if next_move.top < size[1]:
                        self.rect.top = size[1]
                    else:
                        self.rect = self.rect.move(up)
        if pressed[pygame.K_DOWN]:
            self.image_index = 0
            next_move = self.rect.move(down)
            if self.rect.bottom < size[3]:
                ok=[]
                for ob in object_list:
                    if next_move.colliderect(ob):
                        ok.append(1)
                    else:
                        ok.append(0)
                if sum(ok)==0:
                    if next_move.bottom > size[3]:
                        self.rect.bottom = size[3]
                    else:
                        self.rect = self.rect.move(down)
        if pressed[pygame.K_LEFT]:
            self.image_index = 2
            next_move = self.rect.move(left)
            if self.rect.left > size[0]:
                ok=[]
                for ob in object_list:
                    if next_move.colliderect(ob):
                        ok.append(1)
                    else:
                        ok.append(0)
                if sum(ok)==0:
                    if next_move.left < size[0]:
                        self.rect.left = size[0]
                    else:
                        self.rect = self.rect.move(left)
        if pressed[pygame.K_RIGHT]:
            self.image_index = 3
            next_move = self.rect.move(right)
            if self.rect.right < size[2]:
                ok=[]
                for ob in object_list:
                    if next_move.colliderect(ob):
                        ok.append(1)
                    else:
                        ok.append(0)
                if sum(ok)==0:
                    if next_move.right > size[2]:
                        self.rect.right = size[2]
                    else:
                        self.rect = self.rect.move(right)


class object():

    def __init__(self):
        self.width = 0
        self.height = 0
        self.surface = pygame.Surface([self.width, self.height])
        self.rect = self.surface.get_rect()

    def set_design(self,name):

        design = pygame.image.load(name)
        return design

    def set_size(self,width, height,x_length,y_length):

        '''
        :param width: 왼쪽 변의 위치
        :param height: 위쪽 변의 위치
        :param x_length: 오른쪽으로의 길이
        :param y_length: 위쪽으로의 길이
        '''

        self.surface = pygame.Surface([x_length, y_length])
        self.rect = self.surface.get_rect(top=height,left=width, bottom=height+y_length, right = width+x_length)
        return [width,height,width+x_length, height+y_length]