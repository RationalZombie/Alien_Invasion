import pygame, os

class Ship:
    def __init__(self, ai_game):
        #initialize ship and set its initial position
        #attributes
        self.screen=ai_game.screen
        self.screen_rect=ai_game.screen.get_rect()
        self.settings=ai_game.settings
        #Load ship image and get its out rectangle (?)
        base_dir = os.path.dirname(__file__)
        image_path = os.path.join(base_dir, 'images', 'ship.bmp')
        try:
            raw_image = pygame.image.load(image_path)
            self.image = pygame.transform.scale(raw_image, (70, 70))
            self.rect = self.image.get_rect()
        except (pygame.error, FileNotFoundError) as e:
            print(f"Warning: unable to load image '{image_path}'. Using placeholder. Details: {e}")
            default_width = 44
            default_height = 44
            self.image = pygame.Surface((default_width, default_height))
            self.image.fill((255, 0, 0))
            self.rect = self.image.get_rect()
        #every new ship is put ta the bottom of the screen
        self.rect.midbottom=self.screen_rect.midbottom
        self.rect.y -= 40

        #Store a floating point as the x coordinate of the ship
        self.x=float(self.rect.x)

        #'Moving' Flag (The ship is not moving at the beginning)
        self.moving_right=False
        self.moving_left=False

    def update(self):
        '''Change ship position according to 'Moving' flag'''
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x=self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)