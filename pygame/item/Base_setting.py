import pygame



def wallinit(fig_path):
    distance = 200

    wall = pygame.image.load(fig_path + 'wall.png').convert_alpha()
    wall_width = wall.get_width()
    wall_height = wall.get_height()
    a={
        'distance':distance,
        'wall_width':wall_width,
        'wall_height':wall_height,
        'wall':wall
    }
    return  a

def walldisplay(screen_height,wall_height,screen,wall,distance):
    for height in range(0, screen_height, wall_height):
        screen.blit(wall, (distance, height))

if __name__ == '__main__':
    wallinit()
