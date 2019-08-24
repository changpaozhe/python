#!/usr/local/bin/python3.6
#coding:utf-8
# @Time    : 2019/8/24 8:45
# @Author  : ZhangBing
# @Email   : 18829272841@163.com
# @File    : udpclient.py
# @Software: PyCharm
import  threading
import  socket
import  logging
import  time
logging.basicConfig(level=logging.INFO,format="%(asctime)s %(threadName)s  %(message)s")
class  ChatUdpClient:
    def __init__(self,ip='192.168.1.120',port=9998):
        self.addr=(ip,port)
        self.sock=socket.socket(type=socket.SOCK_DGRAM)
        self.event=threading.Event()
    def start(self):
        self.sock.connect(self.addr)
        threading.Thread(target=self.__recv,name="__recv").start()
    def  send(self,data="quit"):
        self.sock.sendto(data.encode(),self.addr)
    def  __recv(self):
        while  not  self.event.is_set():
            data,_=self.sock.recvfrom(1024)
            if data.decode().strip()=="quit":
                break
            logging.info(data.decode())
    def  stop(self):
        logging.info("关闭套接字")
        self.sock.close()
        self.event.set()

if __name__ == "__main__":
    CUC=ChatUdpClient()
    CUC.start()
    while True:
        cmd=input(">>>>>>").strip()
        if cmd=="quit":
            CUC.send()
            CUC.stop()
            break
        CUC.send(cmd)
