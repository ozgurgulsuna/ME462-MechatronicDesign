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


double pan_angle = 10.0;

double dt = 0.0;
double delta_x = 0.0;
double delta_y = 0.0;
double delta_th = 0.0;

double vel = 0.0;


void chatterCallback(const geometry_msgs::Twist& msg)
{

    vel = msg.linear.x;
    vth = msg.angular.z;
    vx = vel;
    vy = 0;  
  
}


void pan_Callback(const geometry_msgs::Twist& msg)
{
  
  pan_angle = float(msg.angular.z);
  //ROS_INFO("I heard: [%f]", msg.angular.z);
  //cout << "Hello World!";
  

}

int main(int argc, char** argv){

  ros::init(argc, argv, "deneme");

  ros::NodeHandle st;  
  ros::Publisher joint_pub = st.advertise<sensor_msgs::JointState>("joint_states", 1);
  

  ros::NodeHandle pan;
  ros::Subscriber subb = pan.subscribe("pan_angle", 1000, pan_Callback);


  ros::NodeHandle n;
  ros::Publisher odom_pub = n.advertise<nav_msgs::Odometry>("odom", 50);
  tf::TransformBroadcaster odom_broadcaster;
  

  ros::NodeHandle en;
  ros::Subscriber sub = en.subscribe("encoder", 1000, chatterCallback);



  ros::Time current_time, last_time;
  current_time = ros::Time::now();
  last_time = ros::Time::now();

  ros::Rate r(50);
  while(n.ok()){
    sensor_msgs::JointState joint_state;
    joint_state.header.stamp = ros::Time::now();
    joint_state.name.resize(1);
    joint_state.position.resize(1);
    joint_state.name[0] ="base_link_to_pan";
    joint_state.position[0] = pan_angle;

  
  
    //printf("%f", x);
    ros::spinOnce();               // check for incoming messages
    current_time = ros::Time::now();
    
    //compute odometry in a typical way given the velocities of the robot
    dt = (current_time - last_time).toSec();
    delta_x = vx * dt * cos(th);
    delta_y = vx*dt*sin(th);
    delta_th = vth * dt;

    x += delta_x;
    y += delta_y;
    th += delta_th;
    //printf("%f", x);

    //since all odometry is 6DOF we'll need a quaternion created from yaw
    geometry_msgs::Quaternion odom_quat = tf::createQuaternionMsgFromYaw(th);

    //first, we'll publish the transform over tf
    geometry_msgs::TransformStamped odom_trans;
    
    odom_trans.header.stamp = current_time;
    odom_trans.header.frame_id = "odom";
    odom_trans.child_frame_id = "base_link";

    odom_trans.transform.translation.x = x;
    odom_trans.transform.translation.y = y;
    odom_trans.transform.translation.z = 0.0;
    odom_trans.transform.rotation = odom_quat;

    //send the transform
    odom_broadcaster.sendTransform(odom_trans);
    joint_pub.publish(joint_state);

    //next, we'll publish the odometry message over ROS
    nav_msgs::Odometry odom;
    odom.header.stamp = current_time;
    odom.header.frame_id = "odom";

    //set the position
    odom.pose.pose.position.x = x;
    odom.pose.pose.position.y = y;
    odom.pose.pose.position.z = 0.0;
    odom.pose.pose.orientation = odom_quat;

    //set the velocity
    odom.child_frame_id = "base_link";
    odom.twist.twist.linear.x = vx;
    odom.twist.twist.linear.y = vy;
    odom.twist.twist.angular.z = vth;

    //publish the message
    odom_pub.publish(odom);
    

    last_time = current_time;
    r.sleep();
  }
} 
