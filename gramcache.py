#!/usr/local/bin/python3.6
# coding:utf-8
# @Time    : 2019/8/1 17:09
# @Author  : ZhangBing
# @Email   : 18829272841@163.com
# @File    : gramcache.py
# @Software: PyCharm
# 代码缓存相关配置
import time
import datetime
import inspect
import functools


# 添加时间管理配置
def times(fn):
    @functools.wraps(fn)
    def __wapper(*args, **kwargs):
        start_time = datetime.datetime.now()
        ret = fn(*args, **kwargs)
        print("{} 函数执行时间为:{}".format(fn.__name__, (datetime.datetime.now() - start_time).total_seconds()))
        return ret

    return __wapper


# 添加缓存管理函数
def cache_local(tim):
    def __cache_local(fn):
        cache_dict = {}

        @functools.wraps(fn)
        def __wapper(*args, **kwargs):
            buffer = []
            for k, v in cache_dict.items():
                _, dat = v
                if (datetime.datetime.now().timestamp() - dat) >= tim:  # 此处字典不能被删除，因为其是在运行状态，若删除，则会报错
                    buffer.append(k)
            for i in buffer:
                cache_dict.pop(i)
            param_keys = {}
            param = inspect.signature(fn).parameters  # 获取字典
            lst_param = tuple(param.keys())  # 此处存储形参集合
            for k, v in enumerate(args):
                param_keys[lst_param[k]] = v
            param_keys.update(kwargs)
            for i in lst_param:
                if i not in param_keys.keys():
                    param_keys[i] = param[i].default
            key = tuple(sorted(param_keys.items()))  # 此处返回形参和实参的元组的集合
            if key not in cache_dict.keys():
                ret = fn(*args, **kwargs)
                cache_dict[key] = (ret, datetime.datetime.now().timestamp())
            return cache_dict[key]

        return __wapper

    return __cache_local


if __name__ == "__main__":
    @times
    @cache_local(5)
    def add(x, y, z=10):
        time.sleep(3)
        return x + y + z


    print(add(3, 4))
    print('------------------')
    print(add(3, 4))

    print(add(3, 4, z=10))
    print('*********************')
    time.sleep(5)
    print(add(3, 4, z=10))
