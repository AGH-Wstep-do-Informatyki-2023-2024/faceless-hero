import pygame as pg
from typing import Callable, Optional


class Timer:
    def __init__(
        self, duration: int, func: Optional[Callable] = None, repeated: bool = False
    ):
        self.duration = duration
        self.func = func
        self.repeated = repeated
        self.stop()

    def start(self):
        self.start_time = pg.time.get_ticks()
        self.is_running = True

    def stop(self):
        self.start_time = 0
        self.is_running = False

    def update(self):
        if pg.time.get_ticks() - self.start_time >= self.duration and self.is_running:
            if self.func and self.start_time != 0:
                self.func()
            self.stop()
            if self.repeated:
                self.start()
