import pygame
from pygame.rect import Rect


class Intersection:

    def __init__(self, left, top, width, length):
        self.width = width
        self.length = length
        self.left = left
        self.top = top
        self.hasStone = False
        self.owner = None
        self.rect = Rect(left, top, width, length)
        self.cpuColor = (0,128,128)
        self.playerColor = (128,0,128)
        self.stoneRadius = 8

    def setOwner(self, owner):
        self.owner = owner

    def click(self):
        self.hasStone = True

    def stonePlaced(self):
        return self.hasStone

    def draw(self, surface, x, y,):
        pygame.draw.rect(surface, (255, 255, 255), self.rect)
        surface.blit(surface, (x, y))

    def placeStone(self, surface):
        if self.owner == "CPU":
            color = self.cpuColor
        else:
            color = self.playerColor
        pygame.draw.circle(surface, color, (self.left + (self.width/2), self.top + (self.length/2)), self.stoneRadius)
