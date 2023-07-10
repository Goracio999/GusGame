import pygame
from pygame.constants import QUIT

pygame.init()

print("Hello World! Let's go!")

HEIGHT = 800
WIDTH = 1200

main_display = pygame.display.set_mode((HEIGHT, WIDTH))

player = pygame.Surface((20, 20))
player.fill((255, 255, 255))
playing = True
while playing: 
    print("Hello from pygame")
    for event in pygame.event.get():
        if event.type == QUIT:
            playing = False
    
    main_display.blit(player, (0, 0))

    pygame.display.flip()