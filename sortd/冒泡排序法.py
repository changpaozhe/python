#!/usr/local/bin/python3.6
#coding:utf-8
# @Time    : 2019/8/2 15:09
# @Author  : ZhangBing
# @Email   : 18829272841@163.com
# @File    : 冒泡排序法.py
# @Software: PyCharm
# 核心思想，两两比较，大的放置在后面
import  random
'''
1 46 89  8932  3  356  45 

第一轮 
    1  46   89   8932  3  356  45  
    1  46   89   8932  3  356  45 
    1  46   89   8932  3  356  45 
    1  46   89    3   8932   356  45
    1  46   89    3   356    8932 45
    1  45   89     3  356    45  8932  
    总计 ： len(n)-1次 
第二轮
    1   45  89    3   356  45  8932 
    1   45  89   3  356  45  8932 
    1   45   3    89  356  45  8932 
    1   45   3    89  356  45  8932
    1   45   3    89   45  356  8932
    总计:len(n)-2 次 
    ...
    总是有最后一个数据不会被比较，因为一轮比较后已经找到最大的数据，就在最后面 
'''

# 原版
l1=[random.randint(0,100) for  i in range(10)   ]
for  i  in range(len(l1)):
    for j  in  range(len(l1)-i-1):
        if  l1[j] > l1[j+1]:
            l1[j],l1[j+1]=l1[j+1],l1[j]

print (l1)

# 升级版
l1=[random.randint(0,100) for  i in range(10)   ]
for  i  in range(len(l1)):
    flags=False
    for j  in  range(len(l1)-i-1):
        if  l1[j] > l1[j+1]: # 如果一直都没有进行数据交换操作，则表示前面一直比后面小，表明本身就是升序排列
            l1[j],l1[j+1]=l1[j+1],l1[j]
            flags=True
    if  not  flags:
        break
print (l1)


if __name__ == "__main__":
    pass