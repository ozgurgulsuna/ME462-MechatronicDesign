#!/usr/bin/env python
# Importing Libraries
import serial
import time
import rospy
import os

from std_msgs.msg import String
from geometry_msgs.msg import Twist



arduino = serial.Serial(port='/dev/ttyUSB0', baudrate=115200, timeout=.1)

def write_read(x):
    
    arduino.write(x.encode())
    time.sleep(1/1000)
    data = arduino.readline().decode()
    print(data)
    return data



def callback_car_vel(msg):
    message = "V " + str(msg.linear.x) + " " + str(msg.angular.z)
    print(message)
    write_read(message)

def callback_pan(msg):
    message = "P " + str(msg.angular.z)
    print(message)
    write_read(message)
    
def car_vel():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('car_vel', anonymous=True)

    rospy.Subscriber("cmd_vel", Twist, callback_car_vel)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


def callback_diff(msg):
    message = "D " + msg.data
    #print(message)
    write_read(message)
    
def differentials():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('differentials', anonymous=True)

    rospy.Subscriber("diffs", String, callback_diff)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


def pan():


    rospy.init_node('pan', anonymous=True)

    rospy.Subscriber("/turtle1/cmd_vel", Twist, callback_pan)
    print("iceri")

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    try:
        
        car_vel()
        differentials()
        pan()
        

    except rospy.ROSInterruptException:
        pass



























