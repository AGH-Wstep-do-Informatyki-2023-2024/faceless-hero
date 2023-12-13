from interval import Interval
from group import Group
from globals import *


class Scene:
    def __init__(self, game):
        self.game = game
        self.entities = Group(AUTOSAVE_FILE)
        self.autosave = Interval(AUTOSAVE_INTERVAL, self.entities.save)

    def update(self):
        self.entities.update()

    def draw_bg(self):
        self.scroll = 0
        self.bg_images = []
        self.bg_width = self.bg_images[0].get_width()
        for i in range(0, 4):
            self.bg_image = self.game.pygame.image.load(f"assets/background parallax_{i}.png").convert_alpha()
            self.bg_images.append(self.bg_image)

        for x in range(5):
            for i in self.bg_images:
                self.game.screen.blit(i, ((x * self.bg_width) - self.scroll, 0))

    # def draw(self):
    #     self.game.screen.fill("crimson")
    #     self.entities.draw(self.game.screen)

    def exit(self):
        self.autosave.stop()
        self.entities.save()
