#!/usr/bin/env python
import sounddevice as sd #Importing the sounddevice library and others
import numpy as np
import scipy.io.wavfile as wav
import rospy

from std_msgs.msg import Float32


fs=44100 #Frecuency of the sound
duration = 5  # seconds



rospy.init_node('topic_publisher') #Name of the topic
pub = rospy.Publisher('voice', Float32, queue_size=100)
rate = rospy.Rate(0.2) #Hz

flag=0
listtosend=[] #IList that will store the data that will be sent


while not rospy.is_shutdown():
	if flag == 0: #Using a flag so the program will just run once
		print "Waiting for 5 secs"
		rate.sleep() #Waits the rate specified above
		myrecording = sd.rec(duration * fs, samplerate=fs, channels=1,dtype='float32')#Function that records the sound of the default recording device for the amount specified above
		print "Recording Audio"
		sd.wait() #Waits for the audio to be recorded

		list1=myrecording.tolist() #The recording data is a numpy array, so I converted it to a list to be sent by the ros publisher
		
		for i in range(len(list1)): #The list I got from the numpy array is a list of lists, with format: list[[],[],...,[]] so I used an auxiliary variable to get the information on the inside list, and send raw data to the subscriber
			aux=list1[i]
			listtosend.append(aux[0]) #This is the list with raw data to collected from the original numpy array, this is the information I will publish

		print "Audio recording complete , Publishing..."
		for i in range(len(listtosend)): 
			pub.publish(listtosend[i]) #This line publishes ("Sends") the raw data one by one of the list
		pub.publish(123) #This is just a control number, it means that the list has finished, when the subscriber receives this number, it will know when to play the audio recorded
		flag = 1 #It runs only one time
		rate.sleep()

