import pygame,sys, random
from pygame.locals import *
pygame.init()
pygame.font.init()
mainclock= pygame.time.Clock()
window=pygame.display.set_mode((360,560,),0,32)
pygame.display.set_caption('SpaceAce')
score=0
Texty = pygame.font.Font('SUPERPOI_R.TTF', 20)
Textyy = pygame.font.Font('SUPERPOI_R.TTF', 10)
text = Texty.render('score: %d' % score, 0, (0,0,255))
astrfrqnc=1500 # the higher the less frequent
dbfrqc=4000
player=pygame.Rect(170,380,20,20)
shield=False
shipx=pygame.image.load('ship.png')
shadow=[]
blink=255
a=0
pb=[]
db=[]
astroid=[]
drone=[]
drone2=[]
drone3=[]
power=0
p=-250
W=(255,255,255)
B=(0,0,0)
R=(255,0,0)
BL=(0,0,255)
P=(100,100,100)
ms=4
bs=10
ha=0
ba=0
son=0
son2=0
bonus=0
highscore=0



test=False
option=2
counter=0
r=True
r2=True
dronetop=0
dronetop2=0

backspd=1
while True:
    if p>-250:
        p=p-1
    powerbar=pygame.Rect(330,560,20,p)
    counter=counter+1
    window.fill (B)
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
    i=random.randint(0,100)
    son=random.randint(0,70)
    son2=random.randint(0,70)
    son3=random.randint(0,70)
        
    if i>99-counter/astrfrqnc:
        test=True
       
    
    score=counter/10 +bonus
    if test:
        astroid.append(pygame.Rect(random.randint(0,320),0,35,35))
        test=False
    for x in astroid:
        x.top+=5
        pygame.draw.rect(window,P,x)
        if x.top >600:
            astroid.remove(x)
    if counter==120 :
        drone.append(pygame.Rect(0,0,20,20))
    #  if counter==520 :
    #     drone2.append(pygame.Rect(0,0,20,20))
        
        #Vaisseau Enemi    
    for x in drone :
        pygame.draw.rect(window,BL,x)
        x.top+=dronetop
        if r:
            x.left+=2
        if x.left>=340:
            r=False
            dronetop=random.randint(-1,1)
                
        if r==False:
            x.left-=2
        if x.left<=0:
            r=True
            dronetop=random.randint(-1,1)
        if x.top<-10:
            dronetop=1
        if x.top >200:
            dronetop=-1
        if son<=1+counter/dbfrqc:
            db.append(pygame.Rect(x.left,x.top,5,10))
      
        
      
     #Missile Enemi       
    for x in db:
        x.top+=random.randint(3,5)
        pygame.draw.rect(window,R,x)
        if x.top>=580:
            db.remove(x)
            
            
            
                
                
                
                
    
        
        
    mainclock.tick(80)
    pygame.display.update()
