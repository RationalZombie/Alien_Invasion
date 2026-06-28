import pygame,sys
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from title_screen import TitleScreen
from game_over_screen import GameOverScreen
from you_won_screen import YouWonScreen

class AlienInvasion:
    def __init__(self):
        '''Initialize game and create game resources'''
        pygame.init()
        self.clock=pygame.time.Clock()
        self.settings=Settings()
        self.screen=pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.explosions = []
        self.score = 0
        self.playing = False
        self.game_state = "TITLE"
        self.title_screen = TitleScreen(self.screen, self.settings)
        self.game_over_screen = GameOverScreen(self.screen, self.settings)
        self.you_won_screen = YouWonScreen(self.screen, self.settings)
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._check_mouse_events(event)
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
        elif event.key == pygame.K_RETURN and not self.playing:
            self._start_game()

    def _check_mouse_events(self, event):
        if not self.playing and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            if self.game_state == "TITLE":
                if self.title_screen.handle_click(mouse_pos):
                    self._start_game()
            elif self.game_state == "GAME_OVER":
                action = self.game_over_screen.handle_click(mouse_pos)
                if action == "retry":
                    self._start_game()
                elif action == "title":
                    self._go_to_title()
            elif self.game_state == "YOU_WON":
                action = self.you_won_screen.handle_click(mouse_pos)
                if action == "retry":
                    self._start_game()
                elif action == "title":
                    self._go_to_title()

    def _check_keyup_events(self, event):
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right=False
            elif event.key == pygame.K_LEFT:
                self.ship.moving_left=False

    def _update_screen(self):
        #Redraw everytime passing through tha loop
        self.screen.fill(self.settings.bg_color)
        if not self.playing:
            if self.game_state == "TITLE":
                self._draw_title_screen()
            elif self.game_state == "GAME_OVER":
                self.game_over_screen.draw()
            elif self.game_state == "YOU_WON":
                self.you_won_screen.draw()
        else:
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()
            self.ship.blitme()
            self.aliens.draw(self.screen)
            self._draw_score()
        #make the most recent-drawn screen visible
        pygame.display.flip()

    def _draw_title_screen(self):
        self.title_screen.draw()

    def _start_game(self):
        self.playing = True
        self.game_state = None
        self.score = 0
        self.bullets.empty()
        self.aliens.empty()
        self.settings.fleet_direction = 1
        self._create_fleet()
        self.ship.rect.midbottom = self.screen.get_rect().midbottom
        self.ship.rect.y -= 40
        self.ship.x = float(self.ship.rect.x)

    def _go_to_title(self):
        self.playing = False
        self.game_state = "TITLE"
        self.score = 0
        self.bullets.empty()
        self.aliens.empty()
        self.settings.fleet_direction = 1
        self._create_fleet()
        self.ship.rect.midbottom = self.screen.get_rect().midbottom
        self.ship.rect.y -= 40
        self.ship.x = float(self.ship.rect.x)

    def _draw_score(self):
        font = pygame.font.SysFont(None, 36)
        score_str = f"Score: {self.score} / {self.settings.max_possible_score}"
        score_surface = font.render(score_str, True, (20, 20, 20))
        self.screen.blit(score_surface, (10, 10))

    def _update_score(self, points):
        self.score += points

    def _update_bullets(self):
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        #print(f"Sprite number: {len(self.bullets)}")
        self.bullets.update()

    def _check_bullet_alien_collisions(self):
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        for bullet, aliens_hit in collisions.items():
            for alien in aliens_hit:
                self.explosions.append((alien.rect.center, 10))
                self._update_score(self.settings.alien_points)

    def _update_aliens(self):
        if any(alien.check_edges() for alien in self.aliens.sprites()):
            self.settings.fleet_direction *= -1
            for alien in self.aliens.sprites():
                alien.rect.y += self.settings.fleet_drop_speed

        self.aliens.update()

        if pygame.sprite.spritecollideany(self.ship, self.aliens) or any(alien.rect.bottom >= self.settings.screen_height for alien in self.aliens.sprites()):
            self.playing = False
            self.game_state = "GAME_OVER"

        if not self.aliens:
            self.playing = False
            self.game_state = "YOU_WON"

    def run_game(self):
        '''Main game-start loop'''
        while True:
            self._check_events()
            if self.playing:
                self.ship.update()
                self._update_bullets()
                self.aliens.update()
                self._check_bullet_alien_collisions()
                self._update_aliens()
            self._update_screen()
            self.clock.tick(60)#Framerate=60


if __name__ =='__main__':
    ai=AlienInvasion()
    ai.run_game()