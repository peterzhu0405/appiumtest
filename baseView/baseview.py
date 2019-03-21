#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/21 下午3:57
# @Author  : jaingtao.zhu
# @File    : baseview.py
class BaseView(object):
    def __init__(self,driver):
        self.driver=driver

    def find_element(self,*loc):
        return self.driver.find_element(*loc)

    # 获取list列表
    def find_elements(self,*loc):
        return self.driver.find_elements(*loc)
    # 获取屏幕尺寸
    def get_window_size(self):
        return self.driver.get_window_size()
    # 滑动方法的封装  duration  滑动持续的时间
    def swipe(self,start_x, start_y, end_x, end_y, duration):
        return self.driver.swipe(start_x, start_y, end_x, end_y, duration)


