#This file was created by Thaddeus Sison
#Sources: goo.gl/2KMivS
#new comment

import pygame as pg
import random
from settings import *
from sprites import *

class Game:
    def __init__(self):
        #init game window
        # init pygame and create window
        pg.init()
        # init sound mixer
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("jumpy")
        self.clock = pg.time.Clock()
        self.running = True 
    def new(self):
        # add all sprites to the pg group
        self.all_sprites = pg.sprite.Group()
        # add a player 1 to the group
        self.player = Player()
        self.all_sprites.add(self.player)
        #add a platform
        self.platform = Platform()
        self.all_sprites.add(self.platform)
        # call the run method
        self.run()
    def run(self):
        # set boolean playing to true
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
    def update(self):
        self.all_sprites.update()
        
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
    def draw(self):
        self.screen.fill(GREEN)
        self.all_sprites.draw(self.screen)
        pg.display.flip()
    def show_start_screen(self):
        pass
    def show_go_screen(self):
        pass

g = Game()

g.show_go_screen()

while g.running:
    g.new()
    g.show_go_screen()