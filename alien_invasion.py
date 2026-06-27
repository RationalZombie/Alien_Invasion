import pygame,sys
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    def __init__(self):
        '''Initialize game and create game resources'''
        pygame.init()
        self.clock=pygame.time.Clock()
        self.settings=Settings()
        self.screen=pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        '''Fullscreen
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.screen.screen_width = self.screen.gey_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        '''
        pygame.display.set_caption("Alien Invasion")

        self.ship=Ship(self)#Create a ship
        self._create_fleet()

    def _create_fleet(self):
        #Create one alien
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        margin_x = self.settings.fleet_margin_x
        margin_y = self.settings.fleet_margin_y
        current_x = margin_x
        current_y = margin_y
        max_x = self.settings.screen_width - margin_x - alien_width

        for row in range(self.settings.fleet_rows):
            for column in range(self.settings.fleet_columns):
                if current_x < max_x:
                    self._create_alien(current_x, current_y)
                    current_x += 2 * alien_width
            current_x = margin_x
            current_y += 2 * alien_height

    def _create_alien(self, x_position, y_position):
        #Create Alien and store in current row.
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)     


    def _check_events(self):
    #Detect keyboard and mouse events
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type==pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right=True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left=True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right=False
            elif event.key == pygame.K_LEFT:
                self.ship.moving_left=False

    def _update_screen(self):
        #Redraw everytime passing through tha loop
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)
        #make the most recent-drawn screen visible
        pygame.display.flip()

    def _update_bullets(self):
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        #print(f"Sprite number: {len(self.bullets)}")
        self.bullets.update()

    def _update_aliens(self):
        if any(alien.check_edges() for alien in self.aliens.sprites()):
            self.settings.fleet_direction *= -1
            for alien in self.aliens.sprites():
                alien.rect.y += self.settings.fleet_drop_speed
        

    def run_game(self):
        '''Main game-start loop'''
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self.aliens.update()
            self._update_aliens()
            self._update_screen()
            self.clock.tick(60)#Framerate=60


if __name__ =='__main__':
    ai=AlienInvasion()
    ai.run_game()