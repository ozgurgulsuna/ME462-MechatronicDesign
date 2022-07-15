#!/usr/bin/env python
# Importing Libraries

from sensor_msgs.msg import LaserScan
import cv2
import numpy as np
import time
import rospy
import os
from geometry_msgs.msg import Twist
from multiprocessing import Process, Queue
from concurrent.futures import ThreadPoolExecutor

area_threshold, mid_x_axis = 60000, 320


scan = 5


cv2.namedWindow("Bos pencere")


def nothing(x):
    pass
    



def callback_velocity(msg, q):
    move_cmd = Twist()
    x = float(q.get())
    #print(x)
    if x < 0.3:
        move_cmd.linear.x = 0.0
    else:
        move_cmd.linear.x = msg.linear.x
    move_cmd.angular.z = msg.angular.z
    pub.publish(move_cmd)
        
 
    
def velocity(q):

    rospy.init_node('velocity', anonymous=True)

    rospy.Subscriber("aruco_2", Twist, callback_velocity, callback_args = q)
    pub = rospy.Publisher('aruco', Twist, queue_size=10)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


def callback_measure(msg, q):
    global scan
    scan = msg.ranges
    print(min(scan))
    try:
        q.get_nowait()
    except:
        pass
    print("231")
    q.put(min(list(scan)))



    
def measure(q):


    rospy.init_node('measure', anonymous=True)

    rospy.Subscriber("scan", LaserScan, callback_measure, callback_args = q)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    q = Queue()
    try:

        th_measure = Process(target = measure, args = (q,))
        th_measure.start()
        velocity(q)


    except rospy.ROSInterruptException:
        pass









