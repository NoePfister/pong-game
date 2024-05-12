import pygame as pg

class Game:
    def __init__(self, dimensions):
        self.dimensions = dimensions
        self.setup()
        self.player1 = Player(True,self.canvas)
        self.player2 = Player(False, self.canvas)
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
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_UP:
                        self.player2.move(1)
                    if event.key == pg.K_DOWN:
                        self.player2.move(-1)
                    if event.key == pg.K_W:
                        self.player1.move(1)
                    if event.key == pg.K_S:
                        self.player1.move(-1)
                    
                    

            self.player1.draw()
            self.player2.draw()
            pg.display.update()
    def quit(self):
        pg.quit()



class Player:
    def __init__(self,is_left: bool, screen):
        self.is_left=is_left
        self.screen = screen
        self.pos = (0,0)
        self.width = 10
        self.height = 100
        self.setup()

    def setup(self):
        if self.is_left:
            self.pos = (0,(500-self.height)/2)
        else:
            self.pos = (1000-self.width,(500-self.height)/2)

    def draw(self):
        pg.draw.rect(self.screen, (255,255,255), (self.pos[0],self.pos[1],self.width,self.height))


    def move(self,y:int):
        self.pos[1] += y

def start():
    dimensions = (1000,500)
    game = Game(dimensions)

if __name__ == "__main__":
    start()



