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
        #print("b") 
        #try:
        raw=ser.readline().decode()
        posfr=int(raw[4:12])
        sfr=int(raw[17:23])
        posfl=int(raw[28:36])
        sfl=int(raw[41:47])
        posmr=int(raw[52:60])
        smr=int(raw[65:71])
        posml=int(raw[76:84])
        sml=int(raw[89:95])
        posrr=int(raw[100:108])
        srr=int(raw[113:119])
        posrl=int(raw[123:132])
        srl=int(raw[137:143])
        #print("a")
        #print(posml)
        vel_right = sfr*dist_per_count*4
        vel_left = sfl*dist_per_count*4
        speed= (vel_left + vel_right)/ 2.0
        v_th=(vel_right - vel_left)/ LenghtBetweenTwoWheels
        pub_encoder(speed, v_th)
        
        #except:
        #    pass
