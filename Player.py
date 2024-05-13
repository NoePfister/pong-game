import Game
import Ball
import pygame as pg


class Player:
    def __init__(self,is_left: bool, screen, game :Game):
        self.is_left=is_left
        self.screen = screen
        self.pos = [0,0]
        self.width = 10
        self.height = 100
        self.game = game
        self.setup()

    def setup(self):
        if self.is_left:
            self.pos = [0,(500-self.height)/2]
        else:
            self.pos = [1000-self.width,(500-self.height)/2]

    def draw(self):
        pg.draw.rect(self.screen, (255,255,255), (self.pos[0],self.pos[1],self.width,self.height))


    def move(self,y:int):
        if not self.check_bounds(self.pos[1]+y): return
        self.pos[1] += y/5

    def check_bounds(self, y: int):
        if (y<0 or y>(500-self.height)):return False
        return True


