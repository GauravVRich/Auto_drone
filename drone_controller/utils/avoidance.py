def avoid_obstacles(depth_response, detections):
    import numpy as np

    if depth_response is None:
        print("[WARN] Depth response is None.")
        return (1, 0, 0)

    # Extract float array
    depth_buffer = depth_response.image_data_float

    if not depth_buffer or len(depth_buffer) == 0:
        print("[WARN] Depth buffer is empty.")
        return (1, 0, 0)

    depth_array = np.array(depth_buffer, dtype=np.float32)

    # Match this to your settings.json config!
    expected_shape = (144, 256)
    if depth_array.size != expected_shape[0] * expected_shape[1]:
        print(f"[ERROR] Unexpected depth size: {depth_array.size}")
        return (1, 0, 0)

    depth_img = depth_array.reshape(expected_shape)

    # Basic obstacle logic
    if np.min(depth_img) < 3.0:
        return (0, 1, 0)  # Move right
    else:
        return (1, 0, 0)  # Forward
