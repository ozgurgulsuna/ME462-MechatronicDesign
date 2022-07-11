#!/usr/bin/env python
# Importing Libraries

import numpy as np
import time
import rospy
import os
from geometry_msgs.msg import Twist
import serial

LenghtBetweenTwoWheels=.2
dist_per_count = 0.0075

ser = serial.Serial(
    port='/dev/ttyACM0',
    baudrate=115200,
    parity=serial.PARITY_ODD,
    stopbits=serial.STOPBITS_TWO,
    bytesize=serial.SEVENBITS
)


def pub_encoder(speed, rotation):
    # Create a publisher which can "talk" to Turtlesim and tell it to move
    pub = rospy.Publisher('/encoder', Twist, queue_size=10)
    rospy.init_node('pub_encoder', anonymous=True)
    rate = rospy.Rate(10)
     
    # Create a Twist message and add linear x and angular z values
    move_cmd = Twist()
    move_cmd.linear.x = speed
    move_cmd.angular.z = rotation
    
    
    pub.publish(move_cmd)
    rate.sleep()
    


while 1:
    
    try:
        raw=ser.readline().decode()
        pos1=int(raw[10:18])
        diff1=int(raw[26:32])
        pos2=int(raw[44:52])
        diff2=int(raw[60:66])
        #print(diff2)
        vel_right = diff1*dist_per_count*10
        vel_left = diff2*dist_per_count*10
        speed= (vel_left + vel_right)/ 2.0
        v_th=(vel_right - vel_left)/ LenghtBetweenTwoWheels
        pub_encoder(speed, v_th)
        
    except:
        pass
