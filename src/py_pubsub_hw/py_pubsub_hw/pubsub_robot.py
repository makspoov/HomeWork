import rclpy
import math
from rclpy.node import Node

from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from appendix.msg import Num


class Publish(Node):

    def __init__(self):
        super().__init__('publisher')
        self.odometry = self.create_publisher(Odometry, 'odom', 10)
        self.incremate_data = self.create_publisher(Num, 'incremate_data', 10)
        self.subscription = self.create_subscription(Twist, '/cmd_vel', self.subscribe, 1)
        self.x_position = Integrate()
        self.y_position = Integrate()
        self.angle_about_z = Integrate()
        self.angle_rad_left = Integrate()
        self.angle_rad_right = Integrate()
        self.angle_velocity_left = Aperiodic()
        self.angle_velocity_right = Aperiodic()

    def subscribe(self, msg):
    
        x_tau_left = (2*msg.linear.x/0.033-msg.angular.z*0.287/0.033)/2
        x_tau_right = (2*msg.linear.x/0.033+msg.angular.z*0.287/0.033)/2
        y_tau_left = self.angle_velocity_left.integrate_this(x_tau_left)
        y_tau_right = self.angle_velocity_right.integrate_this(x_tau_right)
        real_velocity_of_robot = (0.033/2)*(y_tau_left+y_tau_right)
        ang = (0.033/0.287)*(y_tau_right-y_tau_left)
        x = self.x_position.integrate_this(math.cos(self.angle_about_z.x)*real_velocity_of_robot)
        y = self.y_position.integrate_this(math.sin(self.angle_about_z.x)*real_velocity_of_robot)
        z = self.angle_about_z.integrate_this(ang)
        message_from_incremate_data = Num()
        message_from_incremate_data.header.stamp = self.get_clock().now().to_msg()
        message_from_incremate_data.header.frame_id = "iteration"
        message_from_incremate_data.l = int(((4096 /(3.14*2))* ((self.angle_rad_left.integrate_this(y_tau_left)) % 3.14*2)))
        message_from_incremate_data.r = int(((4096 /(3.14*2))* ((self.angle_rad_right.integrate_this(y_tau_right)) % 3.14*2)))
        odometry = Odometry()
        odometry.header.frame_id = "odom"
        odometry.header.stamp = self.get_clock().now().to_msg()
        odometry.pose.pose.orientation.w = float(math.cos(z/2))
        odometry.pose.pose.orientation.z = float(math.sin(z/2))
        odometry.pose.pose.position.x = float(x)
        odometry.pose.pose.position.y = float(y)
        
        self.odometry.publish(odometry)
        self.incremate_data.publish(message_from_incremate_data)


class Aperiodic():
    def __init__(self):
        self.x = 0
        self.b = 0.1/(0.1+1.2)
    def integrate_this(self,w):
        self.x = self.b*self.x+(1-self.b)*w
        return self.x
    
class Integrate():
    def __init__(self):
        self.x = 0
    def integrate_this(self, real_velocity_of_robot):
        self.x = self.x + real_velocity_of_robot*0.1
        return self.x

def main(args=None):
    rclpy.init(args=args)

    publisher = Publish()

    rclpy.spin(publisher)

    publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
