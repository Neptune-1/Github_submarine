import cv2
import socket
import time
import os


print(1)
a = 0
day=  '-'.join('_'.join(str(time.ctime()).split(' ')).split(':'))
os.mkdir(day)
file = "test0.jpg"
Reserv = "Reserv.jpg"
err = 0
sock = socket.socket()
im=cv2.imread('1.jpg')
while err == 0:
    try:
        sock.connect(('192.168.0.39', 9001))
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

def b_light():
    print('light')
    sock.send(bytes('light', 'utf-8'))

def b_shut():
    print('shut')
    sock.send(bytes('shut', 'utf-8'))


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
file='test3.jpg'
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
        b_shut()
    if num == 32:
        b_light()
    try:
        image_result = open(file, 'wb')
    except:
        image_result = open('err.jpg', 'wb')
    image = b''
    data = b''
    # print(1)

    # i+=1
    while b'stop' not in data:

        data += sock.recv(2**15)
        #image_result.write(data)
        print('not ')
    if b'stop' in data:
        image_result.write(data[:data.index(b'stop')])

        data_1 = data[data.index(b'stop') + 4:]

        image_result.close()
        if os.path.getsize(file) > 500:
            print(file,2)
            img = cv2.putText(cv2.imread(file,0), str(i) ,(30,100),cv2.FONT_HERSHEY_SIMPLEX, 1,(255,0,0),2)

            try :
                print('>500 Ok')
                cv2.imshow('Transport', img)
                num = cv2.waitKey(33)

            except Exception as e:
                print(e)
                #os.remove(file)

        else:
            print("STOP______________")
            #os.remove(file)
        file = day+'/'+ str(i) + ".jpg"
        image_result = open(file, 'wb')
        data = b''
        i+=1
        image_result.write(data_1)
        data_1 = b''
        a = 0
