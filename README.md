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

* Code (Publisher): [link]()
* Code (Subscriber): [link]()
* CMakeLists.txt: [link]()
* package.xml: [link]()

### Requirements

The code works with the requirements below.

  * Ubuntu 18.04
  * ROS
  
### Build

1. First of all, clone this repository with the following command.

		$ git clone https://github.com/TanapolHongsuwan/ROS_project.git
       
		$ cd ROS_project

2. In a new terminal, perform
		
		$ roscore
		
3. Perform '$ catkin_make'

		$ cd ..
		
		$ cd catkin_make
       
4. Move to the scripts file, make, install modules, and change permissions

		$ cd src/project2/
		
5. Set the permission

		$ sudo chmod u+x topic_publisher.py
		
		$ sudo chmod u+x topic_subscriber.py
  
### Run

  
## About the Project

This is my first project using ROS (ROS1) recorded sound based on Prof. Ryuichi Ueda's template code, learning about Publisher and Subscriber on Ubuntu. Hopefully, the template would be useful somehow in a next ROS project in the future.

## Preference

[Robot System's lecture 10 (Japanese)](https://ryuichiueda.github.io/robosys2020/lesson10_ros.html#/)

## License

[GNU General Public License v3.0]()
