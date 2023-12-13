import json
import pygame as pg
from entity import Entity
from player import Player

MOVE_DELTA = 10
MOVE_BORDER = 0.1

MAP_SIZE = (1000, 1000)

DB_FILE = "faceless_hero.json"
DB_DEFAULT = "faceless_hero_default.json"


class Group(pg.sprite.Group):
    def __init__(self, screen: pg.Surface):
        super().__init__()
        self.screen = screen
        self.load()

    def load(self):
        try:
            with open(DB_FILE) as f:
                data = json.load(f)
        except FileNotFoundError:
            with open(DB_DEFAULT) as f:
                data = json.load(f)

        self.entities = [Entity(self, params) for params in data["entities"]]
        self.player = Player(self, data["player"])
        self.window = data["window"]

    def save(self):
        with open(DB_FILE, "w") as f:
            json.dump(
                {
                    "window": self.window,
                    "player": self.player.params(),
                    "entities": [entity.params() for entity in self.entities],
                },
                f,
            )

    def move_x(self, delta: int):
        width = self.screen.get_width()
        ratio = self.player.rect.x / width

        if (
            (MOVE_BORDER < ratio < 1 - MOVE_BORDER)
            or (
                ratio > 1 - MOVE_BORDER
                and (delta < 0 or self.window["x"] == MAP_SIZE[0] - width)
            )
            or (ratio < MOVE_BORDER and (delta > 0 or self.window["x"] == 0))
        ):
            self.player.rect.x = max(
                0, min(width - self.player.rect.width, self.player.rect.x + delta)
            )
        else:
            self.window["x"] = max(
                0, min(MAP_SIZE[0] - width, self.window["x"] + delta)
            )
            for entity in self.entities:
                entity.rect.x -= delta

    def move_y(self, delta: int):
        height = self.screen.get_height()
        ratio = self.player.rect.y / height

        if (
            (MOVE_BORDER < ratio < 1 - MOVE_BORDER)
            or (
                ratio > 1 - MOVE_BORDER
                and (delta < 0 or self.window["y"] == MAP_SIZE[1] - height)
            )
            or (ratio < MOVE_BORDER and (delta > 0 or self.window["y"] == 0))
        ):
            self.player.rect.y = max(
                0, min(height - self.player.rect.height, self.player.rect.y + delta)
            )
        else:
            self.window["y"] = max(
                0, min(MAP_SIZE[1] - height, self.window["y"] + delta)
            )
            for entity in self.entities:
                entity.rect.y -= delta

    def update(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_a] and not keys[pg.K_d]:
            self.move_x(-MOVE_DELTA)
        if keys[pg.K_d] and not keys[pg.K_a]:
            self.move_x(MOVE_DELTA)
        if keys[pg.K_s] and not keys[pg.K_w]:
            self.move_y(MOVE_DELTA)
        if keys[pg.K_w] and not keys[pg.K_s]:
            self.move_y(-MOVE_DELTA)
