import pygame as pg
from group import Group
from timer import Timer
from globals import *

MAP_COLOR = (152, 166, 212)

AUTOSAVE_INTERVAL = 60 * 1000


class Scene:
    def __init__(self, screen: pg.Surface):
        self.screen = screen
        self.group = Group(screen)
        self.autosave = Timer(AUTOSAVE_INTERVAL, True, self.group.save)
        self.autosave.start()

    def update(self):
        self.group.update()
        self.autosave.update()

    def draw(self):
        self.screen.fill(MAP_COLOR)
        self.group.draw(self.screen)

    def exit(self):
        self.autosave.stop()
        self.group.save()
