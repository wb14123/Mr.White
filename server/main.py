#!/usr/bin/env python
# -*- coding: utf8 -*-

from car import Car
from flask import Flask
from flask.ext.cors import CORS
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

ena = 27
in1 = 4
in2 = 17
enb = 22
in3 = 2
in4 = 3

car = Car(ena, in1, in2, enb, in3, in4, 0.2)
app = Flask(__name__)
cors = CORS(app)

@app.route("/forward")
def forward():
    car.forward()
    return "ok"

@app.route("/backward")
def backward():
    car.backward()
    return "ok"

@app.route("/turn_left")
def turn_left():
    car.turn_left()
    return "ok"

@app.route("/turn_right")
def turn_right():
    car.turn_right()
    return "ok"

@app.route("/stop")
def stop():
    car.stop()
    return "ok"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
