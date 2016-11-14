#!/usr/bin/env python

import rospy
import cv2
from sensor_msgs.msg import Image
import numpy as np
from cv_bridge import CvBridge

class Node:
    def __init__(self, ):
        self.bridge = CvBridge()
        rospy.Subscriber("image", Image, self.callback)
        self.pub = rospy.Publisher("image_grey", Image, queue_size=1)

    def callback(self, image):
        image = self.bridge.imgmsg_to_cv2(image, "bgr8")
        grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        self.pub.publish(self.bridge.cv2_to_imgmsg(grey, "mono8"))


if __name__ == "__main__":
    rospy.init_node("color2grey")
    node = Node()
    rospy.spin()
