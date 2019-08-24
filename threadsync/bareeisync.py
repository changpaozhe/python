#!/usr/local/bin/python3.6
#coding:utf-8
# @Time    : 2019/8/24 15:56
# @Author  : ZhangBing
# @Email   : 18829272841@163.com
# @File    : bareeisync.py
# @Software: PyCharm
import  threading
import logging
import  time
import  random
logging.basicConfig(level=logging.INFO,format="%(asctime)s %(threadName)s %(message)s")
barr=threading.Barrier(parties=3)  # 此处相当于可以过多少人
event=threading.Event()
def  A(barr:threading.Barrier,data):
    logging.info("当前等待的线程数量为:{}".format(barr.n_waiting))
    try:
        barr.wait()
        logging.info(data)
    except  threading.BrokenBarrierError:
        logging.info("出现超时情况或者about情况下的处理数据为:{}".format(data))
for i in range(9):
    if  i==3:
        barr.abort()
    elif i==6:
        barr.reset()
    event.wait(2)
    threading.Thread(target=A,args=(barr,'122453453445345')).start()







if __name__ == "__main__":
    pass