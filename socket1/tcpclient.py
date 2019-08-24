#!/usr/local/bin/python3.6
#coding:utf-8
# @Time    : 2019/8/24 8:45
# @Author  : ZhangBing
# @Email   : 18829272841@163.com
# @File    : tcpclient.py
# @Software: PyCharm
import   socket
import  threading
import  logging
import  time
logging.basicConfig(level=logging.INFO,format="%(asctime)s %(threadName)s  %(message)s")
class  ChatTcpClient:
    def  __init__(self,ip='192.168.1.120',port=9999):
        self.addr=(ip,port)
        self.sock=socket.socket()
        self.event=threading.Event()
    def  start(self):
        logging.info("服务端断开测试1")
        self.sock.connect(self.addr)
        logging.info("服务端断开测试2")
        threading.Thread(target=self.__recv,name="recv").start()
    def send(self,data="quit"):
        self.sock.send(data.encode())
    def  __recv(self):
        while  not  self.event.is_set():
            try:
                data=self.sock.recv(1024)
            except  BaseException  as e:
                self.event.wait(10)
                logging.info("服务端主动断开")
                data="quit"
            if data.strip()=="quit":
                break
            logging.info(data.decode())
    def stop(self):
        self.event.set()
        self.sock.close()


if __name__ == "__main__":
    # pass
    TCC=ChatTcpClient()
    TCC.start()
    while True:
        cmd=input(">>>>>").strip()
        if  cmd=="quit":
            TCC.send('quit')
            TCC.stop()
            break
        TCC.send(cmd)
