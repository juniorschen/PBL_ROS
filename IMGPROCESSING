import cv2
import numpy as np

def random_callback(msg):
    bridge = CvBridge()
    cv_image = bridge.imgmsg_to_cv2(msg, desired_encoding="bgr8")


    cv_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)

    eq = cv2.equalizeHist(cv_image)	
    image_message = bridge.cv2_to_imgmsg(cv_image, encoding="mono8")
    eq_message = bridge.cv2_to_imgmsg(eq, encoding="mono8")
    ret, tresh = cv2.threshold(cv_image, 80, 255, cv2.THRESH_BINARY)
    lim_message = bridge.cv2_to_imgmsg(tresh, encoding="mono8")
    suave = cv2.GaussianBlur(cv_image, (7, 7), 0)
    canny2 = cv2.Canny(suave, 70, 200)
    resultado = np.vstack([cv_image, canny2])
    canny_message = bridge.cv2_to_imgmsg(resultado, encoding="mono8")

    pub=rospy.Publisher('img_gray', Image, queue_size=10)
    pub.publish(image_message)
    pub1=rospy.Publisher('img_eq', Image, queue_size=10)
    pub1.publish(eq_message)
    pub2=rospy.Publisher('img_li', Image, queue_size=10)
    pub2.publish(lim_message)
    pub2=rospy.Publisher('img_canny', Image, queue_size=10)
    pub2.publish(canny_message)


    #r = rospy.Rate(10)
    #while(true):
      #cv2.imshow('my subs', cv_image)
      #cv2.waitKey(5)
      #r.sleep()
      #pub=rospy.Publisher('rand_no', Image, queue_size=10)
if __name__=='__main__':

    rospy.init_node('img')
    sub=rospy.Subscriber('/usb_cam/image_raw', Image, random_callback)
    rospy.spin()
