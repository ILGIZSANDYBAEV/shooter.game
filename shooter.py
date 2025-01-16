import pygame
import random

# Инициализация Pygame
pygame.init()

# Параметры экрана
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Shooter Game")

# Цвета
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Игрок
player_size = 50
player_pos = [screen_width // 2, screen_height - 2 * player_size]
player_speed = 10

# Враги
enemy_size = 50
enemy_pos = [random.randint(0, screen_width - enemy_size), 0]
enemy_speed = 10

# Пули
bullet_size = 20
bullet_speed = 20
bullets = []

# Основной игровой цикл
game_over = False
clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT] and player_pos[0] < screen_width - player_size:
        player_pos[0] += player_speed
    if keys[pygame.K_SPACE]:
        bullets.append([player_pos[0] + player_size // 2 - bullet_size // 2, player_pos[1]])

    screen.fill(black)

    # Обновление позиции врага
    enemy_pos[1] += enemy_speed
    if enemy_pos[1] > screen_height:
        enemy_pos = [random.randint(0, screen_width - enemy_size), 0]
    
    # Обновление позиции пуль
    for bullet in bullets:
        bullet[1] -= bullet_speed
        if bullet[1] < 0:
            bullets.remove(bullet)
    
    # Проверка столкновений
    for bullet in bullets:
        if (enemy_pos[1] < bullet[1] < enemy_pos[1] + enemy_size) and (enemy_pos[0] < bullet[0] < enemy_pos[0] + enemy_size):
            bullets.remove(bullet)
            enemy_pos = [random.randint(0, screen_width - enemy_size), 0]

    # Отображение игрока, врага и пуль
    pygame.draw.rect(screen, white, (player_pos[0], player_pos[1], player_size, player_size))
    pygame.draw.rect(screen, red, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))
    for bullet in bullets:
        pygame.draw.rect(screen, white, (bullet[0], bullet[1], bullet_size, bullet_size))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()