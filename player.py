import pygame as pg
from entity import Entity

PLAYER_SIZE = (30, 30)
PLAYER_COLOR = (18, 24, 43)


class Player(Entity):
    def __init__(self, group: pg.sprite.Group, params: dict):
        super(Player, self).__init__(group, params, PLAYER_SIZE, PLAYER_COLOR)
