import pygame, os, sys

class Ship:
    def __init__(self, ai_game):
        #initialize ship and set its initial position
        #attributes，属性
        self.screen=ai_game.screen
        self.screen_rect=ai_game.screen.get_rect()
        self.settings=ai_game.settings
        #Load ship image and get its out rectangle (?)
        try:
            # 使用 os.path.join() 构建路径，确保跨平台兼容性
            image_path = os.path.join('AlienInvasion','images',"ship.bmp")
            self.image=pygame.image.load(image_path)
            if self.image is None:
                raise FileNotFoundError(f"无法加载图像: {image_path}.  pygame.image.load() 返回 None.")
            self.rect=self.image.get_rect()
        except pygame.error as e:
            # 捕获 pygame.error，这是图像加载失败时通常抛出的错误
            print(f"警告: 无法加载图像 '{image_path}'。将使用默认占位符。详细信息：{e}")
            # 创建一个默认的占位符 Surface (例如，一个红色的矩形)
            # 可以根据需要调整尺寸，这里使用一个固定值
            default_width = 50
            default_height = 50
            self.image = pygame.Surface((default_width, default_height))
            self.image.fill((255, 0, 0)) # 填充为红色
            self.rect = self.image.get_rect()        
            self.image=None
        #every new ship is put ta the bottom of the screen
        self.rect.midbottom=self.screen_rect.midbottom

        #在飞船的属性x中存储一个浮点数

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