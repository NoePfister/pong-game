import Game
import Player
import Ball
import random
import pygame as pg

class Ball:
    def __init__(self,screen, game: Game):
        self.screen = screen
        self.pos = [500,250]
        self.rad = 10
        self.velocity = [1,0]
        self.game = game

        self.setup()

    def setup(self):
        self.velocity=[1,random.uniform(-1,1)]

    def update(self):
        self.pos[1]+=self.velocity[1]/10
        self.pos[0]+=self.velocity[0]/10
        self.check_collide()

    def draw(self):
        pg.draw.circle(self.screen,(255,255,255),self.pos,self.rad)

    def check_collide(self):
        # Todo: Check if it collides with the player
    # When Ball collides with Player, multiply the x velocity by -1
    # When Ball collides with Wall, multiply the y velocity by -1
    # When Ball collides with Sides, end the game

        # Check if Ball collides with player.
        if self.check_player_collison(self.game.player1) or self.check_player_collison(self.game.player2):
            self.velocity[0] *= -1
            print("Player Collision")
            return
        # Check if Ball is hitting the Wall
        if (self.pos[1] < 0+self.rad) or (self.pos[1] > 500-self.rad):
            self.velocity[1] *= -1 
            print("Wall Collision")
        # Check if Ball is out of Bounds.
        if(self.pos[0] < self.rad) or (self.pos[0] > 1000-self.rad):
            print("Out of bounds")
            self.score()

    def check_player_collison(self,player: Player):
        #Check if ball is traveling away from Player
        if player.is_left and self.velocity[0] > 0: return False
        if not player.is_left and self.velocity[0] < 0: return False
        # Check if Ball is in Range of Player
        if self.pos[0] < 990-self.rad and self.pos[0] > 10+self.rad: return False
        # Check if y value is under the Player
        if self.pos[1] > player.pos[1]+player.height: return False
        # Check if y value is above the Player
        if self.pos[1] < player.pos[1]: return False
        return True
            

    def score(self):
        self.game.update_score() 

