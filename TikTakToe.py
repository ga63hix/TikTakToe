# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 00:03:29 2020

@author: julia
"""

import pygame as pg
import pygame.freetype
# Initialize Process
pg.init()

# Get a screen
screen = pg.display.set_mode((550, 550))
pg.display.set_caption("Tik Tak Toe")
pg.font.init() 
GAME_FONT = pg.font.SysFont('Courier New', 30)
class Game:
    def __init__(self, screen):
        self.done = False
        self.clock = pg.time.Clock()
        self.screen = screen
        self.user = 0
        self.initialize_fields()
        
    def initialize_fields(self):
        pixels = [25, 200, 375]
        self.fields = []
        self.tossed = []
        for j in pixels:
            for i in pixels:
                self.fields.append(self.create_rect(i,j,150,150,255,255,255))
                self.tossed.append(0)
                
    def test_if_victory(self):
        player = 0
        for i in range(3):
            if self.tossed[i] == self.tossed[i+3] == self.tossed[i+6] != 0: # Test for column vicotry
                player = self.tossed[i]
            elif self.tossed[3*i] == self.tossed[(3*i)+1] == self.tossed[(3*i)+2] != 0:
                player = self.tossed[i]
        if self.tossed[2] == self.tossed[4] == self.tossed[6] or self.tossed[0] == self.tossed[4] == self.tossed[8]: # Test for diagonal victory
            player = self.tossed[4]
            
        # Test if there was a victory
        if player != 0:
            if player == 1:
                winner = "Player 1"
                color = (255, 0, 0)
            elif player == 2:
                winner = "Player 2"
                color = (0, 0, 255)
    
            text_surface = GAME_FONT.render(winner + " won this game!", True, color, (0,0,0))
            screen.blit(text_surface, (40, 250))
        
            
                
    def reset(self):
        screen.fill(pygame.Color("black"))
        self.initialize_fields()
        self.user = 0

    def mouse_click(self, position):
        for i, (field, tossed) in enumerate(zip(self.fields, self.tossed)):
            if field.collidepoint(position):
                if self.user == 0 and tossed == 0:
                    pg.draw.rect(screen, (255, 0, 0), (field.left+25, field.top+25, 100, 100))
                    self.user = 1
                    self.tossed[i] = 1
                elif self.user == 1 and tossed == 0:
                    pg.draw.circle(screen, (0,0,255), (field.left+75, field.top+75), 50)
                    self.user = 0
                    self.tossed[i] = 2
        self.test_if_victory()
                    
    def create_rect(self, x, y, dim1, dim2, r, g, b):
        field = pg.draw.rect(screen, (r,g,b), (x,y,dim1,dim2))
        return field
        
    def quit_game(self):
        """Callback method to quit the game."""
        self.done = True
    
    def run(self): 
        while not self.done:
            self.dt = self.clock.tick(30)/1000
            self.handle_events()
            pg.display.flip()
            
    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True

            if event.type == pg.MOUSEBUTTONUP:
                self.mouse_click(pg.mouse.get_pos())
            
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.reset()

# Game Run
if __name__ == '__main__':
    pg.init()
    Game(screen).run()
    pg.quit()