#This amazing re-creation of dollal simulator was programmed by Boyd Kirkman
import pygame
import random
import math
import sys
from time import sleep
from pygame.locals import *

width = 800
height = 700
value_of_dollal = 350
dollals = 10
money = 0
lowerVal = random.choice((-1,-2,-3,-4))
upperVal = random.choice((1,2,3,4,5,6))
day = 1

pygame.init()

screen = pygame.display.set_mode((width, height))
grid = pygame.image.load('grid.png').convert_alpha()
pygame.display.set_caption("Dollal Simulator Simulator")

def update():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

def dayScreen():
    R = random.randrange(0,256)
    G = random.randrange(0,256)
    B = random.randrange(0,256)
    screen.fill(pygame.Color(R,G,B))
    font = pygame.font.SysFont("freeserif", 67)
    textSurface = font.render("Day "+str(day), 1, pygame.Color(0,0,0))
    r = textSurface.get_rect()
    screen.blit(textSurface,(width/2-r.width/2, height/2-r.height/2))
    pygame.display.update()
    update()
    sleep(2)
    global value_of_dollal
    value_of_dollal = 350
    game()



class buyButton(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load("buy.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 25
        self.rect.y = 600

    def clicked(self):
        global money
        global dollals
        global value_of_dollal
        x,y = pygame.mouse.get_pos()
        if x >= self.rect.x and x <= self.rect.x+self.rect.width:
            Mouse_Location_X = True
        if x < self.rect.x or x > self.rect.x+self.rect.width:
            Mouse_Location_X = False
        if y >= self.rect.y and y <= self.rect.y+self.rect.height:
            Mouse_Location_Y = True
        if y < self.rect.y or y > self.rect.y+self.rect.height:
            Mouse_Location_Y = False
        if pygame.mouse.get_pressed()[0] and Mouse_Location_X == True and Mouse_Location_Y == True and money >= value_of_dollal:
            money -= value_of_dollal
            dollals += 1
            if money < 0:
                money = 0
            if dollals < 0:
                dollals = 0

class sellButton(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load("sell.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 775-self.rect.width
        self.rect.y = 600

    def clicked(self):
        global money
        global dollals
        global value_of_dollal
        x,y = pygame.mouse.get_pos()
        if x >= self.rect.x and x <= self.rect.x+self.rect.width:
            Mouse_Location_X = True
        if x < self.rect.x or x > self.rect.x+self.rect.width:
            Mouse_Location_X = False
        if y >= self.rect.y and y <= self.rect.y+self.rect.height:
            Mouse_Location_Y = True
        if y < self.rect.y or y > self.rect.y+self.rect.height:
            Mouse_Location_Y = False
        if pygame.mouse.get_pressed()[0] and Mouse_Location_X == True and Mouse_Location_Y == True and dollals > 0:
            money += value_of_dollal
            dollals -= 1
            if money < 0:
                money = 0
            if dollals < 0:
                dollals = 0

class the_value_line(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load("dot.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 300
        self.tick = 0

    def move(self):
        global lowerVal
        global upperVal
        global screen
        global grid
        self.rect.x += 1
        oldY = self.rect.y
        self.rect.y += random.randrange(lowerVal,upperVal)
        newY = self.rect.y
        global value_of_dollal
        value_of_dollal += oldY - newY
        if self.rect.x == 800-self.rect.width:
            screen.fill(pygame.Color(255,255,255))
            screen.blit(grid, (0,0))
            global playing
            playing = False
            global day
            day += 1
            dayScreen()

    def randomTick(self):
        global lowerVal
        global upperVal
        self.tick += 1
        if self.tick == 100:
            lowerVal = random.choice((-1,-2,-3,-4))
            upperVal = random.choice((1,2,3,4,5,6))
            self.tick = 0

def the_text():
    font = pygame.font.SysFont("freeserif", 20)
    textSurface = font.render("Dollals: "+str(dollals), 1, pygame.Color(0,0,0))
    r = textSurface.get_rect()
    screen.blit(textSurface,(width/2-r.width/2, 625))
    textSurface = font.render("Money: $"+str(money), 1, pygame.Color(0,0,0))
    r = textSurface.get_rect()
    screen.blit(textSurface,(width/2-r.width/2, 655))
    pygame.display.update()

def white_box():
    box = pygame.image.load('whiteBox.png').convert_alpha()
    b = box.get_rect()
    screen.blit(box, (width/2-b.width/2,600))

def title():
    font = pygame.font.SysFont("freeserif", 67)
    textSurface = font.render("Dollal Simulator Simulator", 1, pygame.Color(0,0,0))
    r = textSurface.get_rect()
    screen.blit(textSurface,(width/2-r.width/2, height/2-r.height/2))
    pygame.display.update()

def TitleScreen():
    R = random.randrange(0,256)
    G = random.randrange(0,256)
    B = random.randrange(0,256)
    screen.fill(pygame.Color(R,G,B))

    title()
    update()
    sleep(2)
    dayScreen()


buy = buyButton()
sell = sellButton()
dot = the_value_line()

def game():
    screen.fill(pygame.Color(255,255,255))
    screen.blit(grid, (0,0))
    global playing
    playing = True
    dot.rect.x = 0
    dot.rect.y = 300

    while playing:
        screen.blit(buy.image, buy.rect)
        screen.blit(sell.image, sell.rect)
        buy.clicked()
        sell.clicked()
        screen.blit(dot.image, dot.rect)
        dot.move()
        dot.randomTick()
        white_box()
        the_text()
        update()
        pygame.display.update()
        print(value_of_dollal)

if __name__ == "__main__":
    TitleScreen()
