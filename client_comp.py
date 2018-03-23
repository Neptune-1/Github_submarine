import cv2
import socket
import time
import os
from random import randint
import tkinter as tk
a=0
file="test0.jpg"
Reserv="Reserv.jpg"
sock = socket.socket()
sock.connect(('stena.asuscomm.com',35001))
image_result = open(file, 'wb')

image=bytes('','utf-8')  

root=tk.Tk()
up_frame = tk.Frame(root)
up_frame.pack()
frame = tk.Frame(root)
frame.pack()
bot_frame=tk.Frame(root)
bot_frame.pack()

left_but = tk.Button(frame, text="←", fg="blue")
left_but.pack( side = 'left')

stop_but = tk.Button(frame, text="○", fg="blue")
stop_but.pack(side = 'left')

right_but = tk.Button(frame, text="→", fg="blue")
right_but.pack( side = 'right')

down_but = tk.Button(bot_frame, text="↓", fg="blue")
down_but.pack( side = 'bottom')

up_but = tk.Button(up_frame, text="↑", fg="blue")
up_but.pack( side = 'bottom')

def b_left(event):
    print('left')
    sock.send(bytes('left','utf-8'))
def b_right(event):
    print('right')
    sock.send(bytes('right','utf-8'))
def b_up(event):
    print('up')
    sock.send(bytes('up','utf-8'))
def b_stop(event):
    print('stop')
    sock.send(bytes('stop','utf-8'))
def b_down(event):
    print('down')
    sock.send(bytes('down','utf-8'))
      
left_but.bind('<Button-1>', b_left  )
right_but.bind('<Button-1>', b_right)
up_but.bind('<Button-1>', b_up      )
stop_but.bind('<Button-1>', b_stop  ) 
down_but.bind('<Button-1>', b_down  )

data_1=bytes('','utf-8')
global i
i=0

def dat():
      
      file="test0.jpg"
      image_result = open(file, 'wb')
      image=bytes('','utf-8')  
      data =bytes('','utf-8')
      print(1)
      left_but.bind('<Button-1>', b_left  )
      right_but.bind('<Button-1>', b_right)
      up_but.bind('<Button-1>', b_up      )
      stop_but.bind('<Button-1>', b_stop  ) 
      down_but.bind('<Button-1>', b_down  )

      
     # i+=1
      while bytes('stop','utf-8') not in data:
          data = sock.recv(1024)    
          image_result.write(data)
          print("not")
      if bytes('stop','utf-8')  in data:
            
            image_result.write(data[:data.index(bytes('stop','utf-8'))])
            
            data_1=data[data.index(bytes('stop','utf-8'))+4:]
            
            image_result.close()
            if os.path.getsize(file)>500:
                
                img = cv2.imread(file)
    
                try:
                    print('>50 Ok')
                    cv2.imshow('Transport',img)
    
                    cv2.waitKey(1)
                except:
                      print('Error')
                 #   print(data)
                  #  print("""


#""")
                    
                  #  print(data[:data.index(bytes('stop','utf-8'))])
                   # print("""


#""")
                #    print(data[data.index(bytes('stop','utf-8'))+4:])
                
                    #file="Number"+str(1)+".jpg"
                    #image_result = open(file, 'wb')
                    #data=bytes('','utf-8')
                   # i+=1
                    
                    #data_1=bytes('','utf-8')
                    #break
                   
            else:
                  print("STOP______________")
                  
            file="Number"+str(1)+".jpg"
            image_result = open(file, 'wb')
            data=bytes('','utf-8')
           # i+=1
            print(7)
            image_result.write(data_1)
            data_1=bytes('','utf-8')
            a=0
      root.after(500, dat)
     
      
      
          
root.after(500, dat)

root.mainloop()

