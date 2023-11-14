import pygame
import sys
import random

# Inicializar Pygame
pygame.init()

# Dimensiones de la pantalla
WIDTH, HEIGHT = 800, 600

# Colores
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Clase para representar mini objetos
class MiniObject(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = random.randint(2, 4)

    def update(self, target):
        # Mover hacia el objetivo (ratón)
        dx = target[0] - self.rect.centerx
        dy = target[1] - self.rect.centery
        distance = (dx ** 2 + dy ** 2) ** 0.5

        if distance != 0:
            self.rect.x += int(self.speed * dx / distance)
            self.rect.y += int(self.speed * dy / distance)

# Función para duplicar mini objetos
def duplicate_mini_object(group, obj):
    new_mini_object = MiniObject(obj.rect.x + 30, obj.rect.y + 30)
    group.add(new_mini_object)

# Configuración de la pantalla
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Objects Chase Mouse")

# Reloj para controlar la velocidad del juego
clock = pygame.time.Clock()

# Grupo de sprites para mini objetos
mini_objects_group = pygame.sprite.Group()

# Crear mini objetos iniciales
for _ in range(5):
    mini_object = MiniObject(random.randint(0, WIDTH), random.randint(0, HEIGHT))
    mini_objects_group.add(mini_object)

# Bucle principal del juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Obtener la posición actual del ratón
    mouse_position = pygame.mouse.get_pos()

    # Actualizar mini objetos
    for mini_object in mini_objects_group:
        mini_object.update(mouse_position)

        # Verificar colisión con el ratón
        if mini_object.rect.collidepoint(mouse_position):
            duplicate_mini_object(mini_objects_group, mini_object)

    # Limpiar la pantalla
    screen.fill(WHITE)

    # Dibujar mini objetos en la pantalla
    mini_objects_group.draw(screen)

    # Actualizar la pantalla
    pygame.display.flip()

    # Establecer la velocidad del juego
    clock.tick(60)