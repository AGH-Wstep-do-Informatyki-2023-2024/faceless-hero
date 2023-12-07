import json
import pygame as pg
from entity import Entity
from player import Player
from pool import Pool


class Database:
    def __init__(self, file):
        self.file = file

    def save(self, pool):
        data = []
        for sprite in pool:
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
        pool = Pool()
        try:
            with open(self.file) as file:
                data = json.load(file)
                for entity in data:
                    x, y = entity["x"], entity["y"]
                    match entity["type"]:
                        case "player":
                            pool.add_player(x, y)
                        case "normal":
                            pool.add_entity(x, y)
        except FileNotFoundError:
            pool.add_player(100, 100)
            pool.add_entity(10, 10)
            pool.add_entity(40, 10)
            self.save(pool)
        return pool
