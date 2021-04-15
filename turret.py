import pygame
import math

class Turret():
    def __init__(self, screen, posx, posy):
        print("Kekium")
        self.img = pygame.image.load("turret.png").convert()
        self.img.set_colorkey((0,0,0))

        self.screen = screen
        self.posx = posx
        self.posy = posy

    def update(self, player_posx, player_posy):
        rel_x, rel_y = player_posx - (self.posx-25), player_posy - (self.posy-25)

        angle = ((180 / math.pi) * -math.atan2(rel_y, rel_x)) + 90


        img_copy = pygame.transform.rotate(self.img, int(angle))
        self.screen.blit(img_copy, (self.posx - int(img_copy.get_width() / 2), self.posy - int(img_copy.get_height() / 2)))
