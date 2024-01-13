import pygame as pg
from globals import *


class Entity(pg.sprite.Sprite):
    def __init__(
        self,
        group: pg.sprite.Group,
        size: tuple[int, int],
        color: tuple[int, int, int],
        params: dict[str, int],
    ):
        super().__init__(group)
        self.image = pg.Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect(
            bottomleft=(params["x"], MAP_SIZE[1] - MAP_GROUND_OFFSET)
        )

    def params(self):
        return {"x": self.rect.x}
