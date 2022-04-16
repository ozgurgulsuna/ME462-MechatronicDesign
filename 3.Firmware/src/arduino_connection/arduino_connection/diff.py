# Importing Libraries
import serial
import time
import rclpy
from rclpy.node import Node
import sys
from std_msgs.msg import String

global x, y, z
x, y, z = 0, 0, 0

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(String, 'diffs', 10)
        timer_period = 1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        #self.i = 0
        self.x = x
        self.y = y
        self.z = z

    def timer_callback(self):
        msg = String()
        msg.data = str(self.x) + " " + str(self.y) + " " + str(self.z)
        self.publisher_.publish(msg)
        #self.get_logger().info('Publishing: "%s"' % msg.data)
        #self.x = x


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()
    minimal_publisher.x = int(sys.argv[-3])
    minimal_publisher.y = int(sys.argv[-2])
    minimal_publisher.z = int(sys.argv[-1])

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
  
