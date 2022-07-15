#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge 
import cv2
import numpy as np
import os
from geometry_msgs.msg import Twist
from std_msgs.msg import String,Int32,Int32MultiArray
from rospy_tutorials.msg import Floats
from rospy.numpy_msg import numpy_msg
#import cv2.aruco as aruco

def callback(data):
  br = CvBridge()
  #rospy.loginfo("receiving video frame")
  current_frame = br.imgmsg_to_cv2(data)
  cv_image_array = np.array(current_frame, dtype = np.dtype('f8'))
  image_arr = cv_image_array.tolist()
  #print(len(image_arr))
  cv_image_norm = cv2.normalize(cv_image_array, cv_image_array, 0, 1, cv2.NORM_MINMAX)
  #cv2.imshow("camera", cv_image_array)
  #bbox, ids = findAruco(frame)
  #image_arr = np.float32(cv_image_array)
  #print(type(image_arr))
  #arr = [image_arr[0], image_arr[1], image_arr[2]]
  #print(len(cv_image_array))
  print("aaaaaaaaaaaaaaaaa")
  pub.publish(image_arr)
  cv2.waitKey(1)
      
def receive_message():
  print(2)
  rospy.init_node('receive_message', anonymous=True)
  rospy.Subscriber('/camera/color/image_raw', Image, callback)
  
  rospy.spin()
  cv2.destroyAllWindows()
  
  
if __name__ == '__main__':
  pub=rospy.Publisher('/rgb_cam',Int32,queue_size = 10)
  receive_message()
  
