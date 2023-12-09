import json
import pygame as pg
from entity import Entity
from player import Player
from globals import *


class Group(pg.sprite.Group):
    def __init__(self, file):
        super().__init__()
        self.file = file
        try:
            with open(self.file) as f:
                data = json.load(f)
                for entity in data:
                    x, y = entity["x"], entity["y"]
                    match entity["type"]:
                        case "player":
                            self.add_player(x, y)
                        case "normal":
                            self.add_entity(x, y)
        except FileNotFoundError:
            self.add_player(100, 100)
            self.add_entity(10, 10)
            self.add_entity(40, 10)
            self.save()

    def save(self):
        data = []
        for sprite in self:
            entity = {"x": sprite.rect.x, "y": sprite.rect.y}
            match sprite:
                case Player():
                    entity["type"] = "player"
                case Entity():
                    entity["type"] = "normal"
            data.append(entity)
        with open(self.file, "w") as f:
            json.dump(data, f)

    def add_player(self, x, y):
        Player([self], PLAYER_WIDTH, PLAYER_HEIGHT, (x, y))

    def add_entity(self, x, y):
        Entity([self], ENTITY_WIDTH, ENTITY_HEIGHT, (x, y))
