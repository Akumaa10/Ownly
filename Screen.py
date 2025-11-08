import pygame
import pygame_gui
import random

moneybase = 10
playermoney = 10
spaces = 40
currentspace = 0
upgrades = {"doubledice":False}

properties = {
    "pink": ["prop1", "prop2"],
    "orange": ["prop1", "prop2"],
    "red": ["prop1", "prop2"], 
    "yellow": ["prop1", "prop2"], 
    "green": ["prop1", "prop2"], 
    "dark_blue":["prop1", "prop2"], 
    "brown":["prop1", "prop2"], 
    "light_blue":["prop1", "prop2"]
    }
propertymulti = {"pink": 10, "orange":20, "red":30, "yellow":40, "green":50, "dark_blue":60, "brown":70, "light_blue":80}
owned_spaces = {"pink":0, "orange":0, "red":0, "yellow":0, "green":0, "dark_blue":0, "brown":0, "light_blue":0}

spaces_prices = {"pink":60, "orange": 100, "red": 120, "yellow": 200, "green":250, "dark_blue":300, "brown": 375, "light_blue":450}

def getmoneymulti():
    total = 0
    for color in owned_spaces:
        total += owned_spaces[color] * propertymulti[color]
    return total

def collecttuituion():
    total = 0
    for color in owned_spaces:
        total += owned_spaces[color] * propertymulti[color]
    return total

#checks if player lands on property and if a popup should be triggered
# needs properties dict 
def landedonproperty():
    global currentspace
    global playermoney
    if currentspace in properties:
        color = properties[currentspace]
        price = spaces_prices[color]
        if playermoney >= price:
            return True
    return False

def rolldice():
    global currentspace
    global playermoney

    roll1 = random.randint(1,6)
    roll2 = 0
    if upgrades["doubledice"]:
        roll2 = random.randint(1,6)
    currentspace += roll1 + roll2
    playermoney += (roll1 + roll2) * moneybase

    if currentspace > 40:
        currentspace %= 40
        playermoney += 200 + collecttuituion()



def checkmouseclick(x,y):
    if y < 638:
        rolldice()
        return
    #add functionality for navbar buttons here


    return



pygame.init()
SCREEN_W, SCREEN_H = 400, 719
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
navbar = pygame.image.load("images/Rectangle_1.png").convert_alpha()
screen.fill((255, 255, 255))
navbar = pygame.transform.scale(navbar, (SCREEN_W, 100))

clickarea = ((0,700), (400, 100))

running = True
while running:
    screen.blit(navbar, (0, 638))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            coord = event.pos
            checkmouseclick(coord[0], coord[1])
    pygame.display.flip()
pygame.quit()
