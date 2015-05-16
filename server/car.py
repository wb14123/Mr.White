#!/usr/bin/env python
# -*- coding: utf8 -*-

from wheel import Wheel
from threading import Timer

def __with_timer__(f):
    def wrapper(self):
        self.timer.cancel()
        self.timer = Timer(self.stop_wait, self.stop)
        self.timer.start()
        f(self)
    return wrapper

""" Control the car

The car will stop if it not receive command after stop_wait ms.

"""
class Car:

    def __init__(self, ena, in1, in2, enb, in3, in4, stop_wait):
        self.leftWheel = Wheel(ena, in1, in2)
        self.rightWheel = Wheel(enb, in3, in4)
        self.stop_wait = stop_wait
        self.timer = Timer(stop_wait, self.stop)
        self.timer.start()


    def stop(self):
        self.leftWheel.stop()
        self.rightWheel.stop()


    @__with_timer__
    def forward(self):
        self.leftWheel.forward()
        self.rightWheel.forward()


    @__with_timer__
    def backward(self):
        self.leftWheel.backward()
        self.rightWheel.backward()


    @__with_timer__
    def turn_left(self):
        self.leftWheel.backward()
        self.rightWheel.forward()


    @__with_timer__
    def turn_right(self):
        self.leftWheel.forward()
        self.rightWheel.backward()

