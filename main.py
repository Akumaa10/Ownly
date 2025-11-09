import pygame
import pygame_gui

from Player import Player

from buffs import render_buff
from board import render_board
from boosts import render_boosts
from leaderboard import render_leaderboard
from profile import render_profile

pygame.init()
SCREEN_W, SCREEN_H = 324, 582
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
manager = pygame_gui.UIManager((SCREEN_W, SCREEN_H))

screen.fill((255, 255, 255))
clock = pygame.time.Clock()

running = True


player = Player()
button_render = render_board(screen,player) #default render

def nav_bar_manager(page):
    global button_render
    if(page == "board"):
        print("rendering the board")
        button_render = render_board(screen,player)
    elif(page == "buffs"):
        button_render = render_buff(screen,player)
    elif(page == "boosts"):
        button_render = render_boosts(screen,player)
    elif(page == "leaderboard"):
        button_render = render_leaderboard(screen,player)
    elif(page == "profile"):
        button_render = render_profile(screen,player)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            render_result = button_render(screen,event.pos)
            if(render_result):
                nav_bar_manager(render_result)

        manager.process_events

    #Renders screen aswell as ui elements
    time_delta = clock.tick(30) / 1000.0
    manager.update(time_delta)
    manager.draw_ui(screen)
    pygame.display.flip()


pygame.quit()