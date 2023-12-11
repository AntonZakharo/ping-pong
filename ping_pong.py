from pygame import *
window = display.set_mode((700,500))
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
background = transform.scale(image.load('kosmos.jpg'),(700,500))
clock = time.Clock()
platform_l = Player('platform l.png',3,75,200,30,120)
platform_r = Player('platform r.png',3,625,200,30,120)
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
        clock.tick(60)
        display.update()
