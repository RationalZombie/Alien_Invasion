import pygame


class YouWonScreen:
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings
        self.retry_button_rect = pygame.Rect(0, 0, 0, 0)
        self.title_button_rect = pygame.Rect(0, 0, 0, 0)

    def draw(self):
        self._draw_end_screen(
            "You Won!",
            "You cleared the alien fleet.",
            (20, 140, 20),
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
        retry_surface = button_font.render("Restart", True, (255, 255, 255))
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

    def handle_mouse_down(self, mouse_pos):
        if self.retry_button_rect.collidepoint(mouse_pos):
            self.pressed_button = "retry"
        elif self.title_button_rect.collidepoint(mouse_pos):
            self.pressed_button = "title"
        else:
            self.pressed_button = None

    def handle_mouse_up(self, mouse_pos):
        if not getattr(self, "pressed_button", None):
            return None

        action = None
        if self.pressed_button == "retry" and self.retry_button_rect.collidepoint(mouse_pos):
            action = "retry"
        elif self.pressed_button == "title" and self.title_button_rect.collidepoint(mouse_pos):
            action = "title"

        self.pressed_button = None
        return action
