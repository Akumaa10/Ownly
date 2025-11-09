import pygame
import gc
import pygame_gui
import os
import random

player = None
click = []
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
        clock.tick(1000)
        if click == []:
            click.append(1)
            playdiceone(one,screen)
        else:
            return None

        return None
    

def playdiceone(roll1, screen):
    global click
    print("rolling")
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
    screen.blit(roll1,(110, 280))
    clock.tick(300)
    click.pop()

# def rolldice(screen):
#     global currentspace
#     global playermoney
#     playdiceone(roll1, screen)

#     roll1 = random.randint(1,6)
#     roll2 = 0
#     if buffs["doubledice"]:
#         roll2 = random.randint(1,6)
#     currentspace += roll1 + roll2
#     playermoney += (roll1 + roll2) * moneybase
#     landedonproperty()
#     print(currentspace, "Current space")
#     if currentspace > 40:
#         currentspace %= 40
#         playermoney += 200 + collecttuituion()



def render_board(screen, Player):
    global player
    player = Player
    screen.blit(board, (0,159))   
    screen.blit(moneybar, (0,0))
    screen.blit(navbar,(0,502))
    screen.blit(sprite, positionsxy[player.position])
    screen.blit(right_button, rb_rect)
    screen.blit(left_button, lb_rect)
    return button_clicked

