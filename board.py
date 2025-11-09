import pygame
import gc
import pygame_gui

def clear_screen(screen):
    screen.fill((255, 255, 255))
    pygame.display.flip()
    gc.collect()

def button_clicked(screen,event_pos):
    print("board clicking")
    return "buffs"

def render_board(screen):
    print("rendering board")
    return button_clicked

