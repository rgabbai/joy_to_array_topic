import os

from ament_index_python.packages import get_package_share_directory

import launch
import launch_ros.actions


def generate_launch_description():
    return launch.LaunchDescription([
      
        launch_ros.actions.Node(
            package='joy_to_array_topic', executable='joy_to_array_node', name='joy_to_array_node',
            remappings={('/custom_array', '/joint_whacker/commands')}),
    
    ])
