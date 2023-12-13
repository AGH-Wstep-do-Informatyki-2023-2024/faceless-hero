import pygame as pg
from interval import Interval
from group import Group
from globals import *

MAP_COLOR = (152, 166, 212)

AUTOSAVE_INTERVAL = 60


class Scene:
    def __init__(self, screen: pg.Surface):
        self.screen = screen
        self.group = Group(screen)
        self.autosave = Interval(AUTOSAVE_INTERVAL, self.group.save)

    def update(self):
        self.group.update()

    def draw(self):
        self.screen.fill(MAP_COLOR)
        self.group.draw(self.screen)

    def exit(self):
        self.autosave.stop()
        self.group.save()
