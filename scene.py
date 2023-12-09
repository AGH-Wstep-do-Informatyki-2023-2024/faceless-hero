from interval import Interval
from group import Group
from globals import *


class Scene:
    def __init__(self, game):
        self.game = game
        self.entities = Group(AUTOSAVE_FILE)
        self.autosave = Interval(AUTOSAVE_INTERVAL, self.entities.save)

    def update(self):
        self.entities.update()

    def draw(self):
        self.game.screen.fill("crimson")
        self.entities.draw(self.game.screen)

    def exit(self):
        self.autosave.stop()
        self.entities.save()
