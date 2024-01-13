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
        self.offset = data["offset"]
        self.entities = [
            Entity(self.group, ENTITY_SIZE, ENTITY_COLOR, params, self.offset)
            for params in data["entities"]
        ]
        self.player = Entity(
            self.group, PLAYER_SIZE, PLAYER_COLOR, data["player"], self.offset
        )

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
                    "offset": self.offset,
                    "player": self.player.params(self.offset),
                    "entities": [
                        entity.params(self.offset) for entity in self.entities
                    ],
                },
                f,
            )

    def move(self, delta: int):
        left = self.player.rect.x
        right = left + self.player.rect.width
        if (
            (MOVE_BORDER < left and right < WINDOW_SIZE[0] - MOVE_BORDER)
            or (
                right >= WINDOW_SIZE[0] - MOVE_BORDER
                and (delta < 0 or self.offset == MAP_SIZE[0] - WINDOW_SIZE[0])
            )
            or (left <= MOVE_BORDER and (delta > 0 or self.offset == 0))
        ):
            self.player.rect.x = max(
                0,
                min(
                    WINDOW_SIZE[0] - self.player.rect.width, self.player.rect.x + delta
                ),
            )
        else:
            if self.offset + delta < 0:
                delta = -self.offset
            if self.offset + delta > MAP_SIZE[0] - WINDOW_SIZE[0]:
                delta = MAP_SIZE[0] - WINDOW_SIZE[0] - self.offset
            self.offset += delta
            for entity in self.entities:
                entity.rect.x -= delta

    def update(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_d]:
            self.move(MOVE_DELTA)
        elif keys[pg.K_a]:
            self.move(-MOVE_DELTA)

    def draw(self):
        for i in range(5):
            for j, bg_image in enumerate(self.bg_images):
                self.screen.blit(
                    bg_image,
                    (i * WINDOW_SIZE[0] - self.offset * (j + 1) * PARALLAX_SPEED, 0),
                )
        self.group.draw(self.screen)

    def exit(self):
        self.autosave.stop()
        self.save()
