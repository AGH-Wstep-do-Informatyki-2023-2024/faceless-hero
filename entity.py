import pygame as pg

ENTITY_SIZE = (15, 15)
ENTITY_COLOR = (36, 48, 86)


class Entity(pg.sprite.Sprite):
    def __init__(
        self,
        group: pg.sprite.Group,
        params: dict,
        size: tuple[int, int] = ENTITY_SIZE,
        color: tuple[int, int, int] = ENTITY_COLOR,
    ):
        super(Entity, self).__init__([group])

        self.image = pg.Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(params["x"], params["y"]))

        self.vx = 0
        self.vy = 0
        self.mass = 0

    def params(self):
        return {"x": self.rect.x, "y": self.rect.y}
