from pygame.sprite import Sprite
import pygame

class Bullet(Sprite):
    def __init__(self, screen):

        super(Bullet, self).__init__()
        self.screen = screen
        # Creamos el bullet con un recuadro en la posición 0,0 pero después corregimos la posición de la mismaposition.
        self.rect = pygame.Rect(0, 0, 10, 10)
        self.color = (0,0,0)
        self.speed_factor = 2
    
    def update(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet.
        self.y -= self.speed_factor
        # Update the rect position.
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)