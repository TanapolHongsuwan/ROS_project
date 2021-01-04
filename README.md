# ROS Recorder

## About / Synopsis

* This project is for recording sound in Linux platform using array in Python.
* Project status: Completed

Youtube video: [link]()

## Table of contents

* [Title](#ros-recorder)
  * [About / Synopsis](#about--synopsis)
  * [Code](#code)
    * [Requirements](#requirements)
    * [Build](#build)
    * [Run](#run)
  * [About the Project](#about-the-project)
  * [Preference](#preference)
  * [License](#license)
  
## Code

* Code (Publisher): [link](https://github.com/TanapolHongsuwan/ROS_recorder/blob/main/topic_publisher.py)
* Code (Subscriber): [link](https://github.com/TanapolHongsuwan/ROS_recorder/blob/main/topic_subscriber.py)
* CMakeLists.txt: [link](https://github.com/TanapolHongsuwan/ROS_recorder/blob/main/CMakeLists.txt)
* package.xml: [link](https://github.com/TanapolHongsuwan/ROS_recorder/blob/main/package.xml)

### Requirements

#### Environment

  * Ubuntu 18.04
  * ROS
  
#### Pakages Installation

  * Python pip 
  
  		$ apt install python-pip
  
  * sounddevice lib
  
  		$ sudo apt-get install libportaudio2
  		
		$ sudo apt-get install libasound-dev
		    
  * spicy
  		
		$ sudo apt-get install python-scipy
  
  		$ pip install scipy
  
### Build

1. First of all, clone this repository with the following command.

		$ git clone https://github.com/TanapolHongsuwan/ROS_recorder.git
       
		$ cd ROS_recorder

2. In a new terminal, perform
		
		$ roscore
		
3. Perform '$ catkin_make'

		$ cd ..
		
		$ cd catkin_make
       
4. Move to the project2 file, make, install modules, and change permissions

		$ cd src/project2/
		
5. Set the permission

		$ sudo chmod u+x topic_publisher.py
		
		$ sudo chmod u+x topic_subscriber.py
  
### Run

<img src="![c2c69c5c9377fe00440802de0b949ccd](https://user-images.githubusercontent.com/67133469/103495842-00959100-4e34-11eb-90e0-7ccfd0039fb4.png)" width = "500">

1. Based on the video ([link]()), after we perform `$ roscore`, move to the project2 file and perform `$ rosrun project2 topic_subscriber.py` to stand by and receiving the signal from the publisher.

2. Perform `$ rosrun project2 topic_subscriber.py` to record audio. After recording audio, the publisher will publish a record to the subscriber.

3. After the subscriber received a message, it will play an audio as we recorded from the publisher.

## About the Project

This is my first project using ROS (ROS1) recorded sound based on Prof. Ryuichi Ueda's template code, learning about Publisher and Subscriber on Ubuntu. Hopefully, the template would be useful somehow in a next ROS project in the future.

## Preference

[Robot System's lecture 10 (Japanese)](https://ryuichiueda.github.io/robosys2020/lesson10_ros.html#/)

[Programming Robots with ROS: A Practical Introduction to the Robot Operating System, by Morgan Quigley, Brian Gerkey, William D. Smart](https://www.amazon.com/Programming-Robots-ROS-Practical-Introduction/dp/1449323898)

## License

[GNU General Public License v3.0](https://github.com/TanapolHongsuwan/ROS_recorder/blob/main/COPYING)
