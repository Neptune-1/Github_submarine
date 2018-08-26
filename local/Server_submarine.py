import socket
import os
import time
import cv2
import RPi.GPIO as GPIO

from os import system
# try:
#     system('sudo pigpiod')
#     import pigpio
# except:
#     print('can not pigpio init')

motor = 24
# pi = pigpio.pi()

# pi.set_servo_pulsewidth(motor, 1500)
# time.sleep(0.3)

# pi.set_servo_pulsewidth(motor, 1900)
# time.sleep(2)

# pi.set_servo_pulsewidth(motor, 1500)

i = 0
OK_send = 0
OK_foto = 0
file = ""

cap = cv2.VideoCapture(0) 
beg = 0
speed = 1500
while beg == 0:
    try:
        sock = socket.socket()
        sock.bind(('', 9001))  
        sock.listen(1)
        conn, addr = sock.accept()
        i = 1
        print('connect')
    except:
        pass

# sock.setblocking(0)
# sock.settimeout(5)

right_servo = 22
left_servo = 27
up_servo = 17
down_servo = 23

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(right_servo, GPIO.OUT)
GPIO.setup(left_servo, GPIO.OUT)
GPIO.setup(up_servo, GPIO.OUT)
GPIO.setup(down_servo, GPIO.OUT)

GPIO.setup(right_servo, GPIO.LOW)
GPIO.setup(left_servo, GPIO.LOW)
GPIO.setup(up_servo, GPIO.LOW)
GPIO.setup(down_servo, GPIO.LOW)

while True: 
    data = b''

    conn.setblocking(False)
    try:
        data = conn.recv(50)

    except:
        pass

    if data == b'left':
        # right_servo .ChangeDutyCycle(4)
        # left_servo .ChangeDutyCycle(4)

        GPIO.setup(right_servo, GPIO.LOW)
        GPIO.setup(left_servo, GPIO.HIGH)
        print('left')

    elif data == b'right':

        GPIO.setup(right_servo, GPIO.HIGH)
        GPIO.setup(left_servo, GPIO.LOW)
        print('right')

    elif data == b'up':

        GPIO.setup(up_servo, GPIO.HIGH)
        GPIO.setup(down_servo, GPIO.LOW)
        print('up')

    elif data == b'down':

        GPIO.setup(up_servo, GPIO.LOW)
        GPIO.setup(down_servo, GPIO.HIGH)
        print('down')

    elif data == b'stop':

        GPIO.setup(right_servo, GPIO.LOW)
        GPIO.setup(left_servo, GPIO.LOW)
        GPIO.setup(up_servo, GPIO.LOW)
        GPIO.setup(down_servo, GPIO.LOW)

        pi.set_servo_pulsewidth(motor, 1500)
        print('stop')

    elif data == b'-':
        if speed > 1500:
            speed -= 100
        pi.set_servo_pulsewidth(motor, speed)
        print('-')

    elif data == b'+':
        if speed < 2000:
            speed += 100
        pi.set_servo_pulsewidth(motor, speed)
        print('+')

    file = "Number" + str(1) + ".jpg" 
    i += 1
    ret, im = cap.read()  
    res = cv2.resize(im, (320, 240))

    if data != None:
        try:
            cv2.imwrite(file, res)
            file_op = open(file, "rb")  
            file_read = file_op.read()
            time.sleep(2)
        except:
            print("Error")

    try:
        conn.send(file_read)
        conn.send(b'stop')
        print(1)
    except:

        print(0)
# conn.close()
# pi.stop()
