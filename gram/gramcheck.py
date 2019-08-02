#!/usr/local/bin/python3.6
# coding:utf-8
# @Time    : 2019/8/1 16:56
# @Author  : ZhangBing
# @Email   : 18829272841@163.com
# @File    : gramcheck.py
# @Software: PyCharm
import inspect
import functools


def gramcheck(fn):
    def __wapper(*args, **kwargs):
        param = inspect.signature(fn).parameters  # 此处获取到类型和形参的字典集合
        lst_param = tuple(param.keys())  # 此处获取到的是形参的列表
        for k, v in enumerate(args):
            if not isinstance(v, param[lst_param[k]].annotation):
                raise Exception('ARGS Type  Error')
        for k, v in kwargs.items():  # 此处获取形参和实参列表
            if not isinstance(v, param[k].annotation):
                raise Exception('KWARGS  Type Error')
        ret = fn(*args, **kwargs)
        return ret

    return __wapper


if __name__ == "__main__":
    @gramcheck
    def add(x: int, y: int, a: int = 10, b: int = 20):
        return x + y + a + b


    print(add(20, 30, a='aa'))
