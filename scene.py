import pygame as pg
from entity import Entity
from player import Player


class Scene:
    def __init__(self, game):
        self.game = game

        self.entities = pg.sprite.Group()
        Player([self.entities], 20, 20, (50, 50))
        Entity([self.entities], 20, 20, (10, 10))

    def update(self):
        self.entities.update()

    def draw(self):
        self.game.screen.fill("crimson")
        self.entities.draw(self.game.screen)
