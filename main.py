import pygame as pg
import random

class Game:
    def __init__(self, dimensions):
        self.dimensions = dimensions
        self.setup()
        self.player1 = Player(True,self.canvas)
        self.player2 = Player(False, self.canvas)
        self.ball = Ball(self.canvas)
        self.loop()


    def setup(self):
        pg.init()
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
            pg.display.update()
    def quit(self):
        pg.quit()


class Ball:
    def __init__(self,screen):
        self.screen = screen
        self.pos = [500,250]
        self.cross_pos = [500,250]
        self.rad = 10
        self.start_pos = [500,250]
        self.velocity = [1,0]

        self.setup()

    def setup(self):
        self.velocity=[1,random.uniform(0,1)]

    def update(self):
        self.pos[1]+=self.velocity[1]/10
        self.pos[0]+=self.velocity[0]/10
        self.check_collide()

    def draw(self):
        pg.draw.circle(self.screen,(255,255,255),self.pos,self.rad)

    def check_collide(self):
    # When Ball collides with Player, multiply the x velocity by -1
    # When Ball collides with Wall, multiply the y velocity by -1
    # When Ball collides with Sides, end the game
        if(self.pos[0] < self.rad) or (self.pos[0] > 1000-self.rad):
            self.end()
            print(0)
        if self.pos[0] < 11 or self.pos[0] > 989:
            self.velocity[0] = self.velocity[0]*(-1)
        if (self.pos[1] < 0) or (self.pos[1] > 500):
            self.velocity[1] = self.velocity[1]*(-1)
            

    def end(self):
        pg.quit()
 

        



class Player:
    def __init__(self,is_left: bool, screen):
        self.is_left=is_left
        self.screen = screen
        self.pos = [0,0]
        self.width = 10
        self.height = 100
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

if __name__ == "__main__":
    start()



