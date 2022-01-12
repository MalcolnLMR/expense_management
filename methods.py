import pygame as pg
from pygame.locals import *

def initPygame():
    Screen = getScreen()
    pg.init()
    Canvas = pg.display.set_mode(Screen, 0, 32)
    pg.display.set_caption("Iniciando")
    return Canvas

### Get width and Height from .txt file ###

def getScreen():
    Configs = open("settings.txt", "r")

    aux = Configs.readline().strip()
    listTemp = aux.split(';')
    screenX = int(listTemp[0])
    screenY = int(listTemp[1])

    Configs.close()

    return (screenX, screenY)

def coll_mouse_rect(mouseButton, rect):
    mousePos = pg.mouse.get_pos()    
    if pg.mouse.get_pressed() == mouseButton and rect.collidepoint(mousePos):
        return True
    else:
        return False