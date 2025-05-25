
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='py_srvcli',
            executable='service',
            name='setbool_service'
        ),
        Node(
            package='py_srvcli',
            executable='client',
            name='counter_publisher_client'
        ),
        Node(
            package='rqt_gui',
            executable='rqt_gui',
            name='rqt'
        )
    ])
