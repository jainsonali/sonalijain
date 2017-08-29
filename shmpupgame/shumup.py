import pygame
import random
import time
from os import path

img_dir=path.join(path.dirname(__file__),'images') 
width=480
height=600
FPS=60
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
transparent=(0,0,0,0)
green=(0,255,0)
blue=(0,0,255)

pygame.init()
pygame.mixer.init()
gameDisplay=pygame.display.set_mode((width,height))
pygame.display.set_caption("SHumup")
clock=pygame.time.Clock()
shootsound=pygame.mixer.Sound(path.join(img_dir,"Laser_shoot.wav"))
front=pygame.image.load(path.join(img_dir,"front.jpg"))
gameover=pygame.image.load(path.join(img_dir,"Game_Over.jpg"))

font_name=pygame.font.match_font('arial')
def text_on_screen(surf,msg,color,size,x,y):
    font=pygame.font.Font(font_name,size)
    text_surface=font.render(msg,True,color)
    text_rect=text_surface.get_rect()
    text_rect.midtop=(x,y)
    surf.blit(text_surface,text_rect)

def start():
    start=True
    while start:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_c:
                    start=False
                if event.key==pygame.K_q:
                    pygame.quit()
                    quit()
        gameDisplay.blit(front,(0,0))
        text_on_screen(gameDisplay,"Press 'C' to Play",white,50,250,220)
        text_on_screen(gameDisplay,"Press'Q' to Quit",white,50,250,320)
        pygame.display.update()
        
def pause():
    paused=True
    while paused:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_c:
                    paused=False
                elif event.key==pygame.K_q:
                    pygame.quit()
                    quit()
        text_on_screen(gameDisplay,"paused",white,40,width/2-50,height/2)
        text_on_screen(gameDisplay,"Press 'C' to continue and 'Q' to quit",white,40,150,height/2+100)
        clock.tick(5)    
    
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.transform.scale(player_img,(50,38))
        self.image.set_colorkey(black)
        self.rect=self.image.get_rect()
        self.radius=20
        self.rect.centerx=width/2
        self.rect.bottom=height-10
        self.speedx=0
    def update(self):
        self.speedx=0
        keystate=pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx= -8
        if keystate[pygame.K_RIGHT]:
            self.speedx=8
        self.rect.x+=self.speedx
        if self.rect.right>width:
            self.rect.right=width
        if self.rect.left<0:
            self.rect.left=0
    def shoot(self):
        bullet= Bullet(self.rect.centerx,self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)
        shootsound.play()
            
        
class mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.transform.scale(mob_img,(25,30))
        self.image.set_colorkey(black)
        self.rect=self.image.get_rect()
        self.radius=int(self.rect.width* .85/2)
        self.rect.x=random.randrange(0,width-self.rect.width)
        self.rect.y=random.randrange(-100,-40)
        self.speedy=random.randrange(1,8)
        self.speedx=random.randrange(-3,3)
    def update(self):
        self.rect.y+=self.speedy
        self.rect.x+=self.speedx
        if self.rect.top>height+10 or self.rect.right>width+20 or self.rect.left<-25:
            self.rect.x=random.randrange(0,width-self.rect.width)
            self.rect.y=random.randrange(-100,-40)
            self.speedy=random.randrange(1,8)
        
class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.transform.scale(bullet_img,(10,50))
        self.image.set_colorkey(black)
        self.rect=self.image.get_rect()
        self.rect.bottom=y
        self.rect.centerx=x
        self.speedy=-10

    def update(self):
        self.rect.y+=self.speedy
        if self.rect.bottom<0:
            self.kill()
        
background=pygame.image.load(path.join(img_dir ,"background.png")).convert()
background_rect=background.get_rect()
player_img=pygame.image.load(path.join(img_dir ,"player.png")).convert()
mob_img=pygame.image.load(path.join(img_dir ,"mob.png")).convert()
bullet_img=pygame.image.load(path.join(img_dir ,"bullet.png")).convert()
        
all_sprites=pygame.sprite.Group()
mobs=pygame.sprite.Group()
bullets=pygame.sprite.Group()
player=Player()
all_sprites.add(player)
for i in range(8):
    m=mob()
    all_sprites.add(m)
    mobs.add(m)

def game_loop():
    score=0
    running=True
    gameOver=False
    while running:
        while gameOver==True:
            gameDisplay.fill(black)
            gameDisplay.blit(gameover,(0,0))
            text_on_screen(gameDisplay,"Score : "+str(score),green,50,width/2+10,220)
            text_on_screen(gameDisplay,"press Q to quit",white,30,250,340)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        gameOver=False
                        running=False
                if event.type==pygame.QUIT:
                    gameOver=False
                    running=False
            
 
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    player.shoot()
                if event.key==pygame.K_p:
                    pause()
        
        all_sprites.update()
        bullet_hit=pygame.sprite.groupcollide(mobs,bullets,True,True)
        for hit in bullet_hit:
            m=mob()
            all_sprites.add(m)
            mobs.add(m)
            score+=5
        hits=pygame.sprite.spritecollide(player,mobs,False,pygame.sprite.collide_circle)
        if hits:
                gameOver=True
            
        gameDisplay.blit(background,background_rect)
        all_sprites.draw(gameDisplay)
        text_on_screen(gameDisplay,"score: "+str(score),white,20,50,10)
        text_on_screen(gameDisplay,"pause: p",white,20,width-250,10)
        text_on_screen(gameDisplay,"continue: c and quit:q",white,20,width-150,10)
        pygame.display.flip()
        
        clock.tick(FPS)

start()
game_loop()
pygame.quit()
quit()
