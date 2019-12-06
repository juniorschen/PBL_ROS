    #PUBLISHER
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

if __name__=='__main__':
    try:
        random_number_publisher()
    except rospy.ROSInterruptException:
        pass

    #SUBSCRIBER
#!/usr/bin/env python

import rospy
import RPi.GPIO as GPIO

from std_msgs.msg import *

servo_pin = 21

#Ajuste estes valores para obter o intervalo completo do movimento do servo
deg_0_pulse   = 0.5
deg_180_pulse = 2.5
f = 50.0

# Faca alguns calculos dos parametros da largura do pulso
period = 1000/f
k      = 100/period
deg_0_duty = deg_0_pulse*k
pulse_range = deg_180_pulse - deg_0_pulse
duty_range = pulse_range * k

#Iniciar o pino gpio
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin,GPIO.OUT)
pwm = GPIO.PWM(servo_pin,f)
pwm.start(0)

def callback(data):
    duty = deg_0_duty + (data.data/180.0)* duty_range
    pwm.ChangeDutyCycle(duty)

def random_subscriber():
    rospy.init_node('sub')
    rospy.Subscriber('pub',Int32, callback)
    rospy.spin()

if __name__=='__main__':
    random_subscriber()
