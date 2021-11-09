import random, sys, copy, os, pygame
from pygame.locals import *

FPS = 30
WINWIDTH = 800
WINHEIGHT =  600
HALF_WINWIDTH = int(WINWIDTH / 2)
HALF_WINHEIGHT = int(WINHEIGHT / 2)

TITLEWIDTH = 50
TITLEHEIGHT = 85
TITLEFLOORHEIGHT = 45

CAM_MOVE_SPEED = 5

OUTSIDE_DECORATION_PCT = 20

BRIGHTBLUE = (0, 170, 255)
WHITE = (255, 255, 255)
BGCOLOR = BRIGHTBLUE
TEXTCOLOR = WHITE

UP = "up"
DOWN = "down"
LEFT = "left"
RIGHT = "right"

def main():
    global FPSCLOCK, DISPLAYSURF, IMAGESDICT, TITLEMAPPING, OUTSIDEDECOMAPPING, CURRENTIMAGE

    pygame.init()
    FPSCLOCK = pygame.time.Clock()

    DISPLAYSURF = pygame.display.set_mode((WINWIDTH, WINHEIGHT))

    pygame.set_caption("star pusher")
    BASICFONT = pygame.font.Font("freesansbold.ttf", 18)


    IMAGESDICT = {"uncoverd goal": pygame.image.load("RedSelector.png"), "covered goal": pygame.image.load("selector.png"), "star": pygame.image.load("star.png"), "corner": pygame.image.load("Wall Block Tall.png"), "wall": pygame.image.load("Wood Block Tall.png"), "inside floor": pygame.image.load("Plain Block.png"), "outside floor": pygame.image.load("Grass Block.png"), "title": pygame.image.load("star_title.png"), "solved": pygame.image.load("star_solved.png"), "princess": pygame.image.load("princess.png"), "boy": pygame.image.load("boy.png"), "catgirl": pygame.image.load("catgirl.png"), "horngirl": pygame.image.load("horngirl"), "pinkgirl": pygame.image.load("pinkgirl.png"), "rock": pygame.image.load("Rock.png"), "short tree": pygame.image.load("Short_Short.png"), "tall tree": pygame.image.load("Tall_Tree.png"), "ugly tree": pygame.image.load("Ugly_Tree.png")}