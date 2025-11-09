import pygame

pygame.init()
SCREEN_W, SCREEN_H = 400, 719
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))


screen.fill((255, 255, 255))
clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
    clock.tick(30) #fps limiter

pygame.quit()