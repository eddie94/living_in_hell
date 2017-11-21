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

char_size = [31,48]

up = [0, -2]
down = [0, 2]
right = [2, 0]
left = [-2, 0]
stay = [0,0]

class make_char():

    def __init__(self):

        self.HP = 5
        self.atk_rate = 0.5
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