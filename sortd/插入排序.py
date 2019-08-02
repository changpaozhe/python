#!/usr/local/bin/python3.6
#coding:utf-8
# @Time    : 2019/8/2 15:49
# @Author  : ZhangBing
# @Email   : 18829272841@163.com
# @File    : 选择排序法.py
# @Software: PyCharm
import  random
l1=[random.randint(0,100)  for  i in range(10)]
'''
哨兵相关
4 5 3 2 10  
首位添加 
0  4  5  3   2   10  
第一次 
5   4   5  3  2 10   # 将源列表的第二个元素替换到哨兵位，并和列表的前面的第一位进行比较，若哨兵位大，则不移动
若哨兵位小，则将其移动到前面，此处哨兵位大，不移动 

3   4   5  3  2  10  # 将源列表的第三个元素替换到哨兵位，并和列表的前两个元素进行比较，若哨兵位小，则依次和前面的比较并得到相关结果

3   3  4  5  2  10  

2   2  3  4  5  10  
  
10   
'''
l2=[0]+l1
lenth=len(l2)
for  i in range(2,lenth):
    l2[0]=l2[i]  # 此处配置哨兵位
    j=i-1  # 此处是比较位的大小
    if  l2[j] > l2[0]: # 此处表示哨兵位小,需要向后排列
        while  l2[j] > l2[0]:
            l2[j+1]=l2[0]
            j-=1  # 此处是j 减少
        l2[j+1]=l2[0]
    l2.pop(0)
print (l2)






if __name__ == "__main__":
    pass