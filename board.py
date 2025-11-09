import pygame
import random

moneybase = 10
playermoney = 10
spaces = 40
currentspace = 0
properties = {}

spaces_prices = {"pink":60, "orange": 100, "red": 120, "yellow": 200, "green":250, "dark_blue":300, "brown": 375, "light_blue":450}


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


