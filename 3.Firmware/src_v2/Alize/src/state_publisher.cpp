#include <tf/transform_broadcaster.h>
#include <nav_msgs/Odometry.h>
#include <string>
#include <ros/ros.h>
#include <sensor_msgs/JointState.h>
#include "geometry_msgs/Twist.h"


double current_time, last_time;
double x = 0.0;
double y = 0.0;
double th = 0.0;

double vx = 0.0;
double vy = 0.0;
double vth = 0.0;


double pan_angle = 0.0;

double dt = 0.0;
double delta_x = 0.0;
double delta_y = 0.0;
double delta_th = 0.0;

double vel = 0.0;





void pan_Callback(const geometry_msgs::Twist& msg)
{
  
  pan_angle = float(msg.angular.z);
  ROS_INFO("I heard: [%f]", pan_angle);
  ROS_INFO("I heard2: [%f]", float(msg.angular.z));
  ROS_INFO("I heard2: [%f]", msg.angular.z);
  

}

int main(int argc, char** argv){

  ros::init(argc, argv, "state_publisher");

  ros::NodeHandle pan;
  ros::Subscriber subb = pan.subscribe("pan_angle", 1000, pan_Callback);
	




ros::spin();



} 
