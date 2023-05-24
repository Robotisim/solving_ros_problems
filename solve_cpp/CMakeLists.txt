cmake_minimum_required(VERSION 3.8)
project(solve_cpp)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(cv_bridge REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(std_msgs REQUIRED)
find_package(rclcpp REQUIRED)
find_package(OpenCV REQUIRED)
find_package(image_transport REQUIRED)


add_executable(webcam_test src/webcam.cpp)
ament_target_dependencies(webcam_test cv_bridge sensor_msgs std_msgs rclcpp image_transport )
target_link_libraries(webcam_test ${OpenCV_LIBS})


add_executable(webcam_test_sub src/webcam_sub.cpp)
ament_target_dependencies(webcam_test_sub cv_bridge sensor_msgs std_msgs rclcpp image_transport )
target_link_libraries(webcam_test_sub ${OpenCV_LIBS})

install(TARGETS webcam_test webcam_test_sub
  DESTINATION lib/${PROJECT_NAME})


  install(DIRECTORY
  DESTINATION share/${PROJECT_NAME}/
)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # comment the line when a copyright and license is added to all source files
  set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # comment the line when this package is in a git repo and when
  # a copyright and license is added to all source files
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
