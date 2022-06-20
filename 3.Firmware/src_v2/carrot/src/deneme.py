#!/usr/bin/env python
# Importing Libraries

import cv2
import numpy as np
import time
import rospy
import os
from geometry_msgs.msg import Twist

def pub_commands(lin, ang):
    print('inside pub')
    # Create a publisher which can "talk" to Turtlesim and tell it to move
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rospy.init_node('pub_commands', anonymous=True)
    rate = rospy.Rate(2)
     
    # Create a Twist message and add linear x and angular z values
    move_cmd = Twist()
    move_cmd.linear.x = lin
    move_cmd.angular.z = ang
    print(5**2)
    
    pub.publish(move_cmd)
    rate.sleep()





    
if __name__ == '__main__':
    while True:
        try:
            print('starting')
            pub_commands(50.0, 25.0)
            
        except rospy.ROSInterruptException:
            print('except')
            pass
