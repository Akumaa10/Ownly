import pygame

def format_money(money):
    if(money >= 1000000000):
        return f"{money/1000000000:.1f}b"
    elif(money >= 1000000):
        return f"{money/1000000:.1f}m"
    elif(money >= 100000):
        return f"{money/1000:.1f}k"
    return str(money)

def display_money(screen,player):
    font = pygame.font.SysFont("ByteBounce", 80)
    money = font.render("$" + format_money(player.money),True,(60,83,39))
    money_rect = money.get_rect(center = (162,80))

    screen.blit(money,money_rect)