# drone_controller/train_policy.py

import gym
import numpy as np
import airsim
import time
import os
from stable_baselines3 import PPO
from stable_baselines3.common.env_checker import check_env

class AirSimDroneEnv(gym.Env):
    def __init__(self):
        super().__init__()
        self.last_action = 0  # Initialize
        # Connect to AirSim
        self.client = airsim.MultirotorClient()
        self.client.confirmConnection()
        self.client.enableApiControl(True)
        self.client.armDisarm(True)
        self.client.takeoffAsync().join()
        
        self.action_space = gym.spaces.Discrete(5)  # forward, left, right, ascend, descend
        self.observation_space = gym.spaces.Box(low=0, high=1, shape=(10,), dtype=np.float32)

    def reset(self):
        self.client.reset()
        time.sleep(0.5)
        self.client.enableApiControl(True)
        self.client.armDisarm(True)
        self.client.takeoffAsync().join()
        return self._get_obs()

    def _get_obs(self):
        return np.random.rand(10).astype(np.float32)

    def step(self, action):
        self.last_action = action  # Track for reward
        vx, vy, vz = self._action_to_velocity(action)
        self.client.moveByVelocityAsync(vx, vy, vz, duration=0.5).join()

        reward = self._compute_reward()
        obs = self._get_obs()
        done = False  # You can set this to True if collided, for better training
        info = {}

        return obs, reward, done, info

    def _action_to_velocity(self, action):
        if action == 0: return (1, 0, 0)   # forward
        if action == 1: return (0, 1, 0)   # right
        if action == 2: return (0, -1, 0)  # left
        if action == 3: return (0, 0, -1)  # descend
        if action == 4: return (0, 0, 1)   # ascend

    def _compute_reward(self):
        reward = 0.0

        # --- 1. Reward for forward movement ---
        if self.last_action == 0:
            reward += 1.0

        # --- 2. Small reward for any movement ---
        reward += 0.1

        # --- 3. Collision penalty ---
        collision_info = self.client.simGetCollisionInfo()
        if collision_info.has_collided:
            reward -= 5.0

        # --- 4. Slight penalty for zig-zagging ---
        if self.last_action in [1, 2, 3, 4]:
            reward -= 0.2

        # --- 5. Distance to target (goal position) ---
        # Set your goal here (e.g., end of road or safe zone)
        goal_pos = airsim.Vector3r(50, 0, -10)  # ← you can update this
        drone_pos = self.client.getMultirotorState().kinematics_estimated.position

        dist_to_goal = np.linalg.norm(np.array([drone_pos.x_val, drone_pos.y_val, drone_pos.z_val]) -
                                    np.array([goal_pos.x_val, goal_pos.y_val, goal_pos.z_val]))

        # The closer we are, the better (scaled inverse)
        reward += max(0, 10 - dist_to_goal) * 0.1

        # --- 6. Bonus for reaching the goal ---
        if dist_to_goal < 2.0:
            reward += 10.0  # reached goal!

        # --- 7. Placeholder: reward for being over a road ---
        # Example: Add small reward if the observation detects road ahead (dummy for now)
        obs = self._get_obs()
        if obs[0] > 0.5:  # Assuming obs[0] = confidence of "road" ahead
            reward += 0.5

        # --- 8. Placeholder: obstacle avoidance reward ---
        # If obs[1] = tree/building proximity detection (dummy)
        if obs[1] > 0.7:  # high value = obstacle very near
            reward -= 0.5  # penalize getting close

        return reward
# check_env(AirSimDroneEnv())

env = AirSimDroneEnv()

model = PPO("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=10000)  # increase for better performance

os.makedirs("rl_agent", exist_ok=True)
model.save("rl_agent/trained_policy.zip")

print("✅ Policy trained and saved to rl_agent/trained_policy.zip")
