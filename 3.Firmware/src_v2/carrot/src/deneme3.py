#!/usr/bin/env python
# Importing Libraries
from multiprocessing import Process, Queue
from sensor_msgs.msg import LaserScan
import cv2
import numpy as np
import time
import rospy
import os
from geometry_msgs.msg import Twist

scan = 1.0

def callback_measure(msg):
    global scan
    scan = msg.ranges
    print(min(list(scan)))



    
def measure(q):


    rospy.init_node('measure', anonymous=True)

    rospy.Subscriber("scan", LaserScan, callback_measure)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    q = Queue()
    th_measure = Process(target = measure, args = (q,))
    th_measure.start()
