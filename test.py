#_*_ coding:utf-8 _*_
import pygame
from pygame.locals import *
pygame.init()
# screen=pygame.display.set_mode((800,600))
running=True

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player,self).__init__()
        self.surf=pygame.Surface((75,75))
        self.surf.fill((255,255,255))
        self.rect=self.surf.get_rect()
#
#     def update(self, press_keys):
#         for event in press_keys:
#             if event.key==[K_UP]:
#                 self.rect.move_ip(0, -5)
#             if press_keys[K_DOWN]:
#                 self.rect.move_ip(0, 5)
#             if press_keys[K_LEFT]:
#                 self.rect.move_ip(-5, 0)
#             if press_keys[K_RIGHT]:
#                 self.rect.move_ip(0, 5)
player=Player()
#
while running:
    screen=pygame.display.set_mode((800,600))
    press_keys = pygame.event.get()
    print (press_keys)
    for event in  press_keys:
        # print (event)
        if event.type==KEYDOWN:
            # print (event.key)
            if event.key==K_ESCAPE:
                print (event.key)
                running=False
            # elif event.key==K_UP:
            #     player.rect.move_ip(0, -5)
            # elif event.key==K_DOWN:
            #     player.rect.move_ip(0, 5)
            # elif event.key==K_LEFT:
            #     player.rect.move_ip(-5, 0)
            # elif event.key==K_RIGHT:
            #     player.rect.move_ip(5, 0)
        if event.type==QUIT:
                running=False
    # if press_keys[K_UP]:
    #     player.rect.move_ip(0, -5)
    if press_keys[K_DOWN]:
        player.rect.move_ip(0, 5)
    if press_keys[K_LEFT]:
        player.rect.move_ip(-5, 0)
    if press_keys[K_RIGHT]:
        player.rect.move_ip(5, 0)
    player.update(press_keys)
    screen.blit(player.surf,player.rect)
    pygame.display.flip()
