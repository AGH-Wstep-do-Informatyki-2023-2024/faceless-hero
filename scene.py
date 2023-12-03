from interval import Interval
from db import Database
from globals import *


class Scene:
    def __init__(self, game):
        self.game = game
        self.db = Database(AUTOSAVE_FILE)
        self.autosave = Interval(AUTOSAVE_INTERVAL, self.save)
        self.entities = self.db.load()

    def update(self):
        self.entities.update()

    def draw(self):
        self.game.screen.fill("crimson")
        self.entities.draw(self.game.screen)

    def save(self):
        self.db.save(self.entities)

    def exit(self):
        self.autosave.stop()
        self.save()
