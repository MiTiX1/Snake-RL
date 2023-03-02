# Snake RL

## Environment

This is a basic Snake game made as an OpenAI Gym environment.
The snake evolves in a 20x20 grid, and always starts in the center of the grid with a size of 1 cell.

**Observation space**
- the coordinates of the snake's head
- the coordinates of the apple
- the euclidean distance between the snake's head and the apple

**Rewards**
- +1 if the snake eats the apple
- +0.1 if the snake gets closer to the apple
- -0.1 if the snake gets further from the apple
- -1 if the snake dies

## Installation

1. Clone the repository
```sh
git clone https://github.com/MiTiX1/Snake-RL.git
```
2. Install the dependencies
```sh
pip install -r requirements.txt
```

## Create an environment

```python
import gym

env = gym.make("gym_snake:gym_snake/Snake-v0")
```

## References

- [Gym documentation](https://www.gymlibrary.dev/)
- [Stable baselines 3 documentation](https://stable-baselines3.readthedocs.io/en/master/)
- [PPO paper](https://arxiv.org/abs/1707.06347)
- [A2C paper](https://arxiv.org/abs/1602.01783v2)