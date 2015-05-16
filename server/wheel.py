#!/usr/bin/env python
# -*- coding: utf8 -*-

import RPi.GPIO as GPIO

""" The control of two wheels

The control on board:

         ena in1 in2
forward    1   1   0
backward   1   0   1
stop       1   0   0

"""
class Wheel:

    def __init__(self, ena, in1, in2):
        self.ena = ena
        self.in1 = in1
        self.in2 = in2

        GPIO.setup(ena, GPIO.OUT)
        GPIO.setup(in1, GPIO.OUT)
        GPIO.setup(in2, GPIO.OUT)

        self.stop()


    def stop(self):
        GPIO.output(self.ena, True)
        GPIO.output(self.in1, False)
        GPIO.output(self.in2, False)


    def forward(self):
        GPIO.output(self.ena, True)
        GPIO.output(self.in1, True)
        GPIO.output(self.in2, False)


    def backward(self):
        GPIO.output(self.ena, True)
        GPIO.output(self.in1, False)
        GPIO.output(self.in2, True)
