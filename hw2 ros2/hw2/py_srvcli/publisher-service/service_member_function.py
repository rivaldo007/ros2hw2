from example_interfaces.srv import AddTwoInts

from std_srvs.srv import SetBool

import rclpy
from rclpy.node import Node


class SetBoolService(Node):

    def __init__(self):
        super().__init__('setbool_service')
        self.srv = self.create_service(SetBool, 'set_publishing_state', self.set_bool_callback)
        self.is_publishing = False  # Track the current publishing state
        self.get_logger().info('SetBool service ready')

    def set_bool_callback(self, request, response):
        self.is_publishing = request.data

        if self.is_publishing
            response.success = True
            response.message = "Publishing starting"
        else:
            response.success = True
            response.message = "Publishing stopping"
            self.get_logger().info('Service called: Publishing stoppe')
        


        return response


def main(args=None):
    rclpy.init(args=args)

    setbool_service = SetBoolService()

    rclpy.spin(setbool_service)

    rclpy.shutdown()


if __name__ == '__main__':
    main()