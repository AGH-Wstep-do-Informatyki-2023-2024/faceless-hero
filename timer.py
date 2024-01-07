from pygame.time import get_ticks
from typing import Callable


class Timer:
    def __init__(
        self, duration: int, repeated: bool = False, func: Callable | None = None
    ):
        self.duration = duration
        self.repeated = repeated
        self.func = func
        self.stop()

    def start(self):
        self.start_time = get_ticks()
        self.is_running = True

    def stop(self):
        self.start_time = 0
        self.is_running = False

    def update(self):
        if get_ticks() - self.start_time >= self.duration and self.is_running:
            if self.func and self.start_time != 0:
                self.func()
            self.stop()
            if self.repeated:
                self.start()
