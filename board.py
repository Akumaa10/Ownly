import pygame
import gc
import pygame_gui
import os
import random
from helper import display_money
from Player import *

player = None
#Jail 33:(50, 420)
positionsxy = {1:(225, 429), 2:(200, 429), 3:(175, 429), 4:(150, 429), 5:(125, 429), 6:(100, 429), 7:(75, 429), 8:(30, 439), 
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
sprite = pygame.image.load("./images/board/sprite.png")
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

# Flag to prevent starting a new dice roll while one is running
dice_running = False


def button_clicked(screen,event_pos):
    global dice_running
    if(rb_rect.collidepoint(event_pos)):
        return "buffs"
    elif(lb_rect.collidepoint(event_pos)):
        return "profile" 
    elif(board_rect.collidepoint(event_pos)):
        rolldice(screen)
        return None
    

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
            screen.blit(one,(75, 280) )
        elif num1 == 2:
            screen.blit(two,(75, 280) )
        elif num1 == 3:
            screen.blit(three,(75, 280) )
        elif num1 == 4:
            screen.blit(four,(75, 280) )
        elif num1 == 5:
            screen.blit(five,(75, 280) )
        elif num1== 6:
            screen.blit(six,(75, 280) )
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
    screen.blit(roll1,(75, 280))
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


def rolldice(screen):
    roll_raw_num = random.randint(1,6)
    rollimg = getrollvalue(roll_raw_num)
    roll2_raw_num = 0
    if "doubledice" in player.buffs:
        roll2_raw_num = random.randint(1,6)
        roll2img = getrollvalue(roll2_raw_num)
        playdicetwo(rollimg, roll2img, screen)
        player.roll(roll_raw_num+ roll2_raw_num)
    else:
        playdiceone(rollimg, screen)
        player.roll(roll_raw_num)
    new_pos = roll_raw_num + roll2_raw_num + player.position
    player.position += roll_raw_num + roll2_raw_num
    if player.position > 40:
        player.position %= 40
        player.pass_go()
    screen.blit(board, (0,159))
    screen.blit(sprite, positionsxy[new_pos])
    if "doubledice" in player.buffs:
        screen.blit(rollimg,(75, 280))
        screen.blit(roll2img,(155, 280))
    else:
        screen.blit(rollimg,(110, 280))


def render_board(screen, Player):
    global player
    player = Player
    screen.blit(board, (0,159))   
    screen.blit(moneybar, (0,0))
    screen.blit(navbar,(0,502))
    screen.blit(sprite, positionsxy[player.position])
    screen.blit(right_button, rb_rect)
    screen.blit(left_button, lb_rect)
    display_money(screen, player)
    return button_clicked

