import pygame
import gc
import pygame_gui

import Player
from helper import display_money,display_text

def clear_screen(screen):
    screen.fill((255, 255, 255))
    pygame.display.flip()
    gc.collect()

imgs = {
    "main_page":pygame.image.load("./images/boosts/main_page.png"),
    "right_button":pygame.image.load('./images/right_arrow.png'),
    "left_button":pygame.image.load('./images/left_arrow.png'),
    "buy_roll":pygame.image.load('./images/boosts/buy_roll.png'),
    "buy_go":pygame.image.load('./images/boosts/buy_go.png'),
    "1_bar_1":pygame.image.load('./images/boosts/1_bar_1.png'),
    "2_bar_2":pygame.image.load('./images/boosts/2_bar_2.png'),
    "3_bar_3":pygame.image.load('./images/boosts/3_bar_3.png'),
    "4_bar_4":pygame.image.load('./images/boosts/4_bar_4.png'),
    "5_bar_5":pygame.image.load('./images/boosts/5_bar_5.png'),
    "1_bar":pygame.image.load('./images/boosts/1_bar.png'),
    "2_bar":pygame.image.load('./images/boosts/2_bar.png'),
    "3_bar":pygame.image.load('./images/boosts/3_bar.png'),
    "4_bar":pygame.image.load('./images/boosts/4_bar.png'),
    "5_bar":pygame.image.load('./images/boosts/5_bar.png')
}

rect = {
    "right_button":pygame.Rect((259,519),imgs["right_button"].get_size()),
    "left_button":pygame.Rect((34,519),imgs["left_button"].get_size()),
    "buy_roll":pygame.Rect((101,252),imgs["buy_roll"].get_size()),
    "buy_go":pygame.Rect((101,392),imgs["buy_go"].get_size()),
    "1_bar_1":pygame.Rect((101,375),imgs["1_bar_1"].get_size()),
    "2_bar_2":pygame.Rect((101,375),imgs["2_bar_2"].get_size()),
    "3_bar_3":pygame.Rect((101,375),imgs["3_bar_3"].get_size()),
    "4_bar_4":pygame.Rect((101,375),imgs["4_bar_4"].get_size()),
    "5_bar_5":pygame.Rect((101,375),imgs["5_bar_5"].get_size()),
    "1_bar":pygame.Rect((101,235),imgs["1_bar"].get_size()),
    "2_bar":pygame.Rect((101,235),imgs["2_bar"].get_size()),
    "3_bar":pygame.Rect((101,235),imgs["3_bar"].get_size()),
    "4_bar":pygame.Rect((101,235),imgs["4_bar"].get_size()),
    "5_bar":pygame.Rect((101,235),imgs["5_bar"].get_size())
}

boost_price = {1:300,2:600,3:1200,4:2400,5:"Sold Out"}

def render_boosts(screen,player):
    def button_clicked(screen,event_pos):
        if(rect["left_button"].collidepoint(event_pos)):
            return "buffs"
        elif(rect["right_button"].collidepoint(event_pos)):
            return "leaderboard"
        elif(rect['buy_roll'].collidepoint(event_pos)):
            player.update_boosts("roll",boost_price[player.boosts["roll"]])
        elif(rect['buy_go'].collidepoint(event_pos)):
            player.update_boosts("go",boost_price[player.boosts["go"]])
        
        render_boosts(screen,player)
        return None
    
    for img in imgs:
        if(img[0].isalpha() or 
           (img[0].isdigit() and img[-1].isdigit() and int(img[0]) == player.boosts["go"]) or
           (img[0].isdigit() and not img[-1].isdigit() and int(img[0]) == player.boosts["roll"])): #means it is roll
            screen.blit(imgs[img], rect.get(img,(0,0)))


    roll_text = "$"+str(boost_price[player.boosts["roll"]]) if player.boosts["roll"] != 5 else str(boost_price[player.boosts["roll"]])
    go_text = "$"+str(boost_price[player.boosts["go"]]) if player.boosts["go"] != 5 else str(boost_price[player.boosts["go"]])

    display_text(screen,roll_text,25,(255,255,255),"pixelifysansregular",(173,265))
    display_text(screen,go_text,25,(255,255,255),"pixelifysansregular",(173,405))
    display_money(screen,player)

    return button_clicked

