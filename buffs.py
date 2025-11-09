import pygame
import gc
import pygame_gui

def clear_screen(screen):
    screen.fill((255, 255, 255))
    pygame.display.flip()
    gc.collect()

main_background = pygame.image.load("./images/buffs/main_page.png")
right_button = pygame.image.load('./images/buffs/right.png')
left_button = pygame.image.load('./images/buffs/left.png')
lb_rect = pygame.Rect((34,519),left_button.get_size())
rb_rect = pygame.Rect((259,519),right_button.get_size())

def render_buff(screen):
    screen.blit(main_background, (0,0))
    screen.blit(right_button, rb_rect)
    screen.blit(left_button, lb_rect)


    def button_clicked(screen,event_pos):
        if(lb_rect.collidepoint(event_pos)):
            clear_screen(screen)
            return "board"
        return None

    return button_clicked

