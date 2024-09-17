from pygame.sprite import Sprite
import pygame

class AlienBullet(Sprite):
    def __init__(self, ai_game,alien):
        """Crear la bala donde está la nave"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = (60, 60, 60)
        # Crear la bala en el rect (0, 0).
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midbottom = alien.rect.midbottom  # Use midbottom instead of midtop
        # Store the bullet's position as a float.
        self.y = float(self.rect.y)
        
    
    def update(self):
        """Move the bullet up the screen."""
        # Update the exact position of the bullet.
        self.y += self.settings.alien_bullet_speed
        # Update the rect position.
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)