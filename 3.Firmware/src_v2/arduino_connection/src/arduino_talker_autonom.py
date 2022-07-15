#!/usr/bin/env python
# Importing Libraries
import serial
import time
import rospy
import os
import threading
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from ackermann_msgs.msg import AckermannDriveStamped
x = 0

def write_read_2(x):

    arduino.write(x.encode())

def callback_acker(msg):
    if msg.drive.speed == 0:
        msg.drive.speed = 0
    elif 0 < msg.drive.speed:
        msg.drive.speed = 90 + 10 * msg.drive.speed
    elif msg.drive.speed < 0:
        msg.drive.speed = -110 + msg.drive.speed * 12
    message = "A " + str(msg.drive.speed+1) + " " + str(msg.drive.steering_angle*50*180/3.14+1)
    print(message)
    write_read_2(message)
    #time.sleep(0.01)



def acker():


    rospy.init_node('acker', anonymous=True)

    rospy.Subscriber("/ackermann_cmd", AckermannDriveStamped, callback_acker)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

    
    
    
if __name__ == '__main__':

    print(1)
    arduino = serial.Serial(port='/dev/ttyUSB0', baudrate=115200, timeout=.1)

    acker()


