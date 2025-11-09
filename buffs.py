import pygame
import gc
import pygame_gui
import Player
from helper import display_money

def clear_screen(screen):
    screen.fill((255, 255, 255))
    pygame.display.flip()
    gc.collect()

imgs = {
    "main_page":pygame.image.load("./images/buffs/main_page.png"),
    "right_button":pygame.image.load('./images/right_arrow.png'),
    "left_button":pygame.image.load('./images/left_arrow.png'),
    "buy_hertz":pygame.image.load('./images/buffs/buy_hertz.png'),
    "buy_hunt":pygame.image.load('./images/buffs/buy_hunt.png'),
    "buy_blanton":pygame.image.load('./images/buffs/buy_blanton.png'),
    "sold_hertz":pygame.image.load('./images/buffs/sold_hertz.png'),
    "sold_hunt":pygame.image.load('./images/buffs/sold_hunt.png'),
    "sold_blanton":pygame.image.load('./images/buffs/sold_blanton.png')
}

rect = {
    "right_button":pygame.Rect((259,519),imgs["right_button"].get_size()),
    "left_button":pygame.Rect((34,519),imgs["left_button"].get_size()),
    "buy_hertz":pygame.Rect((82,233),imgs["buy_hertz"].get_size()),
    "buy_hunt":pygame.Rect((82,336),imgs["buy_hunt"].get_size()),
    "buy_blanton":pygame.Rect((82,439),imgs["buy_blanton"].get_size()),
    "sold_hertz":pygame.Rect((66,174),imgs["sold_hertz"].get_size()),
    "sold_hunt":pygame.Rect((66,277),imgs["sold_hunt"].get_size()),
    "sold_blanton":pygame.Rect((66,380),imgs["sold_blanton"].get_size())
}

def render_buff(screen,player:Player):
    def button_clicked(screen,event_pos):
        if(rect["left_button"].collidepoint(event_pos)):
            return "board"
        elif(rect["right_button"].collidepoint(event_pos)):
            return "boosts"
        elif(rect["buy_hertz"].collidepoint(event_pos)):
            player.update_buffs("hertz",800)
        elif(rect["buy_hunt"].collidepoint(event_pos)):
            player.update_buffs("hunt",800)
        elif(rect["buy_blanton"].collidepoint(event_pos)):
            player.update_buffs("blanton",800)

        render_buff(screen,player)
        return None
    
    for img in imgs:
        if("sold" not in img or img.strip("sold_") in player.buffs):
            screen.blit(imgs[img], rect.get(img,(0,0)))

    display_money(screen,player)
    return button_clicked

