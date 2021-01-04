#!/usr/bin/env python
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import rospy
from std_msgs.msg import Float32

fs=44100 #This is the frecuency the sound will be played

list1=[] #List on which I will collect all the data received by the subscriber


def callback(msg): #This is the callback, it will enter this function everytime the subscriber receives information
	if msg.data != 123: #Other number different than the control number 123 will be received and stored in a list
		list1.append([msg.data])
		

		
	if msg.data == 123: #When the subscriber receives the control number it will play the audio recorded

		playrecording=np.array(list1) #The list is transformed into a numpy array again, so the library sounddevice will know how to play it
		print "Message received, playing audio..."
		sd.play(playrecording, fs) #Plays the audio recorded
		sd.wait() #Waits for the audio to be played
		print "Play Audio Complete"

rospy.init_node('topic_subscriber') #Initializes the node
sub = rospy.Subscriber('voice', Float32, callback)
rospy.spin()
