import pygame
import gc
import pygame_gui
import os
import random
from helper import display_money
from Player import *

properties = {1:("knox", "brown_1"), 2: ("talbert", "brown_2"), 4: ("commons", "commons"), 6: ("cfa", "cyan_1"), 7: ("slee", "cyan_2"), 9: ("fron", "pink_1"), 11:("nsc","pink_2") , 12:("su","su"), 14:("bell", "orange_1"), 15:("davis", "orange_2"), 17: ("obrian", "red_1"), 19: ("baldy", "red_2"), 20: ("lock","lock"), 21: ("ketter", "yellow_1"), 22 :("furnas","yellow_2"), 25:("hochst","green_1"), 26:("cooke","green_2"), 28: ("alumni","alumni"), 30: ("norton", "blue_1"), 31: ("capen", "blue_2")}

property_cost = {"brown": 240, "cyan": 2000, "pink":4000, "orange":6000, "red": 20000, "yellow": 40000, "green": 200000, "blue":200000, "su":2000, "commons":1500, "alumni":175000, "lock":26300 }

player = None
#Jail 33:(50, 420)
positionsxy = {0:(259, 429), 1:(225, 429), 2:(200, 429), 3:(175, 429), 4:(150, 429), 5:(125, 429), 6:(100, 429), 7:(75, 429), 8:(30, 439), 
               9:(37, 395), 10: (37, 370), 11:(37, 345), 12: (37, 320), 13:(37, 295), 14:(37, 270), 15:(37, 245), 16:(37, 210),
                17:(75, 210), 18:(100, 210), 19:(125, 210), 20:(150, 210), 21:(175, 210), 22:(200, 210), 23:(225, 210), 24:(259, 210),
                25: (259, 245), 26:(259, 270),27: (259, 295),28:(259, 320), 29:(259, 345), 30:(259, 370), 31:(259, 395), 32:(259, 429)
                }
def clear_screen(screen):
    screen.fill((255, 255, 255))
    pygame.display.flip()
    gc.collect()


clock = pygame.time.Clock()
board = pygame.image.load("./images/board/board.png")
board_rect = board.get_rect(topleft=(0,159))
moneybar = pygame.image.load("./images/board/moneybar.png")
right_button = pygame.image.load('./images/board/right.png')
left_button = pygame.image.load('./images/board/left.png')
navbar = pygame.image.load('./images/board/navbar.png')
lb_rect = pygame.Rect((34,519),left_button.get_size())
rb_rect = pygame.Rect((259,519),right_button.get_size())
one = pygame.image.load('./images/board/dice/one.png')
two = pygame.image.load('./images/board/dice/two.png')
three = pygame.image.load('./images/board/dice/three.png')
four = pygame.image.load('./images/board/dice/four.png')
five = pygame.image.load('./images/board/dice/five.png')
six = pygame.image.load('./images/board/dice/six.png')
grey = pygame.image.load('./images/Grey.png')
grey_rect = grey.get_rect(topleft= (0,0))
alumni = pygame.image.load("./images/properties/alumni.png")
baldy = pygame.image.load("./images/properties/baldy.png")
bell = pygame.image.load("./images/properties/bell.png")
capen = pygame.image.load("./images/properties/capen.png")
cfa = pygame.image.load("./images/properties/cfa.png")
commons = pygame.image.load("./images/properties/commons.png")
cooke = pygame.image.load("./images/properties/cooke.png")
davis = pygame.image.load("./images/properties/davis.png")
fron = pygame.image.load("./images/properties/fron.png")
furnas = pygame.image.load("./images/properties/furnas.png")
hochst = pygame.image.load("./images/properties/hochst.png")
ketter = pygame.image.load("./images/properties/ketter.png")
knox = pygame.image.load("./images/properties/knox.png")
lock = pygame.image.load("./images/properties/lock.png")
norton = pygame.image.load("./images/properties/norton.png")
nsc = pygame.image.load("./images/properties/nsc.png")
obrian = pygame.image.load("./images/properties/obrian.png")
slee = pygame.image.load("./images/properties/slee.png")
su = pygame.image.load("./images/properties/su.png")
talbert = pygame.image.load("./images/properties/talbert.png")
upgrade = pygame.image.load("./images/upgrade.png")
upgrade_rect = upgrade.get_rect(topleft=(110,404))
buy = pygame.image.load("./images/buy.png")
buy_rect = buy.get_rect(topleft=(110,404))

imgs = {
    "hat":pygame.image.load('./images/board/hat.png'),
    "shoe":pygame.image.load('./images/board/shoe.png'),
    "ship":pygame.image.load('./images/board/ship.png'),
    "iron":pygame.image.load('./images/board/iron.png'),
    "horse":pygame.image.load('./images/board/horse.png'),
    "car":pygame.image.load('./images/board/car.png'),
    "wheel_barrel":pygame.image.load('./images/board/wheel_barrel.png'),

}

# Flag to prevent starting a new dice roll while one is running
dice_running = False
buytoggle = False
rolling = False

def button_clicked(screen,event_pos):
    global dice_running
    global buytoggle
    global rolling
    if(rb_rect.collidepoint(event_pos)):
        return "buffs"
    elif(lb_rect.collidepoint(event_pos)):
        return "profile" 
    elif(board_rect.collidepoint(event_pos)) and not buytoggle and rolling == False:
        rolldice(screen)
        return None
    elif (upgrade_rect.collidepoint(event_pos)) and buytoggle:
        buyprop(screen)
    elif (buy_rect.collidepoint(event_pos)) and buytoggle:
        buyprop(screen)
    elif grey_rect.collidepoint(event_pos) and buytoggle:
        screen.blit(sprite, positionsxy[player.position])
        screen.blit(board, (0,159))   
        screen.blit(moneybar, (0,0))
        screen.blit(navbar,(0,502))
        screen.blit(sprite, positionsxy[player.position])
        screen.blit(right_button, rb_rect)
        screen.blit(left_button, lb_rect)
        display_money(screen, player)
        buytoggle = False


def playdiceone(roll1, screen):
    global click
    position = player.position
    for i in range(15):
        screen.blit(board,(0,159))
        screen.blit(sprite, positionsxy[player.position])
        num = random.randint(1,6)
        if num == 1:
            screen.blit(one,(110, 280) )
        elif num == 2:
            screen.blit(two,(110, 280) )
        elif num == 3:
            screen.blit(three,(110, 280) )
        elif num == 4:
            screen.blit(four,(110, 280) )
        elif num == 5:
            screen.blit(five,(110, 280) )
        elif num == 6:
            screen.blit(six,(110, 280) )
        clock.tick(10)
        pygame.display.flip()
    
    screen.blit(board,(0,159))
    screen.blit(roll1,(110, 280))
    screen.blit(sprite, positionsxy[position])

def playdicetwo(roll1, roll2, screen):
    global click
    position = player.position
    for i in range(15):
        screen.blit(board,(0,159))
        screen.blit(sprite, positionsxy[player.position])
        num1 = random.randint(1,6)
        num2 = random.randint(1,6)
        if num1 == 1:
            screen.blit(one,(69, 280) )
        elif num1 == 2:
            screen.blit(two,(69, 280) )
        elif num1 == 3:
            screen.blit(three,(69, 280) )
        elif num1 == 4:
            screen.blit(four,(69, 280) )
        elif num1 == 5:
            screen.blit(five,(69, 280) )
        elif num1== 6:
            screen.blit(six,(69, 280) )
        if num2 == 1:
            screen.blit(one,(155, 280))
        elif num2 == 2:
            screen.blit(two,(155, 280))
        elif num2 == 3:
            screen.blit(three,(155, 280))
        elif num2 == 4:
            screen.blit(four,(155, 280))
        elif num2 == 5:
            screen.blit(five,(155, 280))
        elif num2 == 6:
            screen.blit(six,(155, 280))
        clock.tick(10)
        pygame.display.flip()
    screen.blit(board,(0,159))
    screen.blit(roll1,(69, 280))
    screen.blit(roll2,(155, 280))
    screen.blit(sprite, positionsxy[position])

def getrollvalue(roll):
    if roll == 1:
        return one
    elif roll == 2:
        return two
    elif roll == 3:
        return three
    elif roll == 4:
        return four
    elif roll == 5:
        return five
    elif roll == 6:
        return six


def buyprop(screen):
    
    global buytoggle
    space = player.position
    info = properties[space]
    color = info[1].split("_")[0]
    price = property_cost[color]
    player.update_property(info[1], price)
    screen.blit(sprite, positionsxy[space])
    screen.blit(board, (0,159))   
    screen.blit(moneybar, (0,0))
    screen.blit(navbar,(0,502))
    screen.blit(sprite, positionsxy[player.position])
    screen.blit(right_button, rb_rect)
    screen.blit(left_button, lb_rect)
    display_money(screen, player)
    buytoggle = False


def rolldice(screen):
    pygame.event.clear()
    roll_raw_num = random.randint(1,6)
    rollimg = getrollvalue(roll_raw_num)
    roll2_raw_num = 0
    if "hertz" in player.buffs:
        roll2_raw_num = random.randint(1,6)
        if "hunt" in player.buffs:
            if(roll_raw_num == roll2_raw_num):
                roll_raw_num += 3
        roll2img = getrollvalue(roll2_raw_num)
        playdicetwo(rollimg, roll2img, screen)
        player.roll(roll_raw_num+ roll2_raw_num)
    else:
        playdiceone(rollimg, screen)
        player.roll(roll_raw_num)
    new_pos = roll_raw_num + roll2_raw_num + player.position
    player.position += roll_raw_num + roll2_raw_num

    if player.position > 32:
        player.position %= 32
        player.pass_go()
    screen.blit(board, (0,159))
    screen.blit(sprite, positionsxy[player.position])
    if "hertz" in player.buffs:
        screen.blit(rollimg,(69, 280))
        screen.blit(roll2img,(155, 280))
    else:
        screen.blit(rollimg,(110, 280))
    checksquare(screen)
    screen.blit(moneybar, (0,0))
    display_money(screen, player)
    pygame.event.clear()


def checksquare(screen):
    global buytoggle
    if player.position in properties.keys():
        squareinfo = properties[player.position]
        property = squareinfo[1]
        price = property_cost[squareinfo[1].split("_")[0]]
        color = property.split("_")[0]
        if property in player.properties and player.money > price:
            price = property_cost[color]
            propertyname = squareinfo[0]
            screen.blit(grey)
            screensurface = pygame.image.load(f"./images/properties/{propertyname}.png")
            screen.blit(screensurface,(57, 179))
            screen.blit(upgrade,(110, 445))
            buytoggle = True
        elif property not in player.properties and player.money > price:
            price = property_cost[color]
            propertyname = squareinfo[0]
            screen.blit(grey)
            screensurface = pygame.image.load(f"./images/properties/{propertyname}.png")
            screen.blit(screensurface,(57, 179))
            screen.blit(buy, (110, 445))
            buytoggle = True




def render_board(screen, Player):
    global player
    global sprite
    player = Player
    imgs[player.piece] = pygame.transform.scale(imgs[player.piece], (25, 25))
    sprite = imgs[player.piece]
    screen.blit(board, (0,159))   
    screen.blit(navbar,(0,502))
    screen.blit(moneybar, (0,0))
    screen.blit(sprite, positionsxy[player.position])
    screen.blit(right_button, rb_rect)
    screen.blit(left_button, lb_rect)
    display_money(screen, player)
    return button_clicked

