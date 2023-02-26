import pygame as pg
import random
from typing import List


class Snake:
    HEAD_COLOR = (0, 184, 148)
    BODY_COLOR = (85, 239, 196)
    CELL_WIDTH = 5
    CELL_HEIGHT = 5
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

    def __init__(self, pos: List[int]) -> None:
        # direction up (0) / right (1) / down (2) / left (3)
        self.direction = random.randint(0, 3)
        self.snake_parts = [pos]
        self.original_pos = pos.copy()

    def get_head(self) -> List[int]:
        return self.snake_parts[-1]
    
    def get_body(self) -> List[List[int]]:
        return self.snake_parts[:-1]

    def update(self, new_direction: int = None, just_eaten: bool = False) -> None:
        new_head = self.get_head().copy()
        self.direction = new_direction if new_direction is not None else self.direction

        if self.direction == Snake.UP:
            new_head[1] -= 1
        elif self.direction == Snake.RIGHT:
            new_head[0] += 1
        elif self.direction == Snake.DOWN:
            new_head[1] += 1
        elif self.direction == Snake.LEFT:
            new_head[0] -= 1
        
        if not just_eaten:
            self.snake_parts.pop(0)

        self.snake_parts.append(new_head)

    def render(self, screen: pg.Surface) -> None:
        for part in self.snake_parts[:-1]:
            pg.draw.rect(screen, Snake.BODY_COLOR, [part[0] * Snake.CELL_WIDTH, part[1] * Snake.CELL_HEIGHT, Snake.CELL_WIDTH, Snake.CELL_HEIGHT])

        head = self.get_head()
        pg.draw.rect(screen, Snake.HEAD_COLOR, [head[0] * Snake.CELL_WIDTH, head[1] * Snake.CELL_HEIGHT, Snake.CELL_WIDTH, Snake.CELL_HEIGHT])

    def reset(self):
        self.snake_parts = [self.original_pos.copy()]