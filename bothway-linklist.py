#!/usr/local/bin/python3.6
# coding:utf-8
# @Time    : 2019/8/1 14:38
# @Author  : ZhangBing
# @Email   : 18829272841@163.com
# @File    : bothway-linklist.py
# @Software: PyCharm
# 双向链表相关配置信息处理
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

    def append(self, value):
        node = Node(value)
        current = self.tail
        if current is None:  # 此处表明是空链表
            # self.tail=node
            self.head = node  # 头部为node
        else:
            current.next = node  # 之前的下一跳是当前
            node.prev = current  # 现在的前一个是之前
        self.tail = node

    def iternodes(self, reverse=True):  # 遍历服务
        current = self.head if reverse else self.tail
        while current:
            yield current
            current = current.next if reverse else current.prev

    def insert(self, index, value):  # 此处获取对应的值需要上述的协助处理
        node = Node(value)  # 此处获取值
        if index < 0:
            raise Exception('Index  Error')
        if self.tail is None:
            self.append(node)
            self.head = node
            self.tail = node
        for k, current in enumerate(self.iternodes()):  # 此处返回为索引和对应值的元组集合
            if k == index:  # 此时找到index和key对应关系，进行处理
                prev = current.prev
                if current.prev is None:  # 表明是起始
                    self.head = node
                    node.next = current
                    current.prev = node
                else:
                    node.prev = prev
                    node.next = current
                    prev.next = node
                    current.prev = node
                    return
        else:  # 此处是尾部追加
            self.tail.next = node
            node.prev = self.tail
            self.append(node)
            self.tail = node

    def remove(self, index):
        if index < 0:
            raise Exception('Index Error')
        if self.tail is None:
            raise Exception('Empty  Linklist')
        for k, current in enumerate(self.iternodes()):
            if index == k:
                prev = current.prev
                next = current.next
                if prev is None and next is None:  # 只有一个
                    self.tail = None
                    self.head = None
                elif prev is None:  # current在第一个
                    self.head = next
                    next.prev = None
                elif next is None:  # 在最后一个
                    self.tail = prev
                    prev.next = None
                else:  # 在中间
                    prev.next = next
                    next.prev = prev

    def pop(self):
        if self.tail is None:
            raise Exception('Empty  Linklist')
        if self.tail == self.head:
            self.head = None
            self.tail = None
            return
        current = self.tail
        prev = current.prev
        self.tail = prev
        prev.next = None


if __name__ == "__main__":
    l1 = Nodes()
    node = Node(1)
    l1.append(node)
    node = Node(2)
    l1.append(node)
    for word in l1.iternodes():
        print(word)
    print("代码追加正常")
    node = Node(1)
    l1.insert(1, node)
    node = Node(5)
    l1.insert(10, node)
    for word in l1.iternodes():
        print(word)
    print("插入代码正常")

    l1.remove(0)
    l1.remove(2)
    for word in l1.iternodes():
        print(word)
    print("REMOVE 正常")
    node = Node(10)
    l1.append(node)
    node = Node(20)
    l1.append(node)
    l1.pop()
    l1.pop()
    for word in l1.iternodes():
        print(word)
    print("代码POP 正常")
