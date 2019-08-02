#!/usr/local/bin/python3.6
# coding:utf-8
# @Time    : 2019/8/1 11:25
# @Author  : ZhangBing
# @Email   : 18829272841@163.com
# @File    : linkfile.py
# @Software: PyCharm
# 链表相关配置
class Node:
    def __init__(self, value, next=None, prev=None):
        self.vaule = value
        self.next = next
        self.prev = prev

    def __repr__(self):
        return str(self.vaule)

    def __str__(self):
        return str(self.vaule)


class Nodes:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        self.lst = []

    def apppend(self, value):
        prev = self.tail  # 定义之前的结尾
        node = Node(value)  # 此处获取Node的值
        if prev is None:  # 表明此处无元素
            self.head = node
        else:  # 表明有元素，则
            prev.next = node
            node.prev = prev
        self.tail = node
        self.lst.append(node)

    def iternodes(self, reverse=False):
        current = self.head if reverse else self.tail
        print('head', self.head, self.tail)
        while current:
            yield current
            current = current.next if reverse else current.prev


if __name__ == "__main__":
    l1 = Nodes()

    l1.apppend(10)
    l1.apppend(20)
    l1.apppend(30)

    for word in l1.iternodes():
        print(word)
