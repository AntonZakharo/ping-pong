from pygame import *
font.init()
window_height = 500
window_width = 700
window = display.set_mode((window_width,window_height))
display.set_caption('Пинг понг')
class GameSprite(sprite.Sprite):
    def __init__(self,images,speed,x,y,sizex,sizey):
        super().__init__()
        self.image = transform.scale(image.load(images),(sizex,sizey))
        self.rect = self.image.get_rect()
        self.speed = speed
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x,self.rect.y))
class Player(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 390:
            self.rect.y += self.speed
        self.reset()
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 390:
            self.rect.y += self.speed
        self.reset()
class Ball(GameSprite):
    def __init__(self,images,speed,x,y,sizex,sizey,speed_y,speed_x):
        super().__init__(images,speed,x,y,sizex,sizey)
        self.image = transform.scale(image.load(images),(sizex,sizey))
        self.rect = self.image.get_rect()
        self.speed = speed
        self.rect.x = x
        self.rect.y = y
        self.speed_y = speed_y
        self.speed_x = speed_x
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.y > window_height-50 or self.rect.y <= 0:
            self.speed_y *= -1
        if sprite.collide_rect(self,platform_l) or sprite.collide_rect(self,platform_r):
            self.speed_x *= -1
        if self.rect.x > 700 or self.rect.x < 0:
            global finished
            finished = True
            font1 = font.SysFont('Arial', 70)
            defeat = font1.render('Lose', True, (5, 193, 255))
            window.blit(defeat, (250,250))
        self.reset()
background = transform.scale(image.load('kosmos.jpg'),(700,500))
clock = time.Clock()
platform_l = Player('platform l.png',3,75,200,30,120)
platform_r = Player('platform r.png',3,625,200,30,120)
ball = Ball('tennis.png',3,250,150,50,50,3,3)
game = True
finished = False
while game:
    window.blit(background,(0,0))
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finished:
        platform_l.update_l()
        platform_r.update_r()
        ball.update()
        clock.tick(60)
        display.update()
        
