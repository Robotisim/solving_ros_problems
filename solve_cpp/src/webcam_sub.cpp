#include <chrono>
#include <memory>

#include "cv_bridge/cv_bridge.h"
#include "rclcpp/rclcpp.hpp"
#include "sensor_msgs/msg/image.hpp"
#include "std_msgs/msg/header.hpp"
#include <opencv2/opencv.hpp>
#include <opencv2/highgui.hpp>
#include <stdio.h>

#include <opencv2/core/types.hpp>
#include <opencv2/core/hal/interface.h>
#include <image_transport/image_transport.hpp>
#include <opencv2/imgproc/imgproc.hpp>

using std::placeholders::_1;

class MinimalSubscriber : public rclcpp::Node {
  public:
    MinimalSubscriber()
    : Node("minimal_subscriber")
    {
      auto qos_profile = rclcpp::QoS(rclcpp::KeepLast(10));
      subscription_ = this->create_subscription<sensor_msgs::msg::Image>(
      "topic", qos_profile, std::bind(&MinimalSubscriber::topic_callback, this, _1));
    }

  private :
    void topic_callback(sensor_msgs::msg::Image::SharedPtr msg) const
    {
      RCLCPP_INFO(this->get_logger(), "In callback");
      // cv_bridge::CvImagePtr cv_ptr;
      // cv_ptr = cv_bridge::toCvCopy(msg,"bgr8");
      // cv::imshow("minimal_subscriber", cv_ptr->image);
      // cv::waitKey(1);
    }
    rclcpp::Subscription<sensor_msgs::msg::Image>::SharedPtr subscription_;
};

int main(int argc, char *argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<MinimalSubscriber>());
  rclcpp::shutdown();
  return 0;
}