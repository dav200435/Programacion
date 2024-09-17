import pygame
class Ship(pygame.sprite.Sprite):
    """Clase que gestiona la nave."""
    
    def __init__(self, ai_game):
    
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.moving_right = False
        self.moving_left = False
        self.lifes = 3
    
    # Cargamos la imagen de la imagen y la asociamos a un rectángulo para que sea más fácil gestionar
        self.route="C:/Users/DAV_2004_35/Programacion/retos/SpaceInvaders2/"
        self.image = pygame.image.load(self.route+'img/ship.bmp')
        self.rect = self.image.get_rect()
        
    # Posicionamos la nave en la mitad de fondo de la pantalla
        self.rect.midbottom = self.screen_rect.midbottom
    
    def blitme(self):
        """Dibuja la nave en la posición actual."""
        self.screen.blit(self.image, self.rect)
        
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += 5
        elif self.moving_left and self.rect.left > 0:
            self.rect.x -= 5
