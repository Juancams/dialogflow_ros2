project(dialogflow_ros2_interfaces)

cmake_minimum_required(VERSION 3.5)

find_package(ament_cmake REQUIRED)
find_package(builtin_interfaces REQUIRED)
find_package(rosidl_default_generators REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/DialogflowContext.msg"
  "msg/DialogflowEvent.msg"
  "msg/DialogflowParameter.msg"
  "msg/DialogflowRequest.msg"
  "msg/DialogflowResult.msg"
  "srv/DialogflowService.srv"
  DEPENDENCIES builtin_interfaces
)

ament_export_dependencies(rosidl_default_runtime)
ament_package()