import pygame


class TitleScreen:
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings
        self.play_button_rect = pygame.Rect(0, 0, 0, 0)
        self.difficulty_button_rects = {}
        self.pressed_button = None

    def draw(self):
        font = pygame.font.SysFont(None, 72)
        title_surface = font.render("Alien Invasion", True, (20, 20, 20))
        title_rect = title_surface.get_rect(center=(self.settings.screen_width // 2, 180))
        self.screen.blit(title_surface, title_rect)

        self._draw_difficulty_options()

        button_font = pygame.font.SysFont(None, 48)
        play_surface = button_font.render("Play", True, (255, 255, 255))
        self.play_button_rect = play_surface.get_rect(center=(self.settings.screen_width // 2, 500))
        self._draw_button(
            self.play_button_rect,
            play_surface,
            (40, 120, 200),
            pressed=self.pressed_button == "play",
        )

        about_font = pygame.font.SysFont(None, 18)
        about_surface = about_font.render(
            "Credits: RationalZombie(Markdown&Prompt&idea); Gemini-3.5-flash(Markdown); MAI-Code-1-Flash/Raptor mini(Programming)",
            True,
            (80, 80, 80),
        )
        about_rect = about_surface.get_rect(center=(self.settings.screen_width // 2, 560))
        self.screen.blit(about_surface, about_rect)

    def _draw_difficulty_options(self):
        button_font = pygame.font.SysFont(None, 36)
        label_font = pygame.font.SysFont(None, 24)

        label_surface = label_font.render("Select Difficulty:", True, (20, 20, 20))
        label_rect = label_surface.get_rect(center=(self.settings.screen_width // 2, 260))
        self.screen.blit(label_surface, label_rect)

        options = ["low", "mid", "high"]
        option_text = {"low": "Low", "mid": "Mid", "high": "High"}
        option_colors = {"low": (120, 180, 255), "mid": (80, 160, 220), "high": (40, 120, 200)}
        base_x = self.settings.screen_width // 2
        y = 320
        spacing = 180

        self.difficulty_button_rects = {}
        for index, option in enumerate(options):
            text_surface = button_font.render(option_text[option], True, (255, 255, 255))
            button_rect = text_surface.get_rect(center=(base_x + (index - 1) * spacing, y))
            self.difficulty_button_rects[option] = button_rect
            self._draw_button(
                button_rect,
                text_surface,
                option_colors[option],
                pressed=self.pressed_button == option,
                selected=self.settings.difficulty == option,
            )

        status_surface = label_font.render(
            f"Current difficulty: {self.settings.difficulty.title()}",
            True,
            (20, 20, 20),
        )
        status_rect = status_surface.get_rect(center=(self.settings.screen_width // 2, 390))
        self.screen.blit(status_surface, status_rect)

    def _draw_button(self, rect, text_surface, button_color, pressed=False, selected=False):
        if pressed:
            outer_color = tuple(max(0, c - 45) for c in button_color)
            pygame.draw.rect(self.screen, outer_color, rect.inflate(28, 20))
            inner_rect = rect.inflate(24, 16)
            pygame.draw.rect(self.screen, button_color, inner_rect)
            self.screen.blit(text_surface, text_surface.get_rect(center=rect.center).move(0, 1))
        elif selected:
            pygame.draw.rect(self.screen, (220, 220, 220), rect.inflate(28, 20))
            pygame.draw.rect(self.screen, button_color, rect.inflate(24, 16))
            self.screen.blit(text_surface, text_surface.get_rect(center=rect.center))
        else:
            pygame.draw.rect(self.screen, button_color, rect.inflate(24, 16))
            self.screen.blit(text_surface, text_surface.get_rect(center=rect.center))

    def handle_mouse_down(self, mouse_pos):
        if self.play_button_rect.collidepoint(mouse_pos):
            self.pressed_button = "play"
            return None

        for difficulty, rect in self.difficulty_button_rects.items():
            if rect.collidepoint(mouse_pos):
                self.pressed_button = difficulty
                return None

        self.pressed_button = None
        return None

    def handle_mouse_up(self, mouse_pos):
        if not self.pressed_button:
            return None

        action = None
        if self.pressed_button == "play" and self.play_button_rect.collidepoint(mouse_pos):
            action = "play"
        elif self.pressed_button in self.difficulty_button_rects:
            button_rect = self.difficulty_button_rects[self.pressed_button]
            if button_rect.collidepoint(mouse_pos):
                action = self.pressed_button

        self.pressed_button = None
        return action
