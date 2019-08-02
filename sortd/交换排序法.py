#!/usr/local/bin/python3.6
#coding:utf-8
# @Time    : 2019/8/2 15:29
# @Author  : ZhangBing
# @Email   : 18829272841@163.com
# @File    : 交换排序法.py
# @Software: PyCharm
'''
  34 5657  1 2334
  第一轮从中选择最大的，然后进行移动操作
  结果如下
  5657  34  1  2334
  第二轮
  5657  2334  34  1
  第三轮
  5657  2334   34  1
  完了
'''

import   random
l1=[random.randint(0,100) for  i in range(10)]
for  i  in  range(len(l1)-1):
    maxindex=i
    for  j in  range(i+1,len(l1)):
        if  l1[maxindex]  < l1[j]:
            maxindex=j # 此处返回的maxindex 已经是最大的maxindex
    if  maxindex !=i:  # 此处表明已经产生了maxindex和j的索引交换，但其并未产生真正的数据交换
        l1[maxindex],l1[i] = l1[i],l1[maxindex]  # 此处是将maxindex 替换到i，表示其是从大大小的顺序排列的
print (l1)

# 升级版
l1=[random.randint(0,100) for  i in range(10)]
for i in range(len(l1)//2):
    maxindex=i
    minindex=-i-1
    minorgin=minindex
    for j in range(i+1,len(l1)-i):
        if l1[maxindex]<l1[j]:
            maxindex=j
        if l1[minindex]>l1[-j-1]:
            minindex=-j-1
    if i != maxindex:
        l1[i],l1[maxindex]=l1[maxindex],l1[i]  # 上述中如果出现了1和1000之间的交换，则会导致下面的最小值成为了最大值，而真实的最小值则是I,此时的最大值索引（maxindex）成为了最小值，而i的索引成为了最大值。则需要判断i是否和minindex相等，
        if i == minindex  or i ==  len(l1)+minindex:   # maxindex和I 发生替换后，且i和minindex相等
            minindex=maxindex
    if minorgin !=minindex:
        l1[minindex],l1[minorgin]=l1[minorgin],l1[minindex]

print (l1)



if __name__ == "__main__":
    pass