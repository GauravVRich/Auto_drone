import airsim
import time
import numpy as np
from utils.perception import detect_objects
from utils.avoidance import avoid_obstacles
from utils.planner import decide_next_action

# Goal coordinates
goal_pos = np.array([93.37, 0.79, -7.56])
start_pos = np.array([0, 0, -7.5])

client = airsim.MultirotorClient()
client.confirmConnection()
client.enableApiControl(True)
client.armDisarm(True)

# Takeoff (may already be in air if we set z)
client.takeoffAsync().join()
print("[INFO] Drone initialized and airborne at starting position.")
time.sleep(2)

# Set start position
client.simSetVehiclePose(airsim.Pose(airsim.Vector3r(*start_pos), airsim.to_quaternion(0, 0, 0)), True)
time.sleep(1)

# Define normalized direction vector towards goal
direction = goal_pos - start_pos
norm_dir = direction / np.linalg.norm(direction)

# Scale velocity only in X and Y, keep Z constant
vx = norm_dir[0] * 5.0   # or whatever speed you want in X
vy = norm_dir[1] * 5.0   # or whatever speed you want in Y
vz = -0.5 

while True:
    print(client.simListSceneObjects("Camera*"))
    # Step 1: Get camera image
    responses = client.simGetImages([
        airsim.ImageRequest("front_center", airsim.ImageType.Scene, False, False)
    ])
    img = responses[0].image_data_uint8

    # Step 2: Detect objects
    detections = detect_objects(img)

    # Step 3: Get depth data
    responses = client.simGetImages([
    airsim.ImageRequest("front_center", airsim.ImageType.DepthPerspective, pixels_as_float=True, compress=False)
    ])
    depth = responses[0]

    # Step 4: Avoid obstacles
    safe_direction = avoid_obstacles(depth, detections)

    # Step 5: Route planning (ML or logic-based)
    action = decide_next_action(detections, safe_direction)

    # Optional: override action with base path to goal
    # You can blend logic with RL action output here
    if (
        action is None or
        not isinstance(action, (list, tuple, np.ndarray)) or
        len(action) != 3 or
        not all(np.isfinite(action))
    ):
        vx_override, vy_override, vz_override = vx, vy, vz  # fallback
    else:
        vx_override, vy_override, vz_override = action
    # Step 6: Move the drone
    client.moveByVelocityAsync(
        vx=vx_override, vy=vy_override, vz=vz_override, duration=0.5
    ).join()

    # Check distance to goal
    pos = client.getMultirotorState().kinematics_estimated.position
    current_pos = np.array([pos.x_val, pos.y_val, pos.z_val])
    distance_to_goal = np.linalg.norm(goal_pos - current_pos)

    if distance_to_goal < 5.0:
        print("[INFO] Goal reached 🎯")
        break

    time.sleep(0.1)


#Drone: -190.0 -170.0 102.000687 [-852.509521, -215.003784, 53.554955]
#Goal: -13218.744141  -971.172607  -2.298691