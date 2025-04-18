# Auto_drone
Auto_Drone is a reinforcement learning-based drone navigation system built for intelligent path planning in simulated environments. Designed for rapid, efficient, and safe navigation, it learns optimal routes through continuous interaction with its environment. This repository is part of a 48-hour hackathon challenge.

---

## Features

- 🌍 Realistic drone simulation environment
- 🧠 RL model trained with **Stable-Baselines3 PPO**
- 🧭 Dynamic and optimized route planning
- 🤖 Supports inference and retraining
- 🔁 Self-learning and adaptive behavior
- 🎥 Video demo of route-finding in action

## About AirSim

In 2017 Microsoft Research created AirSim as a simulation platform for AI research and experimentation.

AirSim is a simulator for drones, cars and more, built on Unreal Engine. It is open-source, cross platform, and supports software-in-the-loop simulation with popular flight controllers such as PX4 & ArduPilot and hardware-in-loop with PX4 for physically and visually realistic simulations. It is developed as an Unreal plugin that can simply be dropped into any Unreal environment. Similarly, there is an experimental release for a Unity plugin.

AirSim as a platform can be used in AI research to experiment with deep learning, computer vision and reinforcement learning algorithms for autonomous vehicles. For this purpose, AirSim also exposes APIs to retrieve data and control vehicles in a platform independent way.

### How to use it
Navigate to your working directory and run
 `pip install airsim`
 
Clone the repo with `git clone https://github.com/microsoft/AirSim.git`

Note: Make sure you have Git Bash installed and user configured
#### Follow :
AirSim needs to be built, so it requires Visual Studio Build tools
1. Latest repo of AirSim reuire 2022 Visual Studio and community editor. Download the Visual Studio Build Installer and run it
2. Check Game development with C++, Desktop development with C/C++ and windows[version] SDK
3. Download and install
4. Open Visual 2022 Studio Communitty Edition and Open Developer command line from "Tools -> Developer Command Tools"
5. Navigate to the dierctory of cloned AirSim repo and run `build.cmd`

Note Make sure you have latest version of CMake installed

After this you will have your airsim packages set to be used

## Install Unreral Engine
Download Epic Gmaes, log in with your account.
Find Unreal Engine bar -> Library -> Install Engine

Choose version 4.27.7 to run this demonstration
Create a project

## Things to do before running the simulation
Navigate to Airsim [cloned repo] -> Unreal
Copy the plugins folder and paste it inside your Unreal project folder

Right click UProject starter and click 'Generate Visual Studio Build files' or something similar.

After this open your Unreal project go to World Settings -> GmaeMode -> Choose AirSimGameMode

Now run the project

You will see and drone on your game stage
You could use yopur own maps and environment as the game stage. You can download it from fab -> filer to free -> Select fab -> Add to library
!!Keywords for search: 'Urban City' 'Modular Cuty' 'Roads' 'City'
!!! Download fab that are compatible to your environment

## 📁 Repository Structure

<pre>Auto_drone/ 
  ├── drone_controller/
   |--rl-agent/
       |--trained_policy.zip
   |--utils/
       |--avoidance.py
       |--perception.py
       |--planner.py
   |--yolo_model
       |--yolov8n.pt
 |--control.py
 |--train_policy.py
</pre>

# About the work
This work uses Reinforcement learning ouylaying traing and trained policy utilization for route finding. This happens along with yolov8n model that is used for object detection to mitigate collision amd aid path planning.

## Clone this repo by running
``` git clone https://github.com/GauravVRich/Auto_drone.git```

## Install dependencies
Run ```pip intsall -r requirements.txt```

## Generate trained RL policy
To train the RL policy -run:
```Python train_policy.py```
The output training_policy gets stored as zip file in rl_agent/trained_policy.zip

### To note
The training and inference programs does not happen hand in hand but not limited to. When the inference happens trained_policy.zip is used and not trained along with. However this can be done by modifying the code in train.py and control.py

In process overview:
The trained_policy.zip gets updated alongside the control.py. The collision, last_action, distance to goal are considered for the updating the reward system

## Inference
Make sure the unreal project is running before executing control.py

Run ```python control.py```

Observe the drone reacing its goal coordinagtes in Unreal Engine. Try changing the goal; points to observe drone behaviour and for training the policy

# Demo video
Find the video in this drive link
https://docs.google.com/forms/d/e/1FAIpQLSclf67SIssWY9UN0mBJ3nDnoKFcOEIkp8i8ZWJ7CjZxRT2EoA/viewform?usp=sharing

# THANK YOU!
