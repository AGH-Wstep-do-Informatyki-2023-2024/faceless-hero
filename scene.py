import json
import pygame as pg
from entity import Entity
from timer import Timer
from globals import *


class Scene:
    def __init__(self, screen: pg.Surface):
        self.screen = screen
        self.group = pg.sprite.Group()
        self.load_data()
        self.load_bg()
        self.autosave = Timer(DB_AUTOSAVE_INTERVAL, True, self.save)
        self.autosave.start()

    def load_data(self):
        try:
            with open(DB_FILE) as f:
                data = json.load(f)
        except FileNotFoundError:
            with open(DB_DEFAULT) as f:
                data = json.load(f)
        self.window = data["window"]
        self.player = Entity(self.group, PLAYER_SIZE, PLAYER_COLOR, data["player"])
        self.entities = [
            Entity(self.group, ENTITY_SIZE, ENTITY_COLOR, params)
            for params in data["entities"]
        ]

    def load_bg(self):
        self.bg_images = [
            pg.transform.scale(
                pg.image.load(
                    f"assets/layers/parallax-demon-woods-{i}.png"
                ).convert_alpha(),
                WINDOW_SIZE,
            )
            for i in range(3, -1, -1)
        ]

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

    def move(self, delta: int):
        left_ratio = self.player.rect.x / WINDOW_SIZE[0]
        right_ratio = (self.player.rect.x + self.player.rect.width) / WINDOW_SIZE[0]
        if (
            (PLAYER_MOVE_BORDER < left_ratio and right_ratio < 1 - PLAYER_MOVE_BORDER)
            or (
                right_ratio >= 1 - PLAYER_MOVE_BORDER
                and (delta < 0 or self.window["x"] == MAP_SIZE[0] - WINDOW_SIZE[0])
            )
            or (
                left_ratio <= PLAYER_MOVE_BORDER
                and (delta > 0 or self.window["x"] == 0)
            )
        ):
            self.player.rect.x = max(
                0,
                min(
                    WINDOW_SIZE[0] - self.player.rect.width, self.player.rect.x + delta
                ),
            )
        else:
            self.window["x"] = max(
                0, min(MAP_SIZE[0] - WINDOW_SIZE[0], self.window["x"] + delta)
            )
            for entity in self.entities:
                entity.rect.x -= delta

    def update(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_d]:
            self.move(PLAYER_MOVE_DELTA)
        elif keys[pg.K_a]:
            self.move(-PLAYER_MOVE_DELTA)

    def draw(self):
        for i in range(5):
            for bg_image in self.bg_images:
                self.screen.blit(bg_image, (i * WINDOW_SIZE[0], 0))
        self.group.draw(self.screen)

    def exit(self):
        self.autosave.stop()
        self.save()
