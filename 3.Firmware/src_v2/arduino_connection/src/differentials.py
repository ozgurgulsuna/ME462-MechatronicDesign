#!/usr/bin/env python
# Importing Libraries
import time
import rospy
import os
import sys

from std_msgs.msg import String


x, y, z = 0, 0, 0


def talker():

    pub = rospy.Publisher('diffs', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        
        msg = str(x) + " " + str(y) + " " + str(z)
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':

    try:
        
        x = int(sys.argv[-3])
        y = int(sys.argv[-2])
        z = int(sys.argv[-1])
        talker()
    except rospy.ROSInterruptException:
        pass


