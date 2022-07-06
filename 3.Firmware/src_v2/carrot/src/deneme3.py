#!/usr/bin/env python
# Importing Libraries

import cv2
import numpy as np
import time
import rospy
import os
from geometry_msgs.msg import Twist
from multiprocessing import Process, Queue
from concurrent.futures import ThreadPoolExecutor

area_threshold, mid_x_axis, min_area = 60000, 320, 1000 

pan_angle = 0.0

#cv2.namedWindow("Bos pencere")


def nothing(x):
    pass


def callback_pan_listener(msg):
    pan_angle = msg.angular.z*180/3.14+50
    print(pan_angle)
    #rospy.loginfo(rospy.get_caller_id() + "I heard %f", pan_angle)
    """rate = rospy.Rate(10)
     
    # Create a Twist message and add angular z values
    move_cmd = Twist()
    move_cmd.angular.z = pan_angle

    
    pub.publish(move_cmd)
    rate.sleep()  """  


    
def pan_listener(angl):


    rospy.init_node('pan_listener', anonymous=True)
    #pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

    rospy.Subscriber("/pan_angle", Twist, callback_pan_listener)
    #print(angl)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

   

    



def pub_commands(q,lin, ang):
    # Create a publisher which can "talk" to Turtlesim and tell it to move
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rospy.init_node('pub_commands', anonymous=True)
    rate = rospy.Rate(10)
     
    # Create a Twist message and add linear x and angular z values
    move_cmd = Twist()
    move_cmd.linear.x = q.get()[0]
    move_cmd.angular.z = q.get()[1]

    
    pub.publish(move_cmd)
    rate.sleep()




cap = cv2.VideoCapture(2)
"""

cv2.namedWindow("Trackbars")

cv2.createTrackbar("L - H", "Trackbars", 0, 179, nothing)
cv2.createTrackbar("L - S", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("L - V", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("U - H", "Trackbars", 179, 179, nothing)
cv2.createTrackbar("U - S", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("U - V", "Trackbars", 255, 255, nothing)
"""


last_linear_vel = 0
linear_vel = 0


#pan_listener(5.0)



def get_carrot():
    global last_linear_vel, linear_vel
    #print("aaa")
    #print("kiii")
    cap.grab() 
    cap.grab() 
    _, frame = cap.read()
    cv2.imshow("frame", frame)
    kernel = np.ones((5,5), np.uint8)
    #blurred_frame = cv2.GaussianBlur(frame, (5, 5), 0)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    """
    l_h = cv2.getTrackbarPos("L - H", "Trackbars")
    l_s = cv2.getTrackbarPos("L - S", "Trackbars")
    l_v = cv2.getTrackbarPos("L - V", "Trackbars")
    u_h = cv2.getTrackbarPos("U - H", "Trackbars")
    u_s = cv2.getTrackbarPos("U - S", "Trackbars")
    u_v = cv2.getTrackbarPos("U - V", "Trackbars")

    lower_carrot = np.array([l_h, l_s, l_v])
    upper_carrot = np.array([u_h, u_s, u_v])
    """
    lower_carrot = np.array([126, 83, 42])
    upper_carrot = np.array([157, 174, 142])
    mask = cv2.inRange(hsv, lower_carrot, upper_carrot)
    mask = cv2.erode(mask, kernel, iterations=1)
    mask = cv2.dilate(mask, kernel, iterations=2)
    result = cv2.bitwise_and(frame, frame, mask = mask)

    _, contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    
    max_area = 0
    sum_x , sum_y = 0, 0


    #try:
        
    if len(contours) == 0:
        max_area = area_threshold
        mean_x = 320

    else:
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > max_area:
                max_area = area
                max_contour = contour

        for j in range(len(max_contour)):
            sum_x = sum_x + max_contour[j][0][0]
            sum_y = sum_y + max_contour[j][0][1]

        mean_x  = sum_x/len(max_contour)
        mean_y = sum_y/len(max_contour)
        
    #print(max_area)
    
    if (area_threshold - max_area)>200:
        linear_vel_calc =  100 + (-area_threshold**-0.5 + max_area**-0.5) * 5000
        if(linear_vel_calc > 150):
            linear_vel_calc = 150
    elif (area_threshold - max_area)<-200:
        linear_vel_calc =  -100 + (-area_threshold**-0.5 + max_area**-0.5) * 8000
        if(linear_vel_calc < -150):
            linear_vel_calc = -150
    else:
        linear_vel_calc = 0
        
    angular_vel = -1*(mean_x - mid_x_axis)*30/320.0 * .25 * 50
    pan_angle_des = mean_x/50
    
    #print(linear_vel, angular_vel)
    #print(max_area)
    #print(pan_angle)
    linear_vel = 0.05 * linear_vel_calc + 0.95 * last_linear_vel
    last_linear_vel = linear_vel_calc
    return [linear_vel, angular_vel, pan_angle_des]
    

    cv2.drawContours(frame, contours, -1, (0, 255, 0), 3)
    
    """except:
        print('i passed')
        pub_commands(0, 0)
        pass"""

    
    #cv2.imshow("frame", frame)
    #cv2.imshow("mask", mask)
    #cv2.imshow("result", result)




if __name__ == '__main__':
    q = Queue()
    th_pub_commands = Process(target = pub_commands, args = (q,0.0,0.0,))
    th_pan_listener = Process(target = pan_listener, args = (0.0,))
    th_pub_commands.start()
    th_pan_listener.start()
#while True:
    #rospy.spin()
    
    
    #linear_vel, angular_vel, pan_angle_des = get_carrot()
    get_carrot()
    vel_com = get_carrot()
    try:
        q.get_nowait()
    except:
        pass
    print(vel_com)
    q.put(vel_com)
        
    pan_listener(vel_com[2])
    
    """cap.release()
    cv2.destroyAllWindows()
    key = cv2.waitKey(1)
    if key == 27:
            break"""
