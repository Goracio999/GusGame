import random
import pygame
from pygame.constants import QUIT, K_DOWN, K_UP, K_LEFT, K_RIGHT

pygame.init()

print("Hello World! Let's go!")

HEIGHT = 800
WIDTH = 600

COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)

FPS = pygame.time.Clock()

main_display = pygame.display.set_mode((WIDTH, HEIGHT))

player_size = (20, 20)

player = pygame.Surface(player_size)
player.fill(COLOR_WHITE)
player_rect = player.get_rect()
#player_speed = [1, 1]
player_move_down = [0, 1]
player_move_up = [0, -1]
player_move_left = [-1, 0]
player_move_right = [1, 0]

playing = True

while playing: 
    # print("Hello from pygame")
    FPS.tick(240)
    for event in pygame.event.get():
        if event.type == QUIT:
            playing = False

    main_display.fill(COLOR_BLACK)

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

    # if player_rect.bottom >= HEIGHT:
    #     player_speed[1] = -player_speed[1]
    #     player_speed[0] = random.choice((1,-1))

    # if player_rect.top < 0:
    #     player_speed[1] = -player_speed[1]
    #     player_speed[0] = random.choice((1,-1))    

    # if player_rect.right >= WIDTH:
    #     player_speed[0] = -player_speed[0]
    #     player_speed[1] = random.choice((1,-1))

    # if player_rect.left < 0:
    #     player_speed[0] = -player_speed[0]    
    #     player_speed[1] = random.choice((1,-1))

    main_display.blit(player, player_rect)
    # print("left", player_rect.left,"top:",player_rect.top,"bottom:",player_rect.bottom," right:",player_rect.right)
    # player_rect = player_rect.move(player_speed)

    pygame.display.flip()