import sys
import pygame
from pygame.sprite import Group
import random

from Settings import Settings
from Ship import Ship
from Bullet import Bullet
from Alien import Alien
from AlienBullet import AlienBullet

class AlienInvasion:
    
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """CONSTRUCTOR DEL JUEGO DONDE INICIALIZAMOS LAS VARIABLES MÁS IMPORTANTES."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height),pygame.FULLSCREEN)
        pygame.display.set_caption("Space Invaders")
        self.clock = pygame.time.Clock()
        self.bg_color = self.settings.bg_color
        self.screen.fill(self.bg_color) 
        self.ship = Ship(self)
        self.bullets = Group()
        #aliens
        self.aliens = pygame.sprite.Group()
        self._create_fleet()   
        self.alienBullets=Group()
        
        self.points = 0

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._alienShoot()
            self._check_events()
            if self.ship:
                self.ship.update()
            self.bullets.update()
            self.alienBullets.update()
            self._update_aliens()
            self._update_screen()
            
            self.clock.tick(60)
            
                
    
    def _update_screen(self):
        """Actualiza las imágenes de pantalla y pinta la nueva pantalla."""
        self.screen.fill(self.settings.bg_color)
        if self.ship:
            self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        for bullet in self.alienBullets:
            bullet.draw_bullet()
        for bullet in self.alienBullets:
            if bullet.rect.bottom >= self.settings.screen_width:
                self.alienBullets.remove(bullet)
            
        self._colissions()
        self.aliens.draw(self.screen)
        self.lives()
        self.score()
        self.checkWiner()
        pygame.display.flip()
    
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and self.ship:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT and self.ship:
                    self.ship.moving_left = True
                elif event.key == pygame.K_SPACE:
                    self._fire_bullet()
                elif event.key == pygame.K_r:
                    self._restart_game()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT and self.ship:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT and self.ship:
                    self.ship.moving_left = False
            

    def _check_keyup_events(self, event):
    # no copies nada aquí
        pass

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            
    def _create_fleet(self):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number * (2 * alien_width) + alien_width, row_number * (2 * alien_height))
        
    def _create_alien(self, x_position, y_position):

        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)
        
    def _colissions(self):
        # Check for collisions between bullets and aliens
        if pygame.sprite.groupcollide(self.bullets, self.aliens, True, True):
            self.points+=self.settings.alien_points
            self.hit()
        pygame.sprite.groupcollide(self.bullets, self.alienBullets, True, True)
        # Check for collisions between alien bullets and the player's ship
        for alien_bullet in self.alienBullets:
            if alien_bullet.rect.colliderect(self.ship.rect):
                self.alienBullets.remove(alien_bullet)
                self.ship.lifes-=1
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        
    def _alienShoot(self):
        for alien in self.aliens:
            # Generar un número aleatorio entre 0 y 1
            random_number = random.random()
            # Si el número aleatorio es menor o igual a 0.3 (30% de probabilidad), el alien dispara
            if random_number <= 0.15 and len(self.alienBullets) <= self.settings.alien_bullets_allowed:
                newBullet = AlienBullet(self, alien)
                self.alienBullets.add(newBullet)
                
    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()
    
    def checkaliensBottom(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self.settings.alien_speed=0
                
        
    def _check_fleet_edges(self):
        """Si detecta un borde los alines cambia la dirección"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Cambio de la dirección"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
        
    def checkWiner(self):
        if len(self.aliens)==0:
            self.screen.fill(self.settings.bg_color)
            self.showText(texto="YOU WIN", color=(0, 255, 0))
            self.retry()
            self.pressR()
        elif self.ship.lifes<=0:
            self.screen.fill(self.settings.bg_color)
            self.showText(texto="YOU LOSE", color=(255, 0, 0))
            self.retry()
            self.pressR()
        
    def showText(self, texto, tamano=150, color=(255,255,255)):
        font = pygame.font.Font(None, tamano)
        text_surface = font.render(texto, True, color)
        text_rect = text_surface.get_rect()
        # Centrar horizontal y verticalmente
        text_rect.center = (self.settings.screen_width // 2, self.settings.screen_height // 2)
        self.screen.blit(text_surface, text_rect)
        
    def _restart_game(self):
        # Reinitialize game variables and objects
        self.ship = Ship(self)
        self.bullets.empty()
        self.aliens.empty()
        self.alienBullets.empty()
        self._create_fleet()
        self.points = 0
        
    def retry(self):
        size=50
        font = pygame.font.Font(None, size)
        text_surface = font.render("Retry?", True, (0,255,0))
        text_rect = text_surface.get_rect()
        # Centrar horizontal y verticalmente
        text_rect.center = (self.settings.screen_width // 2, self.settings.screen_height // 2 + 100)
        self.screen.blit(text_surface, text_rect)
    
    def pressR(self):
        size=50
        # Genera un color aleatorio cada vez que se llama a la función
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        font = pygame.font.Font(None, size)
        text_surface = font.render("Press R", True, color)
        text_rect = text_surface.get_rect()
        # Centrar horizontal y verticalmente
        text_rect.center = (self.settings.screen_width // 2, self.settings.screen_height // 2 + 150)
        self.screen.blit(text_surface, text_rect)
        
    def lives(self):
        size=35
        # Genera un color aleatorio cada vez que se llama a la función
        color = (0,0,0)
        font = pygame.font.Font(None, size)
        text_surface = font.render("Vidas x"+str(self.ship.lifes), True, color)
        text_rect = text_surface.get_rect()
        # Centrar horizontal y verticalmente
        text_rect.center = (50,30)
        self.screen.blit(text_surface, text_rect)
        
    def hit(self):
        size=20
        # Genera un color aleatorio cada vez que se llama a la función
        color = (0,0,0)
        font = pygame.font.Font(None, size)
        text_surface = font.render("HIT!", True, color)
        text_rect = text_surface.get_rect()
        # Centrar horizontal y verticalmente
        text_rect.center = (self.ship.rect.x,self.ship.rect.y)
        self.screen.blit(text_surface, text_rect)
    
    def score(self):
        size=35
        # Genera un color aleatorio cada vez que se llama a la función
        color = (0,0,0)
        font = pygame.font.Font(None, size)
        text_surface = font.render(str(self.points), True, color)
        text_rect = text_surface.get_rect()
        # Centrar horizontal y verticalmente
        text_rect.center = (50,100)
        self.screen.blit(text_surface, text_rect)

if __name__ == '__main__':
# Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
