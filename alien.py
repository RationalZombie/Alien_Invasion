import pygame, os
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, ai_game):
        #Initailize
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #Load Alien images and set its start position.
        base_dir = os.path.dirname(__file__)
        image_path = os.path.join(base_dir, 'images', 'alien.bmp')
        try:
            raw_image = pygame.image.load(image_path)
            self.image = pygame.transform.scale(raw_image, (40, 40))
        except (pygame.error, FileNotFoundError) as e:
            print(f"Warning: unable to load image '{image_path}'. Using placeholder. Details: {e}")
            self.image = pygame.Surface((40, 40))
            self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()

        #Every Alien should be placed at the up-left corner on the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Save the precise horizontal position of the alien.
        self.x = float(self.rect.x)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        return self.rect.right >= screen_rect.right or self.rect.left <= 0

    def update(self):
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x
        