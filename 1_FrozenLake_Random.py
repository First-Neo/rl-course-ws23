import gymnasium as gym
import random

env = gym.make("FrozenLake-v1", is_slippery=False, render_mode="ansi")

random.seed(0)

print("## Frozen Lake ##")

action2string = {0: "Left", 1: "Down", 2: "Right", 3: "Up"}

episode_done = False
goal_found = False
state = env.reset(seed=0)

counter = 0

print("Start state:")
print(env.render())
while not goal_found:
    counter = counter + 1
    while not episode_done:
        action = random.randint(0, 3)  # choose a random action
        state, reward, episode_done, _, _ = env.step(action)
        print(f"\nAction:{action2string[action]}, new state:{state}, reward:{reward}")
        print(env.render())

    if(reward > 0):
        goal_found = True
    else:
        episode_done = False
        state = env.reset(seed=0)
        print("Start state:")
        print(env.render())

print("Found Solution: ", counter)