import pygame
import gc
import pygame_gui

def clear_screen(screen):
    screen.fill((255, 255, 255))
    pygame.display.flip()
    gc.collect()

main_background = pygame.image.load("./images/profile/main_page.png")
right_button = pygame.image.load('./images/last_right_arrow.png')
rb_rect = pygame.Rect((235,509),right_button.get_size())

def render_profile(screen):
    screen.blit(main_background, (0,0))
    screen.blit(right_button, rb_rect)


    def button_clicked(screen,event_pos):
        if(rb_rect.collidepoint(event_pos)):
            return "board"
        return None

    return button_clicked

