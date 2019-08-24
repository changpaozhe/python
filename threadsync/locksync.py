#!/usr/local/bin/python3.6
#coding:utf-8
# @Time    : 2019/8/24 15:04
# @Author  : ZhangBing
# @Email   : 18829272841@163.com
# @File    : locksync.py
# @Software: PyCharm
import  threading
import logging
import  time
logging.basicConfig(level=logging.INFO,format="%(asctime)s %(threadName)s %(message)s")
event=threading.Event()
class  dispatcher:
    def __init__(self):
        self.data=0
        self.lock=threading.Lock()
    def addr(self):
        with  self.lock:
            self.data+=1
    def subr(self):
        with  self.lock:
            self.data-=1
    @property
    def  value(self):
        return self.data
def  add(d:dispatcher,task:int=100):
    for i in range(task):
        for   j  in  range(-50,50):
            if j <0:
                d.subr()
            else:
                d.addr()
if __name__ == "__main__":
    c1 = 5
    c2 = 10000
    d = dispatcher()

    for i in range(c1):
        threading.Thread(target=add, args=(d, c2)).start()
    while True:
        time.sleep(0.5)
        if threading.active_count() == 1:
            logging.info(threading.enumerate())
            logging.info(d.value)
            break
        logging.info(threading.enumerate())