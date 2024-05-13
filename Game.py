import pygame as pg
import Ball
import Player
class Game:
    def __init__(self, dimensions):
        self.dimensions = dimensions
        self.setup()
        self.player1 = Player.Player(True,self.canvas, self)
        self.player2 = Player.Player(False, self.canvas, self)
        self.ball = Ball.Ball(self.canvas, self)
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


        

