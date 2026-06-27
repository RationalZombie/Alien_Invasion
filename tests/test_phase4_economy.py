import unittest
import pygame

from alien_invasion import AlienInvasion
from settings import Settings


class Phase4EconomyTests(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.screen = pygame.Surface((800, 800))
        self.settings = Settings()
        self.game = AlienInvasion.__new__(AlienInvasion)
        self.game.screen = self.screen
        self.game.settings = self.settings
        self.game.bullets = pygame.sprite.Group()
        self.game.aliens = pygame.sprite.Group()
        self.game.explosions = []
        self.game.score = 0

    def test_score_increases_when_alien_is_destroyed(self):
        self.game._update_score(10)
        self.assertEqual(self.game.score, 10)


if __name__ == "__main__":
    unittest.main()
