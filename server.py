import socket
import os
import time
sock_t = socket.socket()
sock_t.bind(('',9002))#назначается адресс и порт связи для ноутбука
sock_t.listen(1)
conn_t, addr_t = sock_t.accept()

sock_v = socket.socket()
sock_v.bind(('',9001))#назначается адресс и порт связи для лодки
sock_v.listen(1)
conn_v, addr_v = sock_v.accept()

data_v=bytes('','utf-8')
data_t=bytes('','utf-8')
while True:#бесконечный цикл отправки данных
    print("connected_video:",addr_v)
    
    print("connected_controllers:",addr_t)
    data_t=conn_t.recv(2048)
    conn_v.settimeout(0.5)
    datav=conn_v.recv(38)
    if not data_t :
        pass
    else:
        conn_v.send(data_t)#отправка данных
        data_t=bytes('','utf-8')
        
    if not data_v:
        pass
    else:
        conn_t.send(data_v)#отправка данных
        print(data_v)
        data_v=bytes('','utf-8')
conn.close()#никогда не наступающее закрытие соединения
    
