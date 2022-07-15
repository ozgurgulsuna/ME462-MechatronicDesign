#!/usr/bin/env python
# Importing Libraries

from pynput import keyboard
import threading
import serial
import time
import rospy
import os
from geometry_msgs.msg import Twist



global lin_vel, ang_vel
lin_vel, ang_vel = 0, 0
x, y, i, j = 0, 0, 0, 0
sag, sol = 0 ,0
def pub_commands(lin, ang):
    #print('inside pub')
    # Create a publisher which can "talk" to Turtlesim and tell it to move

    rate = rospy.Rate(10)
     
    # Create a Twist message and add linear x and angular z values
    move_cmd = Twist()
    move_cmd.linear.x = lin
    move_cmd.angular.z = ang
    
    pub.publish(move_cmd)
    #rate.sleep()





"""
def turn():
    global lin_vel, ang_vel, x, y, i, j
    while 1:
        print(x)
        if x == 1:
            print("xx")
            lin_vel=abs(lin_vel)
            pub_commands(lin_vel, ang_vel)
            time.sleep(0.01)
        if y == 1:
            lin_vel=-1*abs(lin_vel)
            pub_commands(lin_vel, ang_vel)
            time.sleep(0.01)
        if i == 1:
            ang_vel=-abs(ang_vel)
            pub_commands(lin_vel, ang_vel)
            time.sleep(0.01)
        if j == 1:
            ang_vel=abs(ang_vel)
            pub_commands(lin_vel, ang_vel)
            time.sleep(0.01)"""


def on_press(key):
    global lin_vel, ang_vel, x, y, i, j, sag, sol
    

    try:
    
        #print(lin_vel, ang_vel)  
        if key.char ==  'w':
            lin_vel=abs(lin_vel)
            if(sag == 1 or sol == 1):
                pub_commands(lin_vel, 0)
            else:
                pub_commands(lin_vel, 0)

        if key.char ==  's':
            lin_vel=-1*abs(lin_vel)
            if(sag == 1 or sol == 1):
                pub_commands(lin_vel, 0)
            else:
                pub_commands(lin_vel, 0)
            
        if key.char ==  'a':
            sol = 1
            ang_vel=abs(ang_vel)
            pub_commands(0, ang_vel)
            #time.sleep(0.01)


        if key.char ==  'd':
            sag = 1
            ang_vel=-abs(ang_vel)
            pub_commands(0, ang_vel)
            #time.sleep(0.01)


       
        if key.char ==  'e':
            if lin_vel>=0:

                lin_vel = lin_vel + 10
                
            else:
                lin_vel = lin_vel - 10


        if key.char ==  'q':
        
            if lin_vel>0:

                lin_vel = lin_vel - 10  
                
            else:
            
                lin_vel = lin_vel + 10
            

        if key.char ==  'z':
            if ang_vel >=0:

                ang_vel = ang_vel - 10
            else:
                ang_vel = ang_vel+10


        if key.char ==  'c':

            if ang_vel >=0:

                ang_vel = ang_vel + 10
            else:
                ang_vel = ang_vel-10
    except:
        pass
        
    
    
def on_release(key):
    pub_commands(0, 0)
    


    
    '''
    try:
        if key.char ==  'w':
            x = 0
        if key.char ==  's':
            y = 0
        if key.char ==  'a':
            i = 0
        if key.char ==  'd':
            j = 0
        
    except:
        pass
    '''
    pass









if __name__ == '__main__':

    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rospy.init_node('pub_commands', anonymous=True) 
    #threading.Thread(target = turn)
    #pub_commands(5, 0)

    listener = keyboard.Listener(
        on_press=on_press,
        on_release=on_release)
    listener.start()
    time.sleep(999999)        
    #rospy.spin()
