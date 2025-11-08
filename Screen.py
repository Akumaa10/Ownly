import pygame
import pygame_gui


pygame.init()


SCREEN_W, SCREEN_H = 700, 1000



screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
navbar = pygame.image.load("images/Rectangle_1.png").convert_alpha()
screen.fill((255, 255, 255))
navbar = pygame.transform.scale(navbar, (SCREEN_W, 150))



running = True

while running:
    screen.blit(navbar, (0, 857))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            coord = event.pos
        

    pygame.display.flip()
    

pygame.quit()