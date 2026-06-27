import unittest
import pygame

from alien_invasion import AlienInvasion
from settings import Settings


class Phase5InterfaceTests(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.screen = pygame.Surface((800, 800))
        self.settings = Settings()
        self.game = AlienInvasion.__new__(AlienInvasion)
        self.game.screen = self.screen
        self.game.settings = self.settings
        self.game.playing = False

    def test_play_button_click_starts_game(self):
        self.game.playing = False
        self.game._start_game()
        self.assertTrue(self.game.playing)


if __name__ == "__main__":
    unittest.main()
