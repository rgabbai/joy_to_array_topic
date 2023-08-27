import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy
from std_msgs.msg import Float64MultiArray

class JoyToArrayNode(Node):
    def __init__(self):
        super().__init__('joy_to_array_node')
        self.get_logger().info("Joy to Array Node initialized.")
        self.get_logger().info("Joy to Array Node Monitor Button 8,10 and Axes 3 of Logitech Joy.")

        self.subscription = self.create_subscription(
            Joy,
            'joy',
            self.joy_callback,
            10
        )
        self.publisher = self.create_publisher(Float64MultiArray, 'custom_array', 10)

    def joy_callback(self, msg):
        # Check if the message contains the required number of axes
        # Extract the proper buttons and Axes used by the robot in addition to main joy movements handled by tele Op 
        # Current Defintion:
        # Axes 3 - Blade direction on/off 
        if len(msg.buttons) >= 11: # verifiy we have proper joystic connected 
            # Extract the value from axis 3 - use it for Neg or Pos indication for CW/CCW settings
            value_axis_3 = msg.axes[3]
            # Extract the value from button 10 - treat val 1 as Blade on (also check -toggle on/off option) in arduino drv.
            #value_button_10 = float(msg.buttons[10])
            # Just for safety add Button 8 for blade off 
            #value_button_8 = float(msg.buttons[8])
            # Create the Float64MultiArray message
            array_msg = Float64MultiArray()
            #array_msg.data = [value_axis_3, value_button_8, value_button_10 ]
            array_msg.data = [value_axis_3] # Velocity controller expect single value from some reason - TBD 
            # Publish the message
            self.publisher.publish(array_msg)
        else: 
            self.get_logger().warn("Received Joy message does not have enough buttons. Exit..")
            sys.exit()
    

def main(args=None):
    rclpy.init(args=args)
    joy_to_array_node = JoyToArrayNode()
    rclpy.spin(joy_to_array_node)
    joy_to_array_node.destroy_node()
    rclpy.shutdown()


