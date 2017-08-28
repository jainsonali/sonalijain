import pygame
import random
import time
pygame.init()
screen_x=750
screen_y=512
black=(0,0,0)
green=(3,166,121)
white=(255,255,255)
apple_color=(212,117,0)
gameDisplay=pygame.display.set_mode((screen_x,screen_y))
pygame.display.set_caption('snakkegame')
front=pygame.image.load("front.png")
background=pygame.image.load("background.jpg")
heart=pygame.image.load("heart.png")
pygame.display.update()


clock=pygame.time.Clock()

def message_to_screen(msg,color,displace=0,size=40):
    font_size=size
    textSurf, textRect=text_objects(msg,color,font_size)
    textRect.center=(screen_x/2),((screen_y/2)+displace)
    gameDisplay.blit(textSurf,textRect)
    
def text_objects(text,color,size):
    font=pygame.font.SysFont(None,size)
    textSurf=font.render(text,True,color)
    return textSurf, textSurf.get_rect()

def snake(blocksize,snakelist):
    for XnY in snakelist:
        pygame.draw.rect(gameDisplay,black,[XnY[0],XnY[1],blocksize,blocksize])
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
        gameDisplay.fill(black)
        gameDisplay.blit(front,(0,0))
        message_to_screen("Press 'C' to Play, 'P' to Pause and 'Q' to Quit",(0,170,0),200,50)
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
        message_to_screen("paused",white,-50,60)
        message_to_screen("Press 'C' to continue and 'Q' to quit",white)
        pygame.display.update()
        clock.tick(5)
        
def game_loop():
    gameExit=False
    gameOver=False
    snakelist=[]
    snakelength=1
    lead_x=screen_x/2
    lead_y=screen_y/2
    FPS=15
    change_x = 0
    change_y=0
    blocksize=10
    applethickness=20
    score=0
    apple_x=round(random.randrange(0,screen_x-blocksize)/10.0)*10.0
    apple_y=round(random.randrange(0,screen_y-blocksize)/10.0)*10.0
    while not gameExit:
        while gameOver==True:
            gameDisplay.fill(black)
            message_to_screen("GAME OVER",white,-150,60)
            message_to_screen("Score : "+str(score),white,-50,50)
            message_to_screen("press C to play again and Q to quit",apple_color)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        gameExit=True
                        gameOver=False
                    if event.key==pygame.K_c:
                        gameOver=False
                        game_loop()
                
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gameExit=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    change_x =-blocksize
                    change_y=0
                elif event.key==pygame.K_RIGHT:
                    change_x =+blocksize
                    change_y=0
                elif event.key==pygame.K_UP:
                    change_y=-blocksize
                    change_x=0
                elif event.key==pygame.K_DOWN:
                    change_y=+blocksize
                    change_x=0
                elif event.key==pygame.K_p:
                    pause()
        if lead_x>=screen_x or lead_x<=0 or lead_y>=screen_y or lead_y<=0:
           gameOver=True
        lead_x += change_x
        lead_y +=change_y
        
        gameDisplay.blit(background,(0,0))
        message_to_screen("Score : "+str(score),white,-200,40)
        gameDisplay.blit(heart,(apple_x,apple_y))
       
        snakehead=[]
        snakehead.append(lead_x)
        snakehead.append(lead_y)
        snakelist.append(snakehead)

        if len(snakelist)>snakelength:
            del(snakelist[0])
        for each in snakelist[:-1]:
            if each==snakehead:
                gameOver=True
        snake(blocksize,snakelist)
        pygame.display.update()
        if lead_x>apple_x and lead_x<apple_x+applethickness or lead_x+blocksize>apple_x and lead_x+blocksize <apple_x+applethickness :
            if lead_y>apple_y and lead_y<apple_y+applethickness or lead_y+blocksize>apple_y and lead_y+blocksize <apple_y+applethickness:
                score+=10
                snakelength+=1
                apple_x=round(random.randrange(0,screen_x-blocksize)/10.0)*10.0
                apple_y=round(random.randrange(0,screen_y-blocksize)/10.0)*10.0
            
        clock.tick(FPS)
    
    pygame.quit()
    quit()
start()          
game_loop()
