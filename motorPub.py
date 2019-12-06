
#!/usr/bin/env python
import rospy

from std_msgs.msg import Int32
from random import randint

def random_number_publisher():
    rospy.init_node('random_number')
    pub=rospy.Publisher('pub', Int32, queue_size=10)
    rate= rospy.Rate(2)
    while not rospy.is_shutdown():
        random_msg=randint(0,180)
        rospy.loginfo(random_msg)
        pub.publish(random_msg)
        rate.sleep()
