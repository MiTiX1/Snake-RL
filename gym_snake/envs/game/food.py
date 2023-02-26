import pygame as pg
from typing import List


class Food:
    COLOR = (255, 0, 0)
    WIDTH = 5
    HEIGHT = 5

    def __init__(self, pos: List[int]) -> None:
        self.pos = pos

    def update(self, new_pos: List[int]) -> None:
        self.pos = new_pos

    def render(self, screen: pg.Surface) -> None:
        pg.draw.rect(screen, Food.COLOR, [self.pos[0] * Food.WIDTH, self.pos[1] * Food.HEIGHT, Food.WIDTH, Food.HEIGHT])

    def reset(self, pos: List[int]) -> None:
        self.pos = pos