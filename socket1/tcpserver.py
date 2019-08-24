#!/usr/local/bin/python3.6
#coding:utf-8
# @Time    : 2019/8/24 8:45
# @Author  : ZhangBing
# @Email   : 18829272841@163.com
# @File    : tcpserver.py
# @Software: PyCharm
import  threading
import  socket
import  logging
import  time
logging.basicConfig(level=logging.INFO,format="%(asctime)s %(threadName)s  %(message)s")
class  ChatTcpServer:
    def __init__(self,ip='192.168.1.120',port=9999):
    # 记录数据结构，需要一个容器
        self.sock=socket.socket()
        self.addr=(ip,port)
        self.clients={} # 此处若需要分手，则可能会导致问题,客户端主动断开，可能会出现问题
        self.event=threading.Event()
    def start(self): #启动和创建连接listen
        self.sock.bind(self.addr)
        self.sock.listen()
        threading.Thread(target=self._accept,name="accept").start()

    def _accept(self):#建立连接，内部的方法
        while not self.event.is_set():  # 此处是接受一个，创建一个线程，接受一个，创建一个线程
            conn,client=self.sock.accept()
            self.clients[client]=conn  # 每链接一个就会有一个conn，一个全新的文件描述符
            threading.Thread(target=self._recv,args=(conn,client),name="recv").start()  # 此处要启线程的原因是recv会阻塞accept的链接

    def _recv(self,conn,client):  #分发，经过简单的处理并格式化处理，
        while  not self.event.is_set(): #此处若没set,则为False
            try:
                data=conn.recv(1024)
            except Exception  as e:
                logging.info(e)
                data=b"quit"
            data=data.decode()
            logging.info(data)
            # 客户端的退出机制
            if data == "quit":
                logging.info("........................quit")
                self.clients.pop(client)  #清除服务端数据
                conn.close()
                break   # 链接断开掉是不用分发的,此处线程就应该消亡了
            msg="ack {}".format(data)
            logging.info(msg)
            for conn  in  self.clients.values():
                conn.send(msg.encode())
    def stop(self):  #关闭和停止服务，终止服务
        for  c  in self.clients.values():  # 清理socket
            c.close()
        self.sock.close()
        self.event.wait(3)
        self.event.set()


if __name__ == "__main__":
    TCS=ChatTcpServer()
    TCS.start()