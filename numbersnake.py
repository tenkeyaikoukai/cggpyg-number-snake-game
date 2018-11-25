
import pygame
import pygame.mixer
import time
import random
from syslogic import CGGPYG

class NumberSnake:

    def __init__(self):
        self.mx=0
        self.my=0
        self.d=1
        self.mtx=[]
        self.currentnum=1
        self.sc=0
        self.gameflag=1
        self.gamestate="title"
        self.cgg=CGGPYG()
        self.beepflag=0
        pygame.mixer.music.load('pingpong1.mp3')
        for i in range(0,21):
            for j in range(0,21):
                self.mtx[len(self.mtx):]=[0]
        for i in range(1,11):
            flag=0
            r1=0
            r2=0
            while(flag==0):
                r1=random.randint(1,17)
                r2=random.randint(1,17)

                """11-19:number 20:my address"""

                if(self.mtx[r2*20+r1]==0):
                    self.mtx[r2*20+r1]=10+i
                    flag=1
        self.mx=r1
        self.my=r2

    def statemanager(self):

        if self.gamestate=="title":

            self.title()

        if self.gamestate=="play":

            self.routine()

        if self.gamestate=="gameover":

            self.gameover()


    def title(self):

        self.cgg.cls()

        self.cgg.setcolor(7)

        self.cgg.printc("number snake the action game",5,5)

        self.cgg.printc("2018 tenkey aikoukai",5,7)

        self.cgg.printc("press ret key",5,9)


    def gameover(self):

        if self.gameflag==2:
            self.cgg.setcolor(2)

            self.cgg.printc("game over",15,10)
        if self.gameflag==3:
            self.cgg.setcolor(5)

            self.cgg.printc("game clear",15,10)
    def keyin(self,key):

        if self.gamestate=="title":

            if key==pygame.K_RETURN:

                self.gamestate="play"

        if self.gamestate=="play":

            if key==pygame.K_LEFT:
                self.d=4 
            if key==pygame.K_RIGHT:
                self.d=2 
            if key==pygame.K_UP:
                self.d=1 
            if key==pygame.K_DOWN:
                self.d=3 
        if self.gamestate=="gameover":

            if key==pygame.K_RETURN:

                self.__init__()

                self.gamestate="title"


 
    def draw(self):
        self.cgg.cls()
        rectcolor=(255,255,255)
        rect=(0,0,608,392)
        pygame.draw.rect(self.cgg.cvs,rectcolor,rect,5)
        for i in range(0,19):
            for j in range(0,19):
                if self.mtx[i*20+j]==1:
                    self.cgg.setcolor(4)
                    self.cgg.put("circle",j,i)
                if self.mtx[i*20+j]==11:
                    self.cgg.setcolor(6)
                    self.cgg.put("1",j,i)
                if self.mtx[i*20+j]==12:
                    self.cgg.setcolor(6)
                    self.cgg.put("2",j,i)
                if self.mtx[i*20+j]==13:
                    self.cgg.setcolor(6)
                    self.cgg.put("3",j,i)
                if self.mtx[i*20+j]==14:
                    self.cgg.setcolor(6)
                    self.cgg.put("4",j,i)
                if self.mtx[i*20+j]==15:
                    self.cgg.setcolor(6)
                    self.cgg.put("5",j,i)
                if self.mtx[i*20+j]==16:
                    self.cgg.setcolor(6)
                    self.cgg.put("6",j,i)
                if self.mtx[i*20+j]==17:
                    self.cgg.setcolor(6)
                    self.cgg.put("7",j,i)
                if self.mtx[i*20+j]==18:
                    self.cgg.setcolor(6)
                    self.cgg.put("8",j,i)
                if self.mtx[i*20+j]==19:
                    self.cgg.setcolor(6)
                    self.cgg.put("9",j,i)
                if i==self.my and j==self.mx:
                    self.cgg.setcolor(7)
                    self.cgg.put("circle",j,i)
        self.cgg.setcolor(7)

    def routine(self):
        self.mtx[self.my*20+self.mx]=1
        pygame.mixer.music.play(1)
        time.sleep(0.2)
        pygame.mixer.music.stop()
        """up:1 and clockwork"""

        if self.d==1:
            self.my=self.my-1
        if self.d==2:
            self.mx=self.mx+1
        if self.d==3:
            self.my=self.my+1
        if self.d==4:
            self.mx=self.mx-1
        self.draw()
        if self.mtx[self.my*20+self.mx]>10 and self.mtx[self.my*20+self.mx]!=self.currentnum+10 or self.mtx[self.my*20+self.mx]==1 or self.mx<0 or self.mx>19 or self.my<0 or self.my>19:
            self.gameflag=2
            self.gamestate="gameover"

        if self.mtx[self.my*20+self.mx]==self.currentnum+10:
            pygame.mixer.music.load('buzzer.mp3')
            pygame.mixer.music.play(1)
            time.sleep(0.2)
            pygame.mixer.music.stop()
            pygame.mixer.music.load('pingpong1.mp3')
            self.sc=self.sc+1
            self.currentnum=self.currentnum+1
        if self.currentnum>=10:
            self.gamestate="gameover"
            self.gameflag=3

ns=NumberSnake()
endflag=0
while endflag==0:
    ns.statemanager()
    pygame.display.flip() 
    for i in range(0,5):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                endflag=1
            if event.type==pygame.KEYDOWN:

                ns.keyin(event.key)
        time.sleep(0.1)

