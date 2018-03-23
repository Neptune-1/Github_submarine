import socket
import os
import time
import cv2
import RPi.GPIO as GPIO

i=0
OK_send=0
OK_foto=0
file=""

cap=cv2.VideoCapture(0)#захват видео с камеры
sock = socket.socket()
sock.connect(('stena.asuscomm.com',35002))#назначается адресс и порт связи

#sock.setblocking(0)

#sock.settimeout(5)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
right_servo=GPIO.PWM(22,50)
left_servo=GPIO.PWM(27,50)
up_servo=GPIO.PWM(17,50)
down_servo=GPIO.PWM(23,50)
right_servo.start(7)
left_servo.start(7)
up_servo.start(7)
down_servo.start(7)

while True:#бесконечный цикл отправки и приема данных
    data=bytes('','utf-8')
   
    sock.setblocking(False)
    try:
        data=sock.recv(50)
        
    except:
        pass
    
    
    if data==bytes('left','utf-8'):
        right_servo .ChangeDutyCycle(4)
        left_servo .ChangeDutyCycle(4)
        print('left')
    elif data==bytes('right','utf-8'):
        right_servo.ChangeDutyCycle(11)
        left_servo .ChangeDutyCycle(11)
        print('right')
    elif data==bytes('up','utf-8'):
        up_servo.ChangeDutyCycle(4)
        down_servo .ChangeDutyCycle(4)
        print('up')
    elif data==bytes('down','utf-8'):
        up_servo.ChangeDutyCycle(11)
        down_servo .ChangeDutyCycle(11)
        print('down')
    elif data==bytes('stop','utf-8'):
        right_servo.ChangeDutyCycle(7)
        left_servo .ChangeDutyCycle(7)
        up_servo .ChangeDutyCycle(7)
        down_servo .ChangeDutyCycle(7)
        print('stop')
    
    file="Number"+str(1)+".jpg"#формирует название файла
    i+=1
    ret, im = cap.read()#считывание данных с камеры
    res = cv2.resize(im,(320,240))
    if data !=None:
        try:
            cv2.imwrite(file,res)
            file_op= open(file,"rb")#открытие созданного файла для записи данных с камеры
            file_read = file_op.read()
            #cv2.imshow('l',im)
            time.sleep(2)
        except:
            print("Error")
            
    try:
        sock.send(file_read)
        sock.send(bytes('stop','utf-8'))
        print(1)
    except:
        
        print(0)
conn.close()
