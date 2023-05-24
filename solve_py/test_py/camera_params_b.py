import rclpy
from rclpy.node import Node
from sensor_msgs.msg import CameraInfo
import yaml

class CameraInfoPublisher(Node):
    def __init__(self):
        super().__init__('camera_info_publisher')
        self.publisher_ = self.create_publisher(CameraInfo, 'camera/camera_info', 10)

        # Load parameters from a YAML file
        with open('/home/luqman/robotisim_ws/src/test_py/config/camera_config_b.yaml', 'r') as f:
            params = yaml.safe_load(f)

        # Create a CameraInfo message and fill in the values
        msg = CameraInfo()
        msg.header.frame_id = params["camera_name"]
        msg.height = params["image_height"]
        msg.width = params["image_width"]
        msg.distortion_model = params["distortion_model"]
        msg.d = [float(val) for val in params["distortion_coefficients"]["data"]]
        msg.k = [float(val) for val in params["camera_matrix"]["data"]]
        msg.r = [float(val) for val in params["rectification_matrix"]["data"]]
        msg.p = [float(val) for val in params["projection_matrix"]["data"]]

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
