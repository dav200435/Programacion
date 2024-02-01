import pygame
import random

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Space Invaders")

# Colores
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Jugador
player_width = 50
player_height = 50
player_x = width // 2 - player_width // 2
player_y = height - 2 * player_height
player_speed = 5

# Enemigo
enemy_width = 50
enemy_height = 50
enemy_speed = 3
enemy_spawn_rate = 25

# Disparo
bullet_width = 5
bullet_height = 15
bullet_speed = 7

# Funciones
def player(x, y):
    pygame.draw.rect(screen, white, [x, y, player_width, player_height])

def enemy(x, y):
    pygame.draw.rect(screen, red, [x, y, enemy_width, enemy_height])

def bullet(x, y):
    pygame.draw.rect(screen, white, [x, y, bullet_width, bullet_height])

# Game Loop
running = True
clock = pygame.time.Clock()

bullets = []
enemies = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < width - player_width:
        player_x += player_speed

    if keys[pygame.K_SPACE]:
        bullets.append([player_x + player_width // 2 - bullet_width // 2, player_y])

    # Mover los enemigos
    for enemy_pos in enemies:
        enemy_pos[1] += enemy_speed

    # Generar nuevos enemigos
    if random.randint(1, enemy_spawn_rate) == 1:
        enemy_x = random.randint(0, width - enemy_width)
        enemy_y = 0
        enemies.append([enemy_x, enemy_y])

    # Mover los disparos
    for bullet_pos in bullets:
        bullet_pos[1] -= bullet_speed

    # Colisiones
    for bullet_pos in bullets:
        for enemy_pos in enemies:
            if (
                bullet_pos[0] < enemy_pos[0] + enemy_width
                and bullet_pos[0] + bullet_width > enemy_pos[0]
                and bullet_pos[1] < enemy_pos[1] + enemy_height
                and bullet_pos[1] + bullet_height > enemy_pos[1]
            ):
                bullets.remove(bullet_pos)
                enemies.remove(enemy_pos)

    # Limpiar la pantalla
    screen.fill(black)

    # Dibujar jugador, enemigos y disparos
    player(player_x, player_y)
    for enemy_pos in enemies:
        enemy(enemy_pos[0], enemy_pos[1])
    for bullet_pos in bullets:
        bullet(bullet_pos[0], bullet_pos[1])

    # Actualizar pantalla
    pygame.display.flip()

    # Controlar la velocidad del juego
    clock.tick(60)

# Salir del juego
pygame.quit()