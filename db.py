import json
import pygame as pg
from entity import Entity
from player import Player
from globals import *


def player(group, pos):
    return Player([group], PLAYER_WIDTH, PLAYER_HEIGHT, pos)


def normal(group, pos):
    return Entity([group], ENTITY_WIDTH, ENTITY_HEIGHT, pos)


class Database:
    def __init__(self, file):
        self.file = file

    def save(self, group):
        data = []
        for sprite in group:
            entity = {"x": sprite.rect.x, "y": sprite.rect.y}
            match sprite:
                case Player():
                    entity["type"] = "player"
                case Entity():
                    entity["type"] = "normal"
            data.append(entity)
        with open(self.file, "w") as file:
            json.dump(data, file)

    def load(self):
        group = pg.sprite.Group()
        try:
            with open(self.file) as file:
                data = json.load(file)
                for entity in data:
                    pos = (entity["x"], entity["y"])
                    match entity["type"]:
                        case "player":
                            player(group, pos)
                        case "normal":
                            normal(group, pos)
        except FileNotFoundError:
            player(group, (100, 100))
            normal(group, (10, 10))
            normal(group, (40, 10))
            self.save(group)
        return group
