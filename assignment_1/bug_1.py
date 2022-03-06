#!/usr/bin/env python

from sc627_helper.msg import MoveXYAction, MoveXYGoal, MoveXYResult
import rospy
import actionlib
import numpy as np
#import other helper files if any


rospy.init_node('test', anonymous= True)

#Initialize client
client = actionlib.SimpleActionClient('move_xy', MoveXYAction)
client.wait_for_server()

#read input file
lines = []
with open("catkin_ws/src/sc627_assignments/assignment_1/input.txt") as f:
    lines = f.readlines()
start1 = lines[0].strip()
start = [start1[0], start1[2]]
goal1 = lines[1].strip()
goal = [goal1[0], goal1[2]]

step = lines[2]

obstacle1 = np.array([[1, 2], [1, 0], [3, 0]])
obstacle2 = np.array([[2, 3], [4, 1], [5, 2]])

#setting result as initial location
result = MoveXYResult()
result.pose_final.x = 0
result.pose_final.y = 0
result.pose_final.theta = 0 #in radians (0 to 2pi)

#Bug1

while True: #replace true with termination condition

    #determine waypoint based on your algo
    #this is a dummy waypoint (replace the part below)
    wp = MoveXYGoal()
    wp.pose_dest.x = 1 + result.pose_final.x
    wp.pose_dest.y = 0
    wp.pose_dest.theta = 0 #theta is the orientation of robot in radians (0 to 2pi)

    #send waypoint to turtlebot3 via move_xy server
    client.send_goal(wp)

    client.wait_for_result()

    #getting updated robot location
    result = client.get_result()

    #write to output file (replacing the part below)
    print(result.pose_final.x, result.pose_final.y, result.pose_final.theta)