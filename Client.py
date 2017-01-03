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

bugfix1=False
bugfix2=False


shoot=False
test=False
menu=True
game=False
option=1
counter=0
r=True
r2=True
dronetop=0
dronetop2=0

moveleft=False
moveright=False
moveup=False
movedown=False
death=pygame.mixer.Sound('death.wav')
pygame.mixer.music.load('chavmusic.mp3')
pygame.mixer.music.play(-1)
makesound=False
back=[pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5)]
backspd=1
while True:
    while game==False:
        
        moveleft=False
        moveright=False
        moveup=False
        movedown=False
        counter=0
        bonus=0
        astroid=[]
        drone=[]
        drone2=[]
        db=[]
        pb=[]
        p=-250
        player=pygame.Rect(170,380,20,20)
        window.fill (B)
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type== KEYDOWN:
                if event.key== K_DOWN and option==1:
                     option=option-1
               
                if event.key==K_UP and option==1:
                    option=option+1
                elif event.key==K_UP and option==0:
                    option=option+1
# Remplacement event.key==K_RIGHT par event.key==K_RETURN
                if event.key==K_RETURN and option==0:
                    pygame.quit()
                    sys.exit()
                if event.key==K_RETURN and option==1: 
                    game=True
                    score=0
                    
        if option==1:
            player.top=380
        if option==0:
            player.top=440
        for booz in back:
            pygame.draw.rect(window,W,booz)
            booz.top+=backspd
            if booz.top>=500:
                booz.left=random.randint(0,300)
                booz.top=-5
    
            
        f = open('high_score.txt','r')
        highscore = int(f.read() )
        f.close()
        if score>=highscore:
            highscore=int(round(score,0))
            f = open('high_score.txt','w')
            f.write(str(highscore))
            f.close()
            
        
        
        
          
            
        
                 
        
            
                
        text = Texty.render('score: %d' % score, 0, (0,0,255))
        text2 = Texty.render('Highscore: %d' % highscore, 0, (0,0,255))
        text3=  Textyy.render('music by Peter H. ', 0, (0,0,255))
        text4=  Textyy.render('code by chavdar d. ', 0, (0,0,255))
        text5=  Texty.render('space ace ', 0, (255,0,0))
        text6=  Texty.render('start', 0, (255,0,0))
        text7=  Texty.render('quit', 0, (255,0,0))
        text8=  Texty.render('Press ENTER', 0, (0,255,0))
        text9=  Texty.render('to select', 0, (0,255,0))
        
        window.blit(text, (5,0))
        window.blit(text2, (5,50))
        
        window.blit(text3, (5,510))
        window.blit(text4, (5,530))
        
        window.blit(text5, (80,150))
        window.blit(text6, (220,375))
        window.blit(text7, (220,435))
        window.blit(text8, (80,220))
        window.blit(text9, (80,270))
        #pygame.draw.rect(window,R,player)
        window.blit(shipx,(player.left-2,player.top))
        mainclock.tick(30)
        pygame.display.update()
        
    while game :
        
        if p>-250:
            p=p-1
        powerbar=pygame.Rect(330,560,20,p)
        counter=counter+1
        if p>=-1:
            shield=False
        window.fill (B)
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type== KEYDOWN:
                if event.key== K_DOWN:
                    movedown=True
                    moveup=False
                if event.key==K_UP:
                    moveup=True
                    movedown=False
                if event.key==K_RIGHT:
                    moveright=True
                    moveleft=False
                if event.key==K_LEFT:
                    moveright=False
                    moveleft=True
                if event.key== ord('f') and p<=-50:
                    shoot=True
                    
                if event.key== ord('s') and p<=-1:
                    shield=True
                
                
            if event.type==KEYUP:
                if event.key== K_DOWN:
                    movedown=False
                if event.key==K_UP:
                    moveup=False
                if event.key==K_RIGHT:
                    moveright=False
                if event.key==K_LEFT:
                    moveleft=False
                if event.key== ord('s'):
                    blink=255
                    shield=False
                    a=225
                    shadow=[]
        
            
        i=random.randint(0,100)
        son=random.randint(0,70)
        son2=random.randint(0,70)
        if shield==True:
            p=p+5
            ms=6
        else :
            ms=4
        if i>99-counter/astrfrqnc:
            test=True
        if shoot:
            p=p+50
            pb.append(pygame.Rect(player.left+5,player.top,6,16))
            shoot=False
        
        for x in pb:
            x.top-=bs
            pygame.draw.rect(window,BL,x)
            for z in drone:
                if z.colliderect(x):
                    #pygame.mixer.music.play(0,0.0)
                    death.play()
                    makesound=True
                    drone.remove(z)
                    pb.remove(x)
                    bugfix1=True
                    drone.append(pygame.Rect(random.randint(0,340),-40,20,20))
                    bonus=bonus+50
            for z in drone2:
                if z.colliderect(x):
                    #pygame.mixer.music.play(0,0.0)
                    death.play()
                    makesound=True
                    drone2.remove(z)
                    if bugfix1==False:
                        pb.remove(x)
                        bugfix2=True
                    drone2.append(pygame.Rect(random.randint(0,340),-40,20,20))
                    bonus=bonus+50
            for z in astroid:
                if z.colliderect(x):
                    score=score+100
                    astroid.remove(z)
                    if bugfix1==False and bugfix2==False:
                        pb.remove(x)
                    bonus=bonus+3
        
            if x.top<-80:
                pb.remove(x)
        if makesound:
            
            makesound=False
        bugfix1=False
        bugfix2=False
        score=counter/10 +bonus
        if test:
            astroid.append(pygame.Rect(random.randint(0,320),0,35,35))
            test=False
        for booz in back:
            pygame.draw.rect(window,W,booz)
            booz.top+=backspd
            if booz.top>=500:
                booz.left=random.randint(0,355)
                booz.top=-5
        for x in astroid:
            x.top+=5
            pygame.draw.rect(window,P,x)
            if x.colliderect(player)and shield==False:
                game=False
            if x.top >600:
                astroid.remove(x)
        if counter==120 :
            drone.append(pygame.Rect(0,0,20,20))
        if counter==520 :
            drone2.append(pygame.Rect(0,0,20,20))
        
        
            
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
        for w in drone2 :
            pygame.draw.rect(window,BL,w)
            w.top+=dronetop2
            if r2:
                w.left+=2
            if w.left>=340:
                r2=False
                dronetop2=random.randint(-1,1)
                
            if r2==False:
                w.left-=2
            if w.left<=0:
                r2=True
                dronetop2=random.randint(-1,1)
            if w.top<-10:
                dronetop2=1
            if w.top >220:
                dronetop2=-1
            
            if son2<=1+counter/dbfrqc:
                db.append(pygame.Rect(w.left,w.top,5,10))
        
            
            
        for x in db:

            x.top+=random.randint(3,5)
            if x.colliderect(player)and shield==False:
                game=False
            
            pygame.draw.rect(window,R,x)
            if x.top>=580:
                db.remove(x)
            
            
            
                
                
                
                
            

        if moveup and player.top>0:
            player.top-=ms
        if movedown and player.top<540:
            player.top+=ms
        if moveleft and player.left>0:
            player.left-=ms
        if moveright and player.left<340:
            player.left+=ms
        text = Texty.render('score: %d' % score, 0, (0,0,255))   
        window.blit(text, (5,0))
        
        #pygame.draw.rect(window,(255, 0, 0, 122),player)
        
        if shield==False:
            blink=255
        if shield==True:
            blink=blink-20
            if blink <=40:
                blink=255
            shipx.set_alpha(blink)
            a=a+25
            if a==250:
                shadow=[]
                shadow.append(pygame.Rect(player.left,player.top,20,20))
                a=0
        shipx.set_alpha(blink)
            #for i in shadow:
               # pygame.draw.rect(window,pygame.Color(255-a,0,0),i)
        window.blit(shipx,(player.left-2,player.top))
        pygame.draw.rect(window,P,powerbar)
        mainclock.tick(80)
        pygame.display.update()

