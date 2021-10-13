# arena-sim-to-real:
This repository contains the code for the paper [Enhancing Navigational Safety in Crowded Environments using
Semantic-Deep-Reinforcement-Learning-based Navigation](https://arxiv.org/pdf/2109.11288.pdf).

arena-sim-to-real is based on [arena-rosnav](https://github.com/ignc-research/arena-rosnav/tree/local_planner_subgoalmode), which is a flexible, high-performance 2D simulator for testing robotic navigation, and [pedsim_ros](https://github.com/srl-freiburg/pedsim_ros), which is a pedestrian simulator implementing the social force model. The agent is trained to learn an object-specific navigation behavior, keeping different safety distances towards different types of humans such as adults, children, and elders. An efficient DRL approach called CPU/GPU asynchronous A3C using curriculum learning is utilized. Within the simulation, it is assumed that the agent knows the accurate position and type of humans in the vicinity for understanding the interaction between the robot and humans. In real-world experiments, this information can be acquired using computer vision approaches.


| <img width="250" height="200" src="https://github.com/ignc-research/arena-sim-to-real/tree/main/img/normal.gif"> | <img width="250" height="200" src="https://github.com/ignc-research/arena-sim-to-real/tree/main/img/guidig.gif"> | <img width="250" height="200" src="hhttps://github.com/ignc-research/arena-sim-to-real/tree/main/img/following.gif"> |

