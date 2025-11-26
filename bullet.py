import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, ai_game):
        '''Create a bullet object'''
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        #Create a rectangle at(0,0) which represent as a bullet, then set a correct position
        self.rect = pygame.Rect(
            0, 0, self.settings.bullet_width, self.settings.bullet_height 
        )
        self.rect.midtop = ai_game.ship.rect.midtop
        #Store position represented by a float
        self.y = float(self.rect.y)

    def update(self):
        '''Moving the bullet to the top'''
        #Update the precise position of the bullet
        self.y -= self.settings.bullet_speed
        #Update the rect that represent the bullet
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)