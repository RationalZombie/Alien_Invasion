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
        self.fleet_rows = 4
        self.fleet_columns = 6

        self.alien_points = 10
        self.max_possible_score = self.fleet_rows * self.fleet_columns * self.alien_points