#!/usr/local/bin/python3.6
#coding:utf-8
# @Time    : 2019/8/24 16:18
# @Author  : ZhangBing
# @Email   : 18829272841@163.com
# @File    : semsync.py
# @Software: PyCharm
import  threading
import logging
logging.basicConfig(level=logging.INFO,format="%(asctime)s %(threadName)s %(message)s")
class  Pool:
    def __init__(self,count):
        self.count=count
        self.sem=threading.Semaphore(count)
        self.lst=[ i   for  i in  range(count)]
    def stop(self,data):
        self.sem.acquire()
        self.lst.append(data)
    def  start(self):
        self.sem.release()
        data=self.lst.pop()
        logging.info(data)
p=Pool(3)

p.start()
p.stop('aaaa')
p.stop('aaaa')
p.stop('aaaa')
p.stop('aaaa')








if __name__ == "__main__":
    pass