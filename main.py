import pygame as pg
import random

class Game:
    def __init__(self, dimensions):
        self.dimensions = dimensions
        self.setup()
        self.player1 = Player(True,self.canvas, self)
        self.player2 = Player(False, self.canvas, self)
        self.ball = Ball(self.canvas, self)
        self.score = [0,0]
        self.loop()


    def setup(self):
        pg.init()
        self.font = pg.font.Font("freesansbold.ttf", 32)
        self.canvas = pg.display.set_mode(self.dimensions)
        pg.display.set_caption("Pong")

    def loop(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.quit() 
                # if event.type == pg.KEYDOWN:
                #     if event.key == pg.K_UP:
                #         self.player2.move(1)
                #     if event.key == pg.K_DOWN:
                #         self.player2.move(-1)
                #     if event.key == pg.K_w:
                #         self.player1.move(1)
                #     if event.key == pg.K_s:
                #         self.player1.move(-1)
                    
            keys = pg.key.get_pressed()
            if keys[pg.K_DOWN]: self.player2.move(1)
            if keys[pg.K_UP]: self.player2.move(-1)
            if keys[pg.K_s]: self.player1.move(1)
            if keys[pg.K_w]: self.player1.move(-1)


            self.ball.update()

            self.canvas.fill((0,0,0))
            pg.draw.rect(self.canvas,(100,100,100),(500,0,10,500))
            self.player1.draw()
            self.player2.draw()
            self.ball.draw()
            self.draw_score()
            pg.display.update()

    def update_score(self):
        print("Score")
        if self.ball.pos[0] > 500:
            self.score[0] += 1
        else:
            self.score[1] += 1
        self.ball.pos = [500,250]


    def draw_score(self):
        text = self.font.render(f'{self.score[0]}:{self.score[1]}',True,(225,225,225))
        textRect = text.get_rect()
        textRect.center = (500,10)

        self.canvas.blit(text,textRect)

    

    def quit(self):
        exit(0)


        



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
def start():
    dimensions = (1000,500)
    game = Game(dimensions)


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

if __name__ == "__main__":
    start()



