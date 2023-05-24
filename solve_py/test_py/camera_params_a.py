import rclpy
from rclpy.node import Node
from sensor_msgs.msg import CameraInfo
import yaml

class CameraInfoPublisher(Node):
    def __init__(self):
        super().__init__('camera_info_publisher')
        self.publisher_ = self.create_publisher(CameraInfo, 'camera/camera_info', 10)

        # Load parameters from a YAML file
        with open('/home/luqman/robotisim_ws/src/test_py/config/camera_config_a.yaml', 'r') as f:
            params = yaml.safe_load(f)

        # Create a CameraInfo message and fill in the values
        msg = CameraInfo()
        msg.header.frame_id = params["header"]["frame_id"]
        msg.height = params["height"]
        msg.width = params["width"]
        msg.distortion_model = params["distortion_model"]
        msg.d = params["d"]
        msg.k = params["k"]
        msg.r = params["r"]
        msg.p = params["p"]
        msg.binning_x = params["binning_x"]
        msg.binning_y = params["binning_y"]
        msg.roi.x_offset = params["roi"]["x_offset"]
        msg.roi.y_offset = params["roi"]["y_offset"]
        msg.roi.height = params["roi"]["height"]
        msg.roi.width = params["roi"]["width"]
        msg.roi.do_rectify = params["roi"]["do_rectify"]

        # Publish the message
        self.publisher_.publish(msg)
        self.get_logger().info("Published camera info")

def main(args=None):
    rclpy.init(args=args)

    node = CameraInfoPublisher()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
