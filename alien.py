import pygame, os
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, ai_game):
        #Initailize
        super().__init__()
        self.screen = ai_game.screen

        #Load Alien images and set its start position.
        base_dir = os.path.dirname(__file__)
        image_path = os.path.join(base_dir, 'images', 'alien.bmp')
        try:
            self.image = pygame.image.load(image_path)
        except (pygame.error, FileNotFoundError) as e:
            print(f"Warning: unable to load image '{image_path}'. Using placeholder. Details: {e}")
            self.image = pygame.Surface((50, 50))
            self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()

        #Every Alien should be placed at the up-left corner on the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Save the precise horizontal position of the alien.
        self.x = float(self.rect.x)
        