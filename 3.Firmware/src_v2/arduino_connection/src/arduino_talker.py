#!/usr/bin/env python
# Importing Libraries
import serial
import time
import rospy
import os
import threading
from std_msgs.msg import String
from geometry_msgs.msg import Twist
import multiprocessing
from multiprocessing import Process, Queue
from concurrent.futures import ThreadPoolExecutor


x = 50

def write_read(x):
    
    arduino.write(x.encode())
    time.sleep(1/1000)
    data = arduino.readline().decode()
    print(data)
    return data
    
    
    
def pan_angle(q):
    #global x
    #type(x)
    
    pub = rospy.Publisher('pan_angle', Twist, queue_size=10)
    rospy.init_node('pan_angle', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while 1:
        move_cmd = Twist()
        try:
            x = int(q.get())

            #print(type(x))
            #print(x)
            move_cmd.angular.z = float((x-50+180)*3.14/180)
            
            
            pub.publish(move_cmd)
            rate.sleep()
        except:
            pass
        



def callback_car_vel(msg):
    message = "V " + str(msg.linear.x) + " " + str(msg.angular.z)
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

def callback_pan(msg, q):
    global x
    message = "P " + str(msg.angular.z)
    #print(message)
    x = write_read(message)
    try:
        q.get_nowait()
    except:
        pass
    q.put(x)

def pan(q):

    rospy.init_node('pan', anonymous=True)

    rospy.Subscriber("/turtle1/cmd_vel", Twist, callback_pan, callback_args = q)
    #print("iceri")

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    

    arduino = serial.Serial(port='/dev/ttyUSB0', baudrate=115200, timeout=.1)
    try:
    

        #car_vel()
        th_car_vel = Process(target = car_vel)
        th_diff = Process(target = differentials)
        th_car_vel.start()
        th_diff.start()
        q = Queue()
        th_pan = Process(target = pan, args = (q,))
        th_pan.start()
        #pan()
        pan_angle(q)
        #rospy.spin()


    except rospy.ROSInterruptException:
        pass



























