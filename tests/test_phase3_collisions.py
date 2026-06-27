import unittest
import pygame

from alien import Alien
from alien_invasion import AlienInvasion
from bullet import Bullet
from settings import Settings


class Phase3CollisionTests(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.screen = pygame.Surface((1200, 800))
        self.settings = Settings()
        self.ai_game = type("GameStub", (), {"screen": self.screen, "settings": self.settings, "ship": type("ShipStub", (), {"rect": pygame.Rect(0, 0, 10, 10)})()})()

    def test_bullet_hits_alien_and_removes_both(self):
        game = AlienInvasion.__new__(AlienInvasion)
        game.screen = self.screen
        game.settings = self.settings
        game.bullets = pygame.sprite.Group()
        game.aliens = pygame.sprite.Group()
        game.explosions = []

        alien = Alien(self.ai_game)
        bullet = Bullet(self.ai_game)
        alien.rect.x = bullet.rect.x = 0
        alien.rect.y = bullet.rect.y = 0

        game.aliens.add(alien)
        game.bullets.add(bullet)

        game._check_bullet_alien_collisions()

        self.assertEqual(len(game.aliens), 0)
        self.assertEqual(len(game.bullets), 0)
        self.assertEqual(len(game.explosions), 1)


if __name__ == "__main__":
    unittest.main()
