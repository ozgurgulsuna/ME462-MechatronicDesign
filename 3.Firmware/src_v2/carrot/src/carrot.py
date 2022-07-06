#!/usr/bin/env python
# Importing Libraries

import cv2
import numpy as np
import time
import rospy
import os
from geometry_msgs.msg import Twist

area_threshold, mid_x_axis = 60000, 320


cv2.namedWindow("Bos pencere")


def nothing(x):
    pass


def pub_commands(lin, ang):
    # Create a publisher which can "talk" to Turtlesim and tell it to move
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rospy.init_node('pub_commands', anonymous=True)
    rate = rospy.Rate(10)
     
    # Create a Twist message and add linear x and angular z values
    move_cmd = Twist()
    move_cmd.linear.x = lin
    move_cmd.angular.z = ang

    
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
while True:
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


    try:
        
        if len(contours) == 0:
            max_area = area_threshold

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
        #print(linear_vel, angular_vel)
        pub_commands(linear_vel, angular_vel)
        print(max_area)
        linear_vel = 0.05 * linear_vel_calc + 0.95 * last_linear_vel
        last_linear_vel = linear_vel_calc
        
        

        cv2.drawContours(frame, contours, -1, (0, 255, 0), 3)
    except:
        #print('i passed')
        pub_commands(0, 0)
        pass





    




    
    cv2.imshow("frame", frame)
    #cv2.imshow("mask", mask)
    #cv2.imshow("result", result)


    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
