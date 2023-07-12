import random
import pygame
from pygame.constants import QUIT, K_DOWN, K_UP, K_LEFT, K_RIGHT

pygame.init()

print("Hello World! Let's go!")

HEIGHT = 800
WIDTH = 600
# setting color constants
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_RED = (255, 0, 0)
COLOR_BLUE = (0, 0, 255)
COLOR_GREEN = (0, 255, 0)
COLOR_YELLOW = (255, 255, 0)

FPS = pygame.time.Clock()

main_display = pygame.display.set_mode((WIDTH, HEIGHT))
display_color = COLOR_BLUE

# Initialize player
player_size = (20, 20)
player = pygame.Surface(player_size)
player_color = COLOR_YELLOW
player.fill(player_color)
player_rect = player.get_rect()
player_move_down = [0, 1]
player_move_up = [0, -1]
player_move_left = [-1, 0]
player_move_right = [1, 0]

# Initialize enemy
def create_enimy():
    enemy_size = (30, 30)
    enemy_color = COLOR_RED
    enemy = pygame.Surface(enemy_size)
    enemy.fill(enemy_color)
    enemy_rect = pygame.Rect(WIDTH, random.randint(0, HEIGHT), *enemy_size)
    enemy_speed = [random.randint(-5, -1), 0]
    return [enemy, enemy_rect, enemy_speed]

CREATE_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(CREATE_ENEMY, 1500)
enemies = []

# Initialize bonus
def create_bonus():
    bonus_size = (20, 20)
    bonus_color = COLOR_GREEN
    bonus = pygame.Surface(bonus_size)
    bonus.fill(bonus_color)
    bonus_rect = pygame.Rect(random.randint(0, WIDTH), 0, *bonus_size)
    bonus_move = [0, 1]
    return [bonus, bonus_rect, bonus_move]

CREATE_BONUS = pygame.USEREVENT + 2
pygame.time.set_timer(CREATE_BONUS, 2500)
bonuses = []

# Starting game process
playing = True

while playing: 
    # print("Hello from pygame")
    FPS.tick(120)
    for event in pygame.event.get():
        if event.type == QUIT:
            playing = False
        if event.type == CREATE_ENEMY:
            enemies.append(create_enimy())
        if event.type == CREATE_BONUS:
            bonuses.append(create_bonus())


    main_display.fill(display_color)

# Arrow keys processing - drive the player
    keys = pygame.key.get_pressed()

    if keys[K_DOWN]:
        print("Down pressed") 
        if player_rect.bottom <= HEIGHT:
            player_rect = player_rect.move(player_move_down)
        else:
            print("Bottom reached")
        print("left", player_rect.left,"top:",player_rect.top,"bottom:",player_rect.bottom," right:",player_rect.right)    

    if keys[K_UP]:
        print("Up pressed") 
        if player_rect.top > 0:
            player_rect = player_rect.move(player_move_up)
        else:
            print("Top reached")
        print("left", player_rect.left,"top:",player_rect.top,"bottom:",player_rect.bottom," right:",player_rect.right)    


    if keys[K_LEFT]:
        print("Left pressed") 
        if player_rect.left > 0:
            player_rect = player_rect.move(player_move_left)
        else:
            print("Left border reached")
        print("left", player_rect.left,"top:",player_rect.top,"bottom:",player_rect.bottom," right:",player_rect.right)

    if keys[K_RIGHT]:
        print("Right pressed") 
        if player_rect.right < WIDTH:
            player_rect = player_rect.move(player_move_right)    
        else:
            print("Right border reached")
        print("left", player_rect.left,"top:",player_rect.top,"bottom:",player_rect.bottom," right:",player_rect.right)

    main_display.blit(player, player_rect)

# processing enemies
    for enemy in enemies:
        enemy[1] = enemy[1].move(enemy[2])
        main_display.blit(enemy[0], enemy[1])
        # deleting out of scene objects
        if enemy[1].right < 0:
            enemies.pop(enemies.index(enemy))

# processing bonuses
    for bonus in bonuses:
        bonus[1] = bonus[1].move(bonus[2])
        main_display.blit(bonus[0], bonus[1])
        # deleting out of scene objects
        if bonus[1].top > HEIGHT:
            bonuses.pop(bonuses.index(bonus))

    print("Enimies: ", len(enemies), "Bonuses: ", len(bonuses))

    pygame.display.flip()