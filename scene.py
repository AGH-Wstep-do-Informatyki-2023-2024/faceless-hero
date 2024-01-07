import pygame as pg
from group import Group
from timer import Timer
from globals import *

AUTOSAVE_INTERVAL = 60 * 1000

class Scene:
    def __init__(self, screen: pg.Surface):
        self.screen = screen
        self.group = Group(screen)
        self.autosave = Timer(AUTOSAVE_INTERVAL, True, self.group.save)
        self.autosave.start()

    def update(self):
        self.group.update()
        self.autosave.update()

    def draw_bg(self):
        self.bg_images = []
        
        for i in range(3, -1, -1):
            self.bg_image = pg.image.load(f"assets/background/background paralax_{i}.png").convert_alpha()
            self.bg_image = pg.transform.scale(self.bg_image,(640, 480))
            self.bg_images.append(self.bg_image)
        
        self.bg_width = self.bg_images[0].get_width()

        for x in range(5):
            for i in self.bg_images:
                self.game.screen.blit(i, ((x * self.bg_width), 0))

    def exit(self):
        self.autosave.stop()
        self.group.save()
