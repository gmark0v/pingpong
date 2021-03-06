from pygame import *
from random import randint
#?окно и фпс
fpsiki = time.Clock()
FPS = 60
okno = display.set_mode((700, 500))
#?фон
background = transform.scale(image.load("FON.png"), (700, 500))
#?классы
class objekt(sprite.Sprite): #*основной класс
    def __init__(self, pic, px, py, ph, pw):    
        super().__init__()
        self.image = transform.scale(image.load(pic), (pw, ph))
        self.rect = self.image.get_rect()
        self.rect.x = px
        self.rect.y = py
    def reset(self):
        okno.blit(self.image, (self.rect.x, self.rect.y))
class playir(objekt): #*игрок
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_s] and self.rect.y < 480 - 50: #вниз
            self.rect.y += 6
        if keys_pressed[K_w] and self.rect.y > 50 - 50: #вверх
            self.rect.y -= 6
gg = playir("sprite2.png", 25, 100, 65, 65)
class playir2(objekt): #*игрок2
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_DOWN] and self.rect.y < 480 - 50: #вниз
            self.rect.y += 6
        if keys_pressed[K_UP] and self.rect.y > 50 - 50: #вверх
            self.rect.y -= 6
g2g = playir2("sprite1.png", 625, 100, 65 ,65)
myach = objekt("ball4ik.png", 300, 200, 45, 45)

bsy = 3.5
bsx = -3.5

font.init() #шрифт
font = font.Font(None, 35)

#?игровой цикл
gm = True
while gm:
    myach.rect.x += bsx
    myach.rect.y += bsy
    if myach.rect.y < 0:
        bsy *= -1
    if myach.rect.y > 435:
        bsy *= -1
    okno.blit(background, (0, 0))
    for e in event.get():
        if e.type == QUIT:
            gm = False
#?функции
    myach.update()
    myach.reset()
    gg.update()
    gg.reset()
    g2g.update()
    g2g.reset()
    display.update()
    if sprite.collide_rect(myach, gg): #столкновение мяча и игрока (слево)
        bsx *= -1
        bsy *= -1
    if sprite.collide_rect(myach, g2g): #столкновение мяча и игрока2 (справо)
        bsx *= -1
        bsy *= -1
    ulos = font.render("Игрок 1 проиграл", True, (255, 255, 255))
    ulos2 = font.render("Игрок 2 проиграл", True, (255, 255, 255))
    if myach.rect.x < gg.rect.x - 75:
        game = False
        antifin = True
        while antifin:
            okno.fill((0, 0, 0))
            okno.blit(ulos, (100,100))
            display.update()
            for e in event.get():
                if e.type == QUIT:
                    gm = False
                    antifin = False
    if myach.rect.x > g2g.rect.x + 75:
        game = False
        antifin = True
        while antifin:
            okno.fill((0, 0, 0))
            okno.blit(ulos2, (100,100))
            display.update()
            for e in event.get():
                if e.type == QUIT:
                    gm = False
                    antifin = False
    fpsiki.tick(FPS) 
