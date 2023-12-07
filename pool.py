import pygame as pg
from entity import Entity
from player import Player
from globals import *


class Pool(pg.sprite.Group):
    def __init__(self):
        super().__init__()

    def add_player(self, x, y):
        Player([self], PLAYER_WIDTH, PLAYER_HEIGHT, (x, y))

    def add_entity(self, x, y):
        Entity([self], ENTITY_WIDTH, ENTITY_HEIGHT, (x, y))
