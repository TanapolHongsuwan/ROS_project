# ROS Project

## About / Synopsis

* This project is for ??? in Linux platform using Python.
* Project status: processing

Youtube video: [link]()

## Table of contents

* [Title](#ros-project)
  * [About / Synopsis](#about--synopsis)
  * [Code](#code)
    * [Requirements](#requirements)
    * [Build](#build)
    * [Run](#run)
  * [About the Project](#about-the-project)
  * [Preference](#preference)
  * [License](#license)
  
## Code

* Code: [link]()
* CMakeLists.txt: [link]()

### Requirements

The code will works with the requirements below.

  * Ubuntu 20.04
  * ROS
  
### Build

1. First of all, clone this repository with the following command.

		$ git clone https://github.com/TanapolHongsuwan/ROS_project.git
       
		$ cd ROS_project
		
2. Perform '$ catkin_make'

		$ cd ..
		
		$ cd catkin_make
       
3. In a new terminal, perform
		
		$ roscore
       
4. Move to the ??? file, make, install modules, and change permissions

		$ cd src/ros_led/scripts/led
		
		$ bash setup.bash
		
5. Set the permission

		$ bash permission.bash
  
### Run

  
## About the Project

This is my first project using ROS (ROS1) with Raspberry Pi based on Prof. Ryuichi Ueda's template code, learning about Publisher and Subscriber on Ubuntu. Hopefully, the template would be useful somehow in a next ROS project in the future.

## Preference

[Robot System's lecture 10 (Japanese)](https://ryuichiueda.github.io/robosys2020/lesson10_ros.html#/)

## License

[GNU General Public License v3.0]()
