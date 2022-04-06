#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String
def talker():
    rospy.init_node('talker')
    pub = rospy.Publisher('Ivan', String, queue_size=10)


    rate = rospy.Rate(4) # 4hz
    counter=0
    while not rospy.is_shutdown():
        hello_str="hola %d" % counter
        counter=counter+1
        
        pub.publish(hello_str)
        rate.sleep()
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass