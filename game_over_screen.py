import pygame


class GameOverScreen:
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings
        self.retry_button_rect = pygame.Rect(0, 0, 0, 0)
        self.title_button_rect = pygame.Rect(0, 0, 0, 0)

    def draw(self):
        self._draw_end_screen(
            "Game Over",
            "An alien hit your ship or reached the bottom.",
            (180, 20, 20),
        )

    def _draw_end_screen(self, title, message, title_color):
        header_font = pygame.font.SysFont(None, 72)
        header_surface = header_font.render(title, True, title_color)
        header_rect = header_surface.get_rect(
            center=(self.settings.screen_width // 2, 160)
        )
        self.screen.blit(header_surface, header_rect)

        body_font = pygame.font.SysFont(None, 32)
        body_surface = body_font.render(message, True, (20, 20, 20))
        body_rect = body_surface.get_rect(
            center=(self.settings.screen_width // 2, 240)
        )
        self.screen.blit(body_surface, body_rect)

        button_font = pygame.font.SysFont(None, 40)
        retry_surface = button_font.render("Retry", True, (255, 255, 255))
        self.retry_button_rect = retry_surface.get_rect(
            center=(self.settings.screen_width // 2 - 120, 360)
        )
        pygame.draw.rect(
            self.screen,
            (40, 120, 200),
            self.retry_button_rect.inflate(24, 16),
        )
        self.screen.blit(retry_surface, self.retry_button_rect)

        title_surface = button_font.render("Title Screen", True, (255, 255, 255))
        self.title_button_rect = title_surface.get_rect(
            center=(self.settings.screen_width // 2 + 140, 360)
        )
        pygame.draw.rect(
            self.screen,
            (80, 80, 80),
            self.title_button_rect.inflate(24, 16),
        )
        self.screen.blit(title_surface, self.title_button_rect)

    def handle_click(self, mouse_pos):
        if self.retry_button_rect.collidepoint(mouse_pos):
            return "retry"
        if self.title_button_rect.collidepoint(mouse_pos):
            return "title"
        return None
