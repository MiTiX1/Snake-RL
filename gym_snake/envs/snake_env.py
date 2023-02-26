import gym
import numpy as np
import pygame as pg

from gym.spaces import Discrete, Box, Dict
from .game import SnakeGame

class SnakeEnv(gym.Env):
    def __init__(self):
        super().__init__()
        self.game = SnakeGame()
        self.action_space = Discrete(4)
        self.observation_space = Dict({
            "snake_head": Box(low=0, high=40, shape=(2,), dtype=int),
            "food": Box(low=0, high=40, shape=(2,), dtype=int),
            "distance": Box(
                low=0, 
                high=self._euclidean_distance(
                    np.array([0, 0]), 
                    np.array([self.game.x_range, self.game.y_range])
                ), 
                shape=(1,), 
                dtype=float
            )
        })
        self.state = self._get_state()
        self.score = 0
        self.distance = self._euclidean_distance(
            np.array(self.game.food.pos), 
            np.array(self.game.snake.get_head())
        )
        self.screen = None
        self.clock = pg.time.Clock()
        
    def _euclidean_distance(self, x1, x2):
        return np.array([np.sqrt(np.sum((x1 - x2)**2))])
        
    def _get_state(self):
        snake_head = np.array(self.game.snake.get_head())
        food = np.array(self.game.food.pos)
        return {
            "snake_head": snake_head,
            "food": food,
            "distance": self._euclidean_distance(food, snake_head)
        }
    
    def step(self, action):
        info = self.game.update(action).__dict__.copy()
        done = info["is_over"]
        reward = 0
        self.state = self._get_state()
        
        if done:
            reward = -1
        elif self.score < info["score"]:
            reward = 1
            self.score = info["score"]
        elif self.state["distance"] < self.distance:
            reward = 0.1
        elif self.state["distance"] > self.distance:
            reward = -0.1
            
        self.distance =  self.state["distance"]
        
        return self.state, reward, done, info
    
    def reset(self):
        self.game.reset()
        self.score = 0
        self.state = self._get_state()
        self.distance = self.state["distance"]
        self.screen = None
        return self.state
    
    def render(self, mode = "human"):
        if mode == "human":
            if self.screen is None:
                self.screen = pg.display.set_mode((SnakeGame.SCREEN_WIDTH, SnakeGame.SCREEN_HEIGHT))
            self.clock.tick(15)
            self.game.render(self.screen)
            pg.display.update()
        
    def close(self):
        if self.screen is not None:
            pg.display.quit()
            pg.quit()
