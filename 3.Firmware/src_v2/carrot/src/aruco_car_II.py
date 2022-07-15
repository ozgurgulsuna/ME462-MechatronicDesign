#!/usr/bin/env python3
# Importing Libraries

from sensor_msgs.msg import LaserScan
import cv2
import numpy as np
import time
import rospy
import os
from geometry_msgs.msg import Twist
import pyrealsense2.pyrealsense2 as rs
import cv2.aruco as aruco

area_threshold, mid_x_axis = 40000, 320

#cv2.namedWindow("Bos pencere")
#cap = cv2.VideoCapture(2)




def pub_commands(lin, ang):
    # Create a publisher which can "talk" to Turtlesim and tell it to move
    pub = rospy.Publisher('/aruco', Twist, queue_size=10)
    rospy.init_node('pub_commands', anonymous=True)
    rate = rospy.Rate(10)
     
    # Create a Twist message and add linear x and angular z values
    move_cmd = Twist()
    move_cmd.linear.x = lin
    move_cmd.angular.z = ang

    
    pub.publish(move_cmd)
    rate.sleep()



def findAruco(img, marker_size=6, total_markers=100, draw=True):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    key = getattr(aruco,f'DICT_{marker_size}X{marker_size}_{total_markers}')
    arucoDict = aruco.Dictionary_get(key)
    arucoParam = aruco.DetectorParameters_create()
    bbox, ids, _ = aruco.detectMarkers(gray, arucoDict, parameters = arucoParam)
    #print(bbox)
    if draw:
        aruco.drawDetectedMarkers(img, bbox)
        
    return bbox, ids



last_linear_vel = 0
linear_vel = 0
angular_vel = 0
linear_vel_calc = 0


# Configure depth and color streams
pipeline = rs.pipeline()
config = rs.config()

# Get device product line for setting a supporting resolution
pipeline_wrapper = rs.pipeline_wrapper(pipeline)
pipeline_profile = config.resolve(pipeline_wrapper)
device = pipeline_profile.get_device()
device_product_line = str(device.get_info(rs.camera_info.product_line))

found_rgb = False
for s in device.sensors:
    if s.get_info(rs.camera_info.name) == 'RGB Camera':
        found_rgb = True
        break
if not found_rgb:
    print("The demo requires Depth camera with Color sensor")
    exit(0)

config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)

if device_product_line == 'L500':
    config.enable_stream(rs.stream.color, 960, 540, rs.format.bgr8, 30)
else:
    config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

# Start streaming
pipeline.start(config)
    
while True:
    linear_vel = 0
    linear_vel_calc = 0
    #cap.grab() 
    #cap.grab() 
    #_, frame = cap.read()
    frames = pipeline.wait_for_frames()
    depth = frames.get_depth_frame()
    color_frame = frames.get_color_frame()
    color_image = np.asanyarray(color_frame.get_data())
    
    bbox, ids = findAruco(color_image)
    for y in range(24):
        for x in range(32):
            dist = depth.get_distance(x*20, y*20)
            if dist > 0.1 and dist < 0.2:
                linear_vel_calc = -120
                last_linear_vel = -120
    try:
        time.sleep(0.01)
        if ids == None:
            pub_commands(0,angular_vel)
        else:
            mean_x = (bbox[0][0][0][0] + bbox[0][0][1][0] + bbox[0][0][2][0] + bbox[0][0][3][0])/4
            x1, y1, x2, y2, x3, y3 = bbox[0][0][0][0] , bbox[0][0][0][1], bbox[0][0][1][0], bbox[0][0][1][1], bbox[0][0][2][0], bbox[0][0][2][1]
            dist1 = ((x2-x1)**2+(y2-y1)**2)**0.5
            dist2 = ((x3-x2)**2+(y3-y2)**2)**0.5
            max_area = dist2*dist1
            
            if (area_threshold - max_area)>10:
                linear_vel_calc =  100 + (-area_threshold**-0.5 + max_area**-0.5) * 4000
                angular_vel = -1*(mean_x - mid_x_axis)*30/320.0 * .25 * 50
                if(linear_vel_calc > 200):
                    linear_vel_calc = 200
            elif (area_threshold - max_area)<-10:
                angular_vel = 1*(mean_x - mid_x_axis)*30/320.0 * .25 * 50
                linear_vel_calc =  -100 + (-area_threshold**-0.5 + max_area**-0.5) * 6500
                if(linear_vel_calc < -200):
                    linear_vel_calc = -200
            else:
                linear_vel_calc = 0
    except:
        pass

            
                        

                
            
    #print(linear_vel, angular_vel)
    #print(max_area)
    linear_vel = 0.05 * linear_vel_calc + 0.95 * last_linear_vel
    pub_commands(linear_vel, angular_vel)
    last_linear_vel = linear_vel_calc

        
        




    #cv2.imshow("frame", color_image)
    key = cv2.waitKey(1)
    if key == 27:
        break


cv2.destroyAllWindows()

