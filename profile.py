import pygame
import gc
import pygame_gui

from helper import display_text

def clear_screen(screen):
    screen.fill((255, 255, 255))
    pygame.display.flip()
    gc.collect()



imgs = {
    "main_page":pygame.image.load("./images/profile/main_page.png"),
    "last_right_arrow":pygame.image.load('./images/last_right_arrow.png'),
    "hat":pygame.image.load('./images/profile/hat.png'),
    "shoe":pygame.image.load('./images/profile/shoe.png'),
    "ship":pygame.image.load('./images/profile/ship.png'),
    "iron":pygame.image.load('./images/profile/iron.png'),
    "horse":pygame.image.load('./images/profile/horse.png'),
    "car":pygame.image.load('./images/profile/car.png'),
    "wheel_barrel":pygame.image.load('./images/profile/wheel_barrel.png'),

}

rect = {
    "last_right_arrow":pygame.Rect((235,509),imgs["last_right_arrow"].get_size()),
    "hat":pygame.Rect((97,42),imgs["hat"].get_size()),
    "shoe":pygame.Rect((97,42),imgs["shoe"].get_size()),
    "ship":pygame.Rect((97,42),imgs["ship"].get_size()),
    "iron":pygame.Rect((97,42),imgs["iron"].get_size()),
    "horse":pygame.Rect((97,42),imgs["horse"].get_size()),
    "car":pygame.Rect((97,42),imgs["car"].get_size()),
    "wheel_barrel":pygame.Rect((97,42),imgs["wheel_barrel"].get_size())
}

all_pieces = {"hat":(97,42),"shoe":(44,304),"ship":(129,304),"iron":(214,304),"horse":(44,392),"car":(129,392),"wheel_barrel":(214,392)}

def render_profile(screen,player):
    def button_clicked(screen,event_pos):
        if(rect["last_right_arrow"].collidepoint(event_pos)):
            return "board"
        for piece in all_pieces:
            if(rect[piece].collidepoint(event_pos)):
                all_pieces[player.piece] = all_pieces[piece]
                all_pieces[piece] = (97,42)
                player.piece = piece
        render_profile(screen,player)
        return None
    
    for img in imgs:
        if(img == player.piece):
            imgs[img] = pygame.transform.scale(imgs[img], (131, 131))
            rect[img] = pygame.Rect((97,42),imgs[img].get_size())
        elif(img in all_pieces):
            imgs[img] = pygame.transform.scale(imgs[img], (67, 67))
            rect[img] = pygame.Rect(all_pieces[img],imgs[img].get_size())
        screen.blit(imgs[img], rect.get(img,(0,0)))


    elapsed = (pygame.time.get_ticks() - player.start_time) // 1000
    days, remainder = divmod(elapsed,86400)
    hours,remainder = divmod(remainder,3600)
    minutes,remainder = divmod(remainder,60)
    time_text = f"{days:02}d:{hours:02}h:{minutes:02}m"
    display_text(screen,time_text,40,(0,0,0),"ByteBounce",(163,250))
    return button_clicked

