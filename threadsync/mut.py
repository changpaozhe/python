#!/usr/local/bin/python3.6
#coding:utf-8
# @Time    : 2019/8/24 16:29
# @Author  : ZhangBing
# @Email   : 18829272841@163.com
# @File    : mut.py
# @Software: PyCharm
import  logging
import  threading
import time
import  queue
logging.basicConfig(level=logging.INFO,format="%(asctime)s  %(threadName)s %(message)s ")
import  datetime

def  cale():
    sum=0
    for _ in range(1000000000):
        sum+=1
start=datetime.datetime.now()
lst=[]
for  _ in range(5):
    t=threading.Thread(target=cale)
    t.start()
    lst.append(t)
   # t.join()  写在此处是线程会等待，其不会起头并进，形成了串行的结果
for  t  in lst:
    t.join() # 若没有join,则其不会等待，直接执行下面的结果，而不是等待上面的情况


delta=(datetime.datetime.now()-start).total_seconds()

print (delta)




if __name__ == "__main__":
    pass