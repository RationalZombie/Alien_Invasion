import pygame


class TitleScreen:
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings
        self.play_button_rect = pygame.Rect(0, 0, 0, 0)

    def draw(self):
        font = pygame.font.SysFont(None, 72)
        title_surface = font.render("Alien Invasion", True, (20, 20, 20))
        title_rect = title_surface.get_rect(center=(self.settings.screen_width // 2, 180))
        self.screen.blit(title_surface, title_rect)

        button_font = pygame.font.SysFont(None, 48)
        play_surface = button_font.render("Play", True, (255, 255, 255))
        self.play_button_rect = play_surface.get_rect(center=(self.settings.screen_width // 2, 360))
        pygame.draw.rect(self.screen, (40, 120, 200), self.play_button_rect.inflate(24, 16))
        self.screen.blit(play_surface, self.play_button_rect)

        about_font = pygame.font.SysFont(None, 28)
        about_surface = about_font.render("About: Defend Earth from the alien fleet.", True, (80, 80, 80))
        about_rect = about_surface.get_rect(center=(self.settings.screen_width // 2, 520))
        self.screen.blit(about_surface, about_rect)

    def handle_click(self, mouse_pos):
        return self.play_button_rect.collidepoint(mouse_pos)
