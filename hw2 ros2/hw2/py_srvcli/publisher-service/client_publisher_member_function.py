import sys

from std_srvs.srv import SetBool
from std_msgs.msg import Int32

import rclpy
from rclpy.node import Node


class CounterPublisherClient(Node):

    def __init__(self):
        super().__init__('counter_publisher_client')
        self.cli = self.create_client(SetBool, 'set_publishing_state')
        
        self.publisher = self.create_publisher(Int32, 'counter', 10)
        self.timer = None
        self.counter_value = 0
        self.is_publishing = False

        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')

        def start_publishing(self):
            """publishing service when setbool==true"""
            self.call_service(True)

        def stop_publishing(self):
            """publishing service when setbool==false"""
            self.call_service(False)

        def call_service(self, enable_publishing):
            """Call the SetBool service"""
            request = SetBool.Request()
            request.data = enable_publishing

            future = self.client.call_async(request)
            rclpy.spin_until_future_complete(self, future)

            response = future.result()
            self.get_logger().info(f'Service response: {response.message}')

            if enable_publishing:
                self.is_publishing = True
                self.counter_value = 0
                self.timer = self.create_timer (0.01,self.publish_counter)
                self.get_logger().info('Started Publishing')
            else:
                self.is_publishing = False
                if self.timer:
                    self.timer.destroy()
                self.get_logger().info('Stopped Publishing')

        

    


def main(args=None):
    rclpy.init(args=args)

    counter_node = CounterPublishingClient()
    rclpy.spin(counter_node)
    counter_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()