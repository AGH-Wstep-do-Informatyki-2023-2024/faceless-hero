import pygame as pg
import sys
from singleton import Singleton
from scene import Scene
from globals import *


class FacelessHero(metaclass=Singleton):
    def __init__(self):
        self.pygame_init()
        self.screen = pg.display.set_mode(WINDOW_SIZE)
        self.clock = pg.time.Clock()
        self.scene = Scene(self.screen)
        self.is_running = True

    @staticmethod
    def pygame_init():
        pg.init()
        pg.display.set_caption("Faceless Hero")
        pg.mixer.init()
        # pg.font.Font() # TODO obsługa fontów

    def main(self, debug=False):
        pg.mixer.music.load("assets/sounds/music/Yakov Golman - Japan.mp3")
        pg.mixer.music.play(-1)
        while self.is_running:
            self.handle_event()
            self.update()
            self.draw()

    def handle_event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_q:
                    self.exit()

    def update(self):
        pg.display.update()
        self.scene.update()
        self.clock.tick(FPS)

    def draw(self):
        self.scene.draw()

    def exit(self):
        self.scene.exit()
        pg.quit()
        try:
            sys.exit()
        finally:
            self.is_running = False
