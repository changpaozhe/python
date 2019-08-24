#!/usr/local/bin/python3.6
#coding:utf-8
# @Time    : 2019/8/24 13:43
# @Author  : ZhangBing
# @Email   : 18829272841@163.com
# @File    : eventsyn.py
# @Software: PyCharm
import  threading
import  logging
import datetime
logging.basicConfig(level=logging.INFO)
class Timers:
    def  __init__(self,interval,fn,*args,**kwargs):
        self.event=threading.Event()
        self.args=args
        self.kwargs=kwargs
        self.fn=fn
        self.interval=interval
    def start(self):
        threading.Thread(target=self.__run,name="run00").start()
    def __run(self):
        if  not  self.event.is_set():
            start = datetime.datetime.now()
            logging.info("启用")
            self.event.wait(self.interval)
            self.fn=self.fn(*self.args,**self.kwargs)
            logging.info("当前函数的运行时间为:{}  值为:{}".format((datetime.datetime.now()-start).total_seconds(),self.fn))
    def  cacel(self):
        self.event.set()

def add(x:int,y:int):
      return (x+y)
t=Timers(3,add,10,4)
t.start()









if __name__ == "__main__":
    pass