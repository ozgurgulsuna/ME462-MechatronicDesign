
# Importing Libraries
import serial
import time
import rclpy
from rclpy.node import Node
from rclpy.executors import Executor
from concurrent.futures import ThreadPoolExecutor
import os

from std_msgs.msg import String
from geometry_msgs.msg import Twist





arduino = serial.Serial(port='/dev/ttyUSB0', baudrate=115200, timeout=.1)


def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.0005)
    #data = arduino.readline().decode()
    #return data



class PriorityExecutor(Executor):
    """
    Execute high priority callbacks in multiple threads, all others in a single thread.
    This is an example of a custom exectuor in python. Executors are responsible for managing
    how callbacks get mapped to threads. Rclpy provides two executors: one which runs all callbacks
    in the main thread, and another which runs callbacks in a pool of threads. A custom executor
    should be written if neither are appropriate for your application.
    """

    def __init__(self):
        super().__init__()
        self.high_priority_nodes = set()
        self.hp_executor = ThreadPoolExecutor(max_workers=os.cpu_count() or 4)
        self.lp_executor = ThreadPoolExecutor(max_workers=1)

    def add_high_priority_node(self, node):
        self.high_priority_nodes.add(node)
        # add_node inherited
        self.add_node(node)

    def spin_once(self, timeout_sec=None):
        """
        Execute a single callback, then return.
        This is the only function which must be overridden by a custom executor. Its job is to
        start executing one callback, then return. It uses the method `wait_for_ready_callbacks`
        to get work to execute.
        :param timeout_sec: Seconds to wait. Block forever if None. Don't wait if <= 0
        :type timeout_sec: float or None
        """
        # wait_for_ready_callbacks yields callbacks that are ready to be executed
        try:
            handler, group, node = self.wait_for_ready_callbacks(timeout_sec=timeout_sec)
        except StopIteration:
            pass
        else:
            if node in self.high_priority_nodes:
                self.hp_executor.submit(handler)
            else:
                self.lp_executor.submit(handler)

     
        
class Differentials(Node):

    def __init__(self):
        super().__init__('differentials')
        self.subscription = self.create_subscription(
            String,
            'diffs',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        #self.get_logger().info('I heard222: "%s"' % msg.data)
        message = "D " + msg.data
        print(message)
        write_read(message)

        
        
class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
            Twist,
            'turtle1/cmd_vel',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        #self.get_logger().info('I heard: "%s"' % msg.linear.x)
        message = "V " + str(msg.linear.x) + " " + str(msg.angular.z)
        print(message)
        write_read(message)


def main(args=None):
    rclpy.init(args=args)

    
    differentials = Differentials()
    minimal_subscriber = MinimalSubscriber()
    
    executor = PriorityExecutor()
    executor.add_node(differentials)
    executor.add_node(minimal_subscriber)
    executor.spin()
	
    
    rclpy.spin(differentials)
    rclpy.spin(minimal_subscriber)
    print(str(diff))

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    executor.shutdown()
    minimal_subscriber.destroy_node()
    differentials.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
    
    
    






        
