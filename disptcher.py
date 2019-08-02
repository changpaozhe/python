#!/usr/local/bin/python3.6
# coding:utf-8
# @Time    : 2019/8/1 16:21
# @Author  : ZhangBing
# @Email   : 18829272841@163.com
# @File    : disptcher.py
# @Software: PyCharm
class Disptcher:
    # 此处处理实例化及绑定相关事宜
    def defaultfun(self):
        print("defaultfunction")

    def __init__(self):
        pass

    def reg(self, cmd, fn):
        setattr(self, cmd, fn)

    def run(self):
        while True:
            cmd = input("请输入相关命令:")
            if cmd == 'q' or cmd == 'quit':
                break
            else:
                getattr(self, cmd, self.defaultfun)()


if __name__ == "__main__":
    #  此处使用settar 和 gettar 处理相关操作
    d1 = Disptcher()
    d1.reg('cmd1', lambda: print(1))
    d1.reg('cmd2', lambda: print(2))
    d1.reg('cmd3', lambda: print(3))
    d1.run()
