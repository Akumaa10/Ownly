import pygame
import gc
import pygame_gui

def clear_screen(screen):
    screen.fill((255, 255, 255))
    pygame.display.flip()
    gc.collect()

main_background = pygame.image.load("./images/leaderboard/main_page.png")
left_button = pygame.image.load('./images/last_left_arrow.png')
lb_rect = pygame.Rect((31,509),left_button.get_size())

def render_leaderboard(screen):
    screen.blit(main_background, (0,0))
    screen.blit(left_button, lb_rect)


    def button_clicked(screen,event_pos):
        if(lb_rect.collidepoint(event_pos)):
            return "boosts"
        return None

    return button_clicked

