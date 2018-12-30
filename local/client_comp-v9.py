import cv2
import socket
import time
import os
print(1)
a = 0
file = "test0.jpg"
Reserv = "Reserv.jpg"
err = 0
sock = socket.socket()
im=cv2.imread('1.jpg')
while err == 0:
    try:
        sock.connect(('192.168.43.237', 9001))
        err = 1
        print('connect')

    except:
        pass

image_result = open(file, 'wb')

image = bytes('', 'utf-8')
print(2)

def b_left():
    print('left')
    sock.send(bytes('left', 'utf-8'))


def b_right():
    print('right')
    sock.send(bytes('right', 'utf-8'))


def b_up():
    print('up')
    sock.send(bytes('up', 'utf-8'))


def b_stop():
    print('stop')
    sock.send(bytes('stop', 'utf-8'))


def b_down():
    print('down')
    sock.send(bytes('down', 'utf-8'))


def b_plus():
    print('+')
    sock.send(bytes('+', 'utf-8'))


def b_minus():
    print('-')
    sock.send(bytes('-', 'utf-8'))


data_1 = bytes('', 'utf-8')
i = 0
num=0
while True:
    #cv2.imshow('l',im)
    #num = cv2.waitKey(33)
    #print(num)
    if num == 52:  # left arrow
        b_left()
    if num == 54:  # right arrow
        b_right()
    if num == 56:  # up arrow
        b_up()
    if num == 50:  # down arrow
        b_down()
    if num == 53:  # central button
        b_stop()
    if num == 45:  # -
        b_minus()
    if num == 43:  # +
        b_plus()
    if num == 27:  # escape
        sock.close()

    file = "test0.jpg"
    try:
        image_result = open(file, 'wb')
    except:
        image_result = open('err.jpg', 'wb')
    image = bytes('', 'utf-8')
    data = bytes('', 'utf-8')
    # print(1)

    # i+=1
    while bytes('stop', 'utf-8') not in data:

        data = sock.recv(1024)
        image_result.write(data)
        print('not ')
    if bytes('stop', 'utf-8') in data:

        image_result.write(data[:data.index(bytes('stop', 'utf-8'))])

        data_1 = data[data.index(bytes('stop', 'utf-8')) + 4:]

        image_result.close()
        if os.path.getsize(file) > 500:

            img = cv2.imread(file)

            try:
                print('>500 Ok')
                cv2.imshow('Transport', img)
                num = cv2.waitKey(33)


            except:
                print('Error')

        else:
            print("STOP______________")

        file = "Number" + str(i) + ".jpg"
        image_result = open(file, 'wb')
        data = bytes('', 'utf-8')
        i+=1
        print(7)
        image_result.write(data_1)
        data_1 = bytes('', 'utf-8')
        a = 0
