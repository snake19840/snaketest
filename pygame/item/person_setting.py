import math

import pygame
from pygetwindow import Rect




def personinit(fig_path):
    rect_bg = Rect(50, 50, 133, 142)
    bg_speed = 2
    begger_pos = []
    begger = pygame.image.load(fig_path + 'person.png').convert_alpha()
    begger_width = begger.get_width()
    begger_height = begger.get_height()
    a = {
        'rect_bg': rect_bg,
        'bg_speed': bg_speed,
        'begger_pos': begger_pos,
        'begger': begger,
        'begger_width': begger_width,
        'begger_height': begger_height
    }
    return a

def rota(begger_height, begger_width, screen,begger_pos, begger_img):


    position = pygame.mouse.get_pos()
    angle = math.atan2(position[1] - (begger_pos[1] + begger_height),
                       position[0] - (begger_pos[0] + begger_width))
    begger_rot = pygame.transform.rotate(begger_img, 360 - angle * 57.29)
    begger_pos1 = (begger_pos[0] - begger_rot.get_rect().width / 2,
                   begger_pos[1] - begger_rot.get_rect().height / 2)
    screen.blit(begger_rot, begger_pos1)





