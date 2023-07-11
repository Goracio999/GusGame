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
enemy_size = (30, 30)
enemy_color = COLOR_RED
enemy = pygame.Surface(enemy_size)
enemy.fill(enemy_color)
enemy_rect = pygame.Rect(WIDTH-100, 100, *enemy_size)
enemy_speed = [-1, 1]

# Starting game process
playing = True

while playing: 
    # print("Hello from pygame")
    FPS.tick(240)
    for event in pygame.event.get():
        if event.type == QUIT:
            playing = False

    main_display.fill(display_color)

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

    if enemy_rect.bottom >= HEIGHT:
        enemy_speed[1] = -enemy_speed[1]
    #     enemy_speed[0] = random.choice((1,-1))

    if enemy_rect.top <= 0:
        enemy_speed[1] = -enemy_speed[1]
    #     player_speed[0] = random.choice((1,-1))    

    if enemy_rect.right >= WIDTH:
        enemy_speed[0] = -enemy_speed[0]
    #     player_speed[1] = random.choice((1,-1))

    if enemy_rect.left <= 0:
        enemy_speed[0] = -enemy_speed[0]    
    #     player_speed[1] = random.choice((1,-1))
    enemy_rect = enemy_rect.move(enemy_speed)

    main_display.blit(player, player_rect)
    main_display.blit(enemy, enemy_rect)

    # print("left", player_rect.left,"top:",player_rect.top,"bottom:",player_rect.bottom," right:",player_rect.right)
    # player_rect = player_rect.move(player_speed)

    pygame.display.flip()