# arena-sim-to-real:
Arena-sim-to-real is based on [arena-rosnav](https://github.com/ignc-research/arena-rosnav/tree/local_planner_subgoalmode), which is a flexible, high-performance 2D simulator for testing robotic navigation, and [pedsim_ros](https://github.com/srl-freiburg/pedsim_ros), which is a pedestrian simulator implementing the social force model. The agent is trained to learn an object-specific navigation behavior, keeping different safety distances towards different types of humans such as adults, children, and elders. An efficient DRL approach called CPU/GPU asynchronous A3C using curriculum learning is utilized. Within the simulation, it is assumed that the agent knows the accurate position and type of humans in the vicinity for understanding the interaction between the robot and humans. In real-world experiments, this information can be acquired using computer vision approaches.


 | <img src="https://github.com/ignc-research/arena-sim-to-real/blob/main/img/normal.gif"> |  
 |:-----------------------------------------------------: |
 |                            *normal*                             |
In addition to the normal task of navigating in a complex environment, auxiliary human guidance/following tasks have been introduced.


<img src="https://github.com/ignc-research/arena-sim-to-real/blob/644cd5c85fcf98a5cac00e661097f0c008118a29/img/guiding.gif"> | <img  src="https://github.com/ignc-research/arena-sim-to-real/blob/6db42521ed0a624e5c6b3df9297cf22c3ccb69ec/img/following_human.gif"> |
|:-----------------------------------------------------: |:-----------------------------------------------------: |
|                            *Guiding Human*                             |                            *Following Human*                             |



# Start Guide
We recommend starting with the [start guide](https://github.com/ignc-research/arena-sim-to-real/tree/main/docs/guide.md) which contains all information you need to know to start off with this project including installation on **Linux and Windows** as well as tutorials to start with. 


## 1. Installation
Please refer to [Installation.md](docs/Installation.md) for detailed explanations about the installation process.

## 2. Usage

### DRL Training

Please refer to [DRL-Training.md](docs/DRL-Training.md) for detailed explanations about agent, policy and training setups.

**DRL agents** are located in the [agents folder](https://github.com/ignc-research/arena-sim-to-real/tree/main/arena_navigation/arena_local_planner/learning_based/arena_local_planner_drl/agents).



##### Quick Start and Supplementary Notes

* In one terminnal, start simulation

```bash
workon the_name_of_your_virtual_env
roslaunch arena_bringup start_training.launch num_envs:=1 show_pedsim_labels:=true  republish_flatland_markers:=true 

```
* In another terminal, load the pretrained agent

```bash
workon the_name_of_your_virtual_env

roscd arena_local_planner_drl  &&  python scripts/training/train_agent.py --load name_of_pretrained_agent  --config rule_03     --n_envs 1

...



