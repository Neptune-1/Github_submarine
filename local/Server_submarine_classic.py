import socket
import os
import time
import cv2
# ************************************************************

import RPi.GPIO as GPIO
# ************************************************************

from os import system
try:
    system('sudo pigpiod')
    import pigpio
except:
    print('can not pigpio init')


motor = 24
pi = pigpio.pi()

pi.set_servo_pulsewidth(motor, 1500)
time.sleep(0.3)

pi.set_servo_pulsewidth(motor, 1900)
time.sleep(2)

pi.set_servo_pulsewidth(motor, 1500)

i = 0
OK_send = 0
OK_foto = 0
file = ""
try:
    print('cam 0')
    cap = cv2.VideoCapture(0) 
    print('cam 01')
except:
    print('NO CAMERA')
beg = 0
speed = 1500
print('start connection')
while beg == 0:
    try:
        sock = socket.socket()
        sock.bind(('', 9001))  
        sock.listen(1)
        conn, addr = sock.accept()
        i = 1
        print('connect')
        beg=1
    except Exception as e:
        print('no connection', e)
print('end connection')

# sock.setblocking(0)
# sock.settimeout(5)
# ************************************************************
shut=22
light=23
right_servo = 27
left_servo = 18
up_servo = 17
down_servo = 4

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(shut,GPIO.OUT)
GPIO.setup(light,GPIO.OUT)
GPIO.setup(right_servo, GPIO.OUT)
GPIO.setup(left_servo, GPIO.OUT)
GPIO.setup(up_servo, GPIO.OUT)
GPIO.setup(down_servo, GPIO.OUT)

GPIO.output(shut,True)
GPIO.output(light,False)
GPIO.output(right_servo, False)
GPIO.output(left_servo, False)
GPIO.output(up_servo, False)
GPIO.output(down_servo, False)
# ************************************************************

li=0

es=1
while True: 
    data = b''

    conn.setblocking(False)
    try:
        data = conn.recv(50)

    except:
        pass
# ************************************************************

    if data == b'left':
    
        GPIO.output(right_servo, False)
        GPIO.output(left_servo, True)
        print('left')
    elif data == b'light':
        if li==0:
             GPIO.output(light, True)
             li=1
        else:
             li=0
             GPIO.output(light, False)
    elif data == b'shut':
       
        if li==0:
             GPIO.output(shut, True)
             li=1
        else:
             li=0
             GPIO.output(shut, False)

    elif data == b'right':
    
        GPIO.output(right_servo, True)
        GPIO.output(left_servo, False)
        print('right')
    
    elif data == b'up':
    
        GPIO.output(up_servo, True)
        GPIO.output(down_servo, False)
        print('up')
    
    elif data == b'down':
    
        GPIO.output(up_servo, False)
        GPIO.output(down_servo, True)
        print('down')
    
    elif data == b'stop':
    
        GPIO.output(right_servo, False)
        GPIO.output(left_servo, False)
        GPIO.output(up_servo, False)
        GPIO.output(down_servo, False)
    
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
# ************************************************************


    file = "Number" + str(1) + ".jpg" 
    i += 1
    ret, im = cap.read()
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 4]



    
    try:
        result, encimg = cv2.imencode('.jpg', im, encode_param)
        im1 = cv2.imdecode(encimg, 1)
        res = cv2.resize(im1, (320, 240))
    except:
#         res = cv2.resize(im, (320, 240))
#         res = cv2.putText(res, str(i) ,(160,120),cv2.FONT_HERSHEY_SIMPLEX, 1,(255,0,0),2)
        im=cv2.imread('error.jpg')
        res = cv2.resize(im, (320, 240))
        print('ERROR ENCODE')

    


    print('ok1')
    
    if data != None:
        try:
            cv2.imwrite(file, res)
            
            file_op = open(file, "rb")  
            file_read = file_op.read()
            
        except:
            print("ERROR READ OR WRITE")

    try:
        time.sleep(0.1)
        conn.send(file_read)
        conn.send(b'stop')
    except Exception as e:

        #print('ERROR SEND')
        print(e)
    
# conn.close()
# pi.stop()
