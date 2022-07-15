#!/usr/bin/env python3
# Importing Libraries

from sensor_msgs.msg import LaserScan
import cv2
import numpy as np
import time
import rospy
import os
from geometry_msgs.msg import Twist
import cv2.aruco as aruco
from std_msgs.msg import String,Float32,Float32MultiArray
from rospy_tutorials.msg import Floats
from rospy.numpy_msg import numpy_msg


area_threshold, mid_x_axis = 60000, 320


scan = 5




def callback(data):
  
  
  cv_image_array = data.data
  print(cv_image_array.shape)
  #print(type(cv_image_array))
  #cv_image_norm = cv2.normalize(cv_image_array, cv_image_array, 0, 1, cv2.NORM_MINMAX)
  #cv2.imshow("camera", cv_image_array)
  #bbox, ids = findAruco(frame)
  #print(cv_image_norm.shape)
  #arr = []
  #my_arr = Float32(cv_image_array)
  #pub.publish(cv_image_array)
  cv2.waitKey(1)
      
def receive_image():
  print(2)
  rospy.init_node('receive_image', anonymous=True)
  rospy.Subscriber('/rgb_cam', numpy_msg(Floats), callback)
  
  rospy.spin()
  cv2.destroyAllWindows()
  
  
"""

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

"""
if __name__ == '__main__':
    receive_image()









