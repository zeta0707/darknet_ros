from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
  darknet_ros_share_dir = get_package_share_directory('darknet_ros')
  network_param_file = darknet_ros_share_dir + '/config/yolov4-moniarm.yaml'

  darknet_ros_launch = IncludeLaunchDescription(
    PythonLaunchDescriptionSource([darknet_ros_share_dir + '/launch/darknet_ros.launch.py']),
      launch_arguments={'network_param_file': network_param_file}.items()
  )

  return LaunchDescription([
    darknet_ros_launch,
  ])
