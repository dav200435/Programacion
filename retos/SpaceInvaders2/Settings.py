class Settings:
    def __init__(self):
        self.screen_width = 1020 
        self.screen_height = 800 
        self.bg_color = (230,230,230)
        #setting para las bullets
        self.bullet_speed = 5.0
        self.alien_bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3
        self.alien_bullets_allowed=16
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
        self.alien_points=10