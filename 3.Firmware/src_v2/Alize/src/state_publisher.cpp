#include <string>
#include <ros/ros.h>
#include <sensor_msgs/JointState.h>
#include <tf/transform_broadcaster.h>
#include "geometry_msgs/Twist.h"
#include <nav_msgs/Odometry.h>

double current_time, last_time;
double x = 0.0;
double y = 0.0;
double th = 0.0;

double vx = 0.0;
double vy = 0.0;
double vth = 0.0;

double dt = 0.0;
double delta_x = 0.0;
double delta_y = 0.0;
double delta_th = 0.0;

double vel = 0.0;


void chatterCallback(const geometry_msgs::Twist& msg)
{
    //dt = (current_time - last_time);
    vel = msg.linear.x;
    //printf("%f", vel);
    vth = msg.angular.z;
    vx = vel * sin(th);
    vy = vel * cos(th);
    /*
    delta_x = (vx * cos(th) - vy * sin(th)) * dt;
    delta_y = (vx * sin(th) + vy * cos(th)) * dt;
    delta_th = vth * dt;
    x += delta_x;
    //x += 10;
    y += delta_y;
    th += delta_th;
    //ROS_INFO("I heard: [%f]", msg.linear.x);
    //printf("%f", msg.linear.x);*/
    
  
}


int main(int argc, char** argv) {

    ros::init(argc, argv, "odometry_publisher");

    ros::NodeHandle od;
    ros::Publisher odom_pub = od.advertise<nav_msgs::Odometry>("odom", 50);
    tf::TransformBroadcaster odom_broadcaster;
  
  
    ros::init(argc, argv, "state_publisher");
    ros::init(argc, argv, "encoder");
    ros::NodeHandle n;
    ros::NodeHandle en;
    ros::Publisher joint_pub = n.advertise<sensor_msgs::JointState>("joint_states", 1);
    tf::TransformBroadcaster broadcaster;
    ros::Rate loop_rate(50);
    
    ros::Subscriber sub = en.subscribe("encoder", 1000, chatterCallback);

    const double degree = M_PI/180;

    // robot state
    double tilt = 0, tinc = degree, pan_angle=0, angle=0, height=0, hinc=0.005;

    // message declarations
    geometry_msgs::TransformStamped odom_trans;
    //sensor_msgs::JointState joint_state;
    odom_trans.header.frame_id = "odom";
    odom_trans.child_frame_id = "base_link";

    while (ros::ok()) {
        ros::Time current_time, last_time;
        ros::spinOnce();  
        current_time = ros::Time::now();
        //update joint_state
        /*
        joint_state.header.stamp = ros::Time::now();
        joint_state.name.resize(1);
        joint_state.position.resize(1);
        joint_state.name[0] ="base_link_to_pan";
        joint_state.position[0] = pan_angle;
        */
        
        //compute odometry in a typical way given the velocities of the robot
        dt = (current_time - last_time).toSec();
        delta_x = (vx * cos(th) - vy * sin(th)) * dt;
        delta_y = (vx * sin(th) + vy * cos(th)) * dt;
        delta_th = vth * dt;

        x += delta_x;
        y += delta_y;
        th += delta_th;




        geometry_msgs::Quaternion odom_quat = tf::createQuaternionMsgFromYaw(th);
        odom_trans.header.stamp = ros::Time::now();
        odom_trans.transform.translation.x = x;
        odom_trans.transform.translation.y = y;
        odom_trans.transform.translation.z = 0.0;
        odom_trans.transform.rotation = odom_quat;
        //printf("%f", x);
        
        odom_broadcaster.sendTransform(odom_trans);
        
        //next, we'll publish the odometry message over ROS
        nav_msgs::Odometry odom;
        odom.header.stamp = current_time;
        odom.header.frame_id = "odom";

        //set the position
        odom.pose.pose.position.x = 0.0;
        odom.pose.pose.position.y = 0.0;
        odom.pose.pose.position.z = 0.0;
        odom.pose.pose.orientation = odom_quat;

        //set the velocity
        odom.child_frame_id = "base_link";
        odom.twist.twist.linear.x = 0.0;
        odom.twist.twist.linear.y = 0.0;
        odom.twist.twist.angular.z = 0.0;


        //joint_pub.publish(joint_state);
        
        
        //publish the message
        odom_pub.publish(odom);
        
        last_time = current_time;
        loop_rate.sleep();
        //ros::spin();
	
    }


    return 0;
}
