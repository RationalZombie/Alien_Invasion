import unittest
import pygame

from alien import Alien
from alien_invasion import AlienInvasion
from settings import Settings


class AlienMovementTests(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.screen = pygame.Surface((1200, 800))
        self.settings = Settings()
        self.settings.fleet_direction = 1
        self.ai_game = type("GameStub", (), {"screen": self.screen, "settings": self.settings})()

    def test_alien_update_keeps_fleet_direction_stable(self):
        alien = Alien(self.ai_game)
        alien.rect.x = self.screen.get_width() - alien.rect.width
        alien.x = float(alien.rect.x)

        self.assertTrue(alien.check_edges())

        alien.update()

        self.assertEqual(self.settings.fleet_direction, 1)
        self.assertEqual(alien.rect.x, self.screen.get_width() - alien.rect.width + self.settings.alien_speed)

    def test_fleet_starts_with_large_edge_margins(self):
        class FleetStub:
            def __init__(self):
                self.screen = pygame.Surface((1200, 800))
                self.settings = Settings()
                self.aliens = []

            def _create_alien(self, x_position, y_position):
                new_alien = Alien(self)
                new_alien.x = x_position
                new_alien.rect.x = x_position
                new_alien.rect.y = y_position
                self.aliens.append(new_alien)

        fleet_stub = FleetStub()
        AlienInvasion._create_fleet(fleet_stub)

        self.assertGreaterEqual(min(alien.rect.x for alien in fleet_stub.aliens), fleet_stub.settings.fleet_margin_x)
        self.assertLessEqual(max(alien.rect.right for alien in fleet_stub.aliens), self.screen.get_width() - fleet_stub.settings.fleet_margin_x)
        self.assertGreaterEqual(min(alien.rect.y for alien in fleet_stub.aliens), fleet_stub.settings.fleet_margin_y)


if __name__ == "__main__":
    unittest.main()
