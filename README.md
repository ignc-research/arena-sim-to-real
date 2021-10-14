# arena-sim-to-real:
This repository contains the code for the paper [Enhancing Navigational Safety in Crowded Environments using
Semantic-Deep-Reinforcement-Learning-based Navigation](https://arxiv.org/pdf/2109.11288.pdf).

arena-sim-to-real is based on [arena-rosnav](https://github.com/ignc-research/arena-rosnav/tree/local_planner_subgoalmode), which is a flexible, high-performance 2D simulator for testing robotic navigation, and [pedsim_ros](https://github.com/srl-freiburg/pedsim_ros), which is a pedestrian simulator implementing the social force model. The agent is trained to learn an object-specific navigation behavior, keeping different safety distances towards different types of humans such as adults, children, and elders. An efficient DRL approach called CPU/GPU asynchronous A3C using curriculum learning is utilized. Within the simulation, it is assumed that the agent knows the accurate position and type of humans in the vicinity for understanding the interaction between the robot and humans. In real-world experiments, this information can be acquired using computer vision approaches.


 <img src="https://github.com/ignc-research/arena-sim-to-real/blob/main/img/normal.gif">  
In addition to the normal task of navigating in a complex environment, auxiliary human guidance/following tasks have been introduced.
<img src="https://github.com/ignc-research/arena-sim-to-real/blob/644cd5c85fcf98a5cac00e661097f0c008118a29/img/guiding.gif"> <img  src="https://github.com/ignc-research/arena-sim-to-real/blob/6db42521ed0a624e5c6b3df9297cf22c3ccb69ec/img/following_human.gif"> 

