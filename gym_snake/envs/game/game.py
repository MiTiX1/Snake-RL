import pygame as pg
import numpy as np
import random
from dataclasses import dataclass, field
from typing import List
from .snake import Snake
from .food import Food


@dataclass
class GameInformation:
    snake_head_pos: field(default_factory=list)
    food_pos: List[int]
    score: int = 0
    is_over: bool = False


class SnakeGame:
    SCREEN_WIDTH = 200
    SCREEN_HEIGHT = 200
    BACKGROUND = (0, 0, 0)

    def __init__(self) -> None:
        self.screen = None
        self.x_range = SnakeGame.SCREEN_WIDTH // Snake.CELL_WIDTH - 1
        self.y_range = SnakeGame.SCREEN_HEIGHT // Snake.CELL_HEIGHT - 1
        self.snake = Snake([
            self.x_range // 2 + 1,
            self.y_range // 2 + 1
        ])
        self.food = Food(self._get_food_random_pos())
        self.game_information = GameInformation(
            snake_head_pos=self.snake.get_head(),
            food_pos=self.food.pos
        )

    def _get_food_random_pos(self) -> List[int]:
        x = random.randint(0, self.x_range)
        y = random.randint(0, self.y_range)

        while [x, y] in self.snake.snake_parts:
            x = random.randint(0, self.x_range)
            y = random.randint(0, self.y_range)

        return [x, y]

    def _eat(self):
        return self.snake.get_head() == self.food.pos

    def render(self, screen) -> None:
        screen.fill(SnakeGame.BACKGROUND)
        self.snake.render(screen)
        self.food.render(screen)

    def _collision(self) -> bool:
        head = self.snake.get_head()
        if head[0] < 0 or head[0] > self.x_range or head[1] < 0 or head[1] > self.y_range:
            return True

        if head in self.snake.get_body():
            return True
        return False

    def test_snake(self) -> GameInformation:
        just_eaten = self._eat()
        keys = pg.key.get_pressed() 
        if keys[pg.K_w]:
            self.snake.update(new_direction=Snake.UP, just_eaten=just_eaten)
        elif keys[pg.K_d]:
            self.snake.update(new_direction=Snake.RIGHT, just_eaten=just_eaten)
        elif keys[pg.K_s]:
            self.snake.update(new_direction=Snake.DOWN, just_eaten=just_eaten)
        elif keys[pg.K_a]:
            self.snake.update(new_direction=Snake.LEFT, just_eaten=just_eaten)
        else:
            self.snake.update(just_eaten=just_eaten)

        if just_eaten:
            self.food.update(self._get_food_random_pos())
            self.game_information.score += 1
            self.game_information.food_pos = self.food.pos
        self.game_information.snake_head_pos = self.snake.get_head()
        self.game_information.is_over = self._collision()

        return self.game_information
        
    def update(self, direction: int) -> GameInformation:
        just_eaten=self._eat()
        self.snake.update(new_direction=direction, just_eaten=just_eaten)

        if just_eaten:
            self.food.update(self._get_food_random_pos())
            self.game_information.score += 1
            self.game_information.food_pos = self.food.pos
        self.game_information.snake_head_pos = self.snake.get_head()
        self.game_information.is_over = self._collision()

        return self.game_information

    def reset(self) -> None:
        self.snake.reset()
        self.food.reset(self._get_food_random_pos())
        self.game_information = GameInformation(
            snake_head_pos=self.snake.get_head(),
            food_pos=self.food.pos
        )
    
    def close(self) -> None:
        pg.display.quit()
        pg.quit()
