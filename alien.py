import pygame, os
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, ai_game):
        #Initailize
        super().__init__()
        self.screen = ai_game.screen

        #Load Ailen images and set its start position.
        self.image = pygame.image.load(os.path.join('AlienInvasion','images',"alien.bmp"))
        self.rect = self.image.get_rect()

        #Every Alien should be placed at the up-left corner on the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Save the precise horizontal position of the alien.
        self.x = float(self.rect.x)
        