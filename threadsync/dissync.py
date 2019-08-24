#!/usr/local/bin/python3.6
#coding:utf-8
# @Time    : 2019/8/24 15:20
# @Author  : ZhangBing
# @Email   : 18829272841@163.com
# @File    : dissync.py
# @Software: PyCharm
import  threading
import logging
import  time
import  random
logging.basicConfig(level=logging.INFO,format="%(asctime)s %(threadName)s %(message)s")
con=threading.Condition()
# 利用notify进行对线程的队列进行通知
# 通过wait进行阻塞
class   dispather:
    def  __init__(self,count=10):
        self.count=count
        self.data=0
        self.con=threading.Condition()
        self.event=threading.Event()
    def  producer(self):
        for i  in range(10):
            with  self.con:
                data=random.randint(1,100)
                self.data=data
                self.con.notify_all()
            self.event.wait(1)
    def  customer(self):
        while  True:
            with  self.con:
                self.con.wait()
                logging.info(self.data)
            self.event.wait(0.5)
a=dispather()
p=threading.Thread(target=a.producer,name="prode").start()
for  i in range(10):
    threading.Thread(target=a.customer,name="aaaaa").start()


if __name__ == "__main__":
    pass