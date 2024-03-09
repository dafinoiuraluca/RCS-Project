#!/usr/bin/env python3
import rospy
from moveit_commander import RobotCommander, PlanningSceneInterface, MoveGroupCommander
from math import pi
import time

def start_program():
    # group.set_goal_tolerance(0.7)
    group.set_planning_time(10)
    group.set_max_velocity_scaling_factor(0.2)

    starting_point = [0.0, 0.0, 0.0, -pi/2, 0.0, 0.0]
    group.go(starting_point, wait=True)
    group.stop()
    # rospy.sleep(0.5)

    # first waypoint
    first_waypoint = group.get_current_joint_values()

    first_waypoint[0] = pi/4
    first_waypoint[1] = 0
    first_waypoint[2] = 0
    first_waypoint[3] = -pi/2
    first_waypoint[4] = 0
    first_waypoint[5] = 0

    group.go(first_waypoint, wait=True)
    group.stop()
    # rospy.sleep(0.5)

    # second waypoint
    second_waypoint = group.get_current_joint_values()

    second_waypoint[0] = first_waypoint[0]
    second_waypoint[1] = -pi/8
    second_waypoint[2] = 0
    second_waypoint[3] = -pi/2
    second_waypoint[4] = 0
    second_waypoint[5] = 0 

    group.go(second_waypoint, wait=True)
    group.stop()
    # rospy.sleep(0.5)

    #third waypoint
    third_waypoint = group.get_current_joint_values()
    third_waypoint[0] = second_waypoint[0]
    third_waypoint[1] = -pi/3
    third_waypoint[2] = pi/3
    third_waypoint[3] = 0
    third_waypoint[4] = 0
    third_waypoint[5] = 0

    group.go(third_waypoint, wait=True)
    group.stop()
    # rospy.sleep(0.5)

    # forth waypoint
    fourth_waypoint = group.get_current_joint_values()
    fourth_waypoint[0] = 3*pi/4
    fourth_waypoint[1] = third_waypoint[1]
    fourth_waypoint[2] = pi/2
    fourth_waypoint[3] = -pi
    fourth_waypoint[4] = 0
    fourth_waypoint[5] = 0

    group.go(fourth_waypoint, wait=True)
    group.stop()
    rospy.sleep(0.5)

    group.go(third_waypoint, wait=True)
    group.stop()
    # rospy.sleep(0.5)

    group.go(second_waypoint, wait=True)
    group.stop()
    # rospy.sleep(0.5)

    group.go(first_waypoint, wait=True)
    group.stop()
    # rospy.sleep(0.5)

    # goal pose
    goal_pose = group.set_named_target("home")
    group.go(goal_pose, wait=True)
    group.stop()

    
if __name__ == "__main__":
    rospy.init_node('robot_program_node')
    robot = RobotCommander()
    scene = PlanningSceneInterface()
    group_name = "manipulator"
    group = MoveGroupCommander(group_name)

    # planning_frame = group.get_planning_frame()
    # print("============ Planning frame: %s" % planning_frame)

    # group_names = robot.get_group_names()
    # print("============ Planning Groups:", robot.get_group_names())

    print("============ Printing robot state")
    print(robot.get_current_state())

    
    start_time = time.time()
    start_program()
    end_time = time.time()
    total_duration = end_time - start_time
    print("============= Duration of the task: ", total_duration)