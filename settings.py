class Settings:
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 800
        self.bg_color = (230,230,230)

        self.ship_speed = 2.5

        self.bullet_speed = 4.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3

        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
        self.fleet_margin_x = 100
        self.fleet_margin_y = 120

        self.alien_points = 10
        self.difficulty = "mid"
        self.set_difficulty(self.difficulty)

    def set_difficulty(self, level):
        """Adjust grid counts depending on level selection."""
        if level == "low":
            self.fleet_rows = 2
            self.fleet_columns = 4
        elif level == "mid":
            self.fleet_rows = 4
            self.fleet_columns = 6
        elif level == "high":
            self.fleet_rows = 6
            self.fleet_columns = 8
        else:
            raise ValueError(f"Unknown difficulty level: {level}")

        self.difficulty = level
        self.max_possible_score = self.fleet_rows * self.fleet_columns * self.alien_points