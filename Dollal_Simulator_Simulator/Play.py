import pygame
import random
import math
import sys
from pygame.locals import *

width = 800
height = 720
value_of_dollal = 350
dollals = 10
money = 0
lowerVal = random.choice((-1,-2,-3,-4))
upperVal = random.choice((1,2,3,4,5))

pygame.init()

screen = pygame.display.set_mode((width, height))
grid = pygame.image.load('grid.png').convert_alpha()
pygame.display.set_caption("Dollal Simulator Simulator")

def update():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

class buyButton(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load("buy.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 25
        self.rect.y = 605

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
            if dollals == 0 and money == 0:
                exit()

class sellButton(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load("sell.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 775-self.rect.width
        self.rect.y = 605

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
            if dollals == 0 and money == 0:
                exit()

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
            self.rect.x = 0
            self.rect.y = 300
            value_of_dollal = 500
            lowerVal = random.choice((-1,-2,-3,-4))
            upperVal = random.choice((1,2,3,4,5))

    def randomTick(self):
        global lowerVal
        global upperVal
        self.tick += 1
        if self.tick == 50:
            lowerVal = random.choice((-1,-2,-3,-4))
            upperVal = random.choice((1,2,3,4,5))
            self.tick = 0
def the_text():
    font = pygame.font.SysFont("freeserif", 20)
    textSurface = font.render(f"Dollals: {dollals}", 1, pygame.Color(0,0,0))
    r = textSurface.get_rect()
    screen.blit(textSurface,(width/2-r.width/2, 665))
    textSurface = font.render(f"Money: ${money}", 1, pygame.Color(0,0,0))
    r = textSurface.get_rect()
    screen.blit(textSurface,(width/2-r.width/2, 695))
    pygame.display.update()

def white_box():
    box = pygame.image.load('whiteBox.png').convert_alpha()
    b = box.get_rect()
    screen.blit(box, (width/2-b.width/2,600))

buy = buyButton()
sell = sellButton()
dot = the_value_line()

screen.fill(pygame.Color(255,255,255))
screen.blit(grid, (0,0))

while True:
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
