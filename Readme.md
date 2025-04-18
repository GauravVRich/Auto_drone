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

## 📁 Repository Structure

<pre>Auto_drone/ 
  ├── models/
  │ └── trained_policy.zip # Pretrained PPO policy 
  ├── scripts/
  │   ├── train.py # RL training script 
  │ └── infer.py # Inference using trained model 
  ├── env/ 
  │ └── drone_env.py # Custom drone environment 
  ├── utils/ 
  │ └── helpers.py # Utility functions
  ├── results/ 
  │ ├── simulation_gif.gif # Test run snapshots / simulation GIF 
  │ └── logs/ # Training logs ├── demo/ 
  │ └── demo_video.mp4 # Route finding demo video 
  ├── README.md # You're here 
  └── requirements.txt # Python dependencies</pre>

