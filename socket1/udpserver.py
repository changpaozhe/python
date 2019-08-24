#!/usr/local/bin/python3.6
#coding:utf-8
# @Time    : 2019/8/24 8:45
# @Author  : ZhangBing
# @Email   : 18829272841@163.com
# @File    : udpserver.py
# @Software: PyCharm
import  threading
import  socket
import  logging
import  time
logging.basicConfig(level=logging.INFO,format="%(asctime)s %(threadName)s  %(message)s")
class  ChatUdpServer:
    def __init__(self,ip='192.168.1.120',port=9998):
        self.addr=(ip,port)
        self.sock=socket.socket(type=socket.SOCK_DGRAM)
        self.event=threading.Event()
        self.clients=set()
    def  start(self):
        self.sock.bind(self.addr)
        self.event.wait(10)
        threading.Thread(target=self.__recv,name="__recv").start()
    def __recv(self):
        while  not self.event.is_set():
            data,remoteaddr=self.sock.recvfrom(1024)  # 此处会被阻塞
            self.clients.add(remoteaddr)
            try:
                data=data.decode()
            except  UnicodeDecodeError as e:
                logging.info("输入格式错误")
                data="quit"
            if  data.strip()=="quit":
                self.sock.sendto(data.encode(),address=remoteaddr)
                self.clients.remove(remoteaddr)
                continue
            logging.info(data)
            # data="ack  udp  {}".format(data)
            for  ad  in  self.clients:
                self.sock.sendto(data.encode(),ad)
    def stop(self):
        self.sock.close()
        self.event.set()


if __name__ == "__main__":
    # pass
    cus=ChatUdpServer()
    cus.start()