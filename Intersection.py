import pygame
from pygame.rect import Rect

class Intersection:

    def __init__(self, left, top, width, stoneRadius):
        self.width = width
        self.left = left
        self.top = top
        self.hasStone = False
        self.owner = None
        self.rect = Rect(left, top, width, width)
        self.cpuColor = (0,128,128)
        self.playerColor = (128,0,128)
        self.stoneRadius = stoneRadius

    def setOwner(self, owner):
        self.owner = owner

    def getOwner(self):
        return self.owner

    def getX(self):
        return self.left

    def getY(self):
        return self.top

    def getXY(self):
        return self.left, self.top

    def wasClicked(self, x, y):
        if self.left < x < (self.left + self.width):
            if self.top < y < (self.top + self.length):
                return True
        return False

    def click(self, turn):
        if not self.hasStone:
            self.owner = turn
            self.hasStone = True
        else:
            return -1


    def hasStone(self):
        return self.hasStone

    def draw(self, surface):
        if self.hasStone:
            self.drawStone(surface)

    def drawStone(self, surface):
        if self.owner == "CPU":
            color = self.cpuColor
        else:
            color = self.playerColor
        pygame.draw.circle(surface, color, (int(self.left+self.width/2), int(self.top+self.width/2)), self.stoneRadius)
