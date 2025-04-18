import numpy as np
from stable_baselines3 import PPO

# Load once
policy = PPO.load(r"rl_agent\trained_policy.zip")

def decide_next_action(detections, direction_hint):
    # You can simplify with rules, or use the RL model:
    obs = create_observation(detections, direction_hint)
    action, _ = policy.predict(obs)
    action_id = int(action) if not isinstance(action, int) else action
    return decode_action(action_id)

def create_observation(detections, hint):
    # Example: one-hot detections + safe dir encoded
    obs = np.zeros(10)
    for name, _ in detections:
        if name == "building":
            obs[0] = 1
        elif name == "tree":
            obs[1] = 1
        elif name == "road":
            obs[2] = 1
    obs[3:6] = hint
    return obs

def decode_action(action_id):
    if isinstance(action_id, np.ndarray):
        action_id = int(action_id.item())

    actions = {
        0: (1, 0, 0),   # Forward
        1: (0, 1, 0),   # Right
        2: (0, -1, 0),  # Left
        3: (0, 0, -1),  # Up
        4: (0, 0, 1),   # Down
        5: (-1, 0, 0)   # Backward
    }
    return actions.get(action_id, (0, 0, 0))

