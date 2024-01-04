import random #For generating random numbers
import sys #sys.exit() will be used
import pygame
from pygame.locals import * #basic pygame imports
#Global variables:
FPS = 32
SCREENWIDTH = 289
SCREENHEIGHT = 511
SCREEN = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
GROUNDY = SCREENHEIGHT * 0.8
GAME_SPRITES = {}
GAME_SOUNDS = {}
PLAYER = {}