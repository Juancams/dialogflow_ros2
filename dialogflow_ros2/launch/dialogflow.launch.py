import launch
import launch_ros.actions

def generate_launch_description():

    dialogflow_client_node = launch_ros.actions.Node(
        package='dialogflow_ros2',
        executable='dialogflow_client',
        output='screen'
    )

    return launch.LaunchDescription([dialogflow_client_node])
