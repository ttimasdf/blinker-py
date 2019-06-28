#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Blinker import Blinker, BlinkerButton, BlinkerNumber
from Blinker.BlinkerDebug import *
import random

auth = 'a3ed8e406003'

BLINKER_DEBUG.debugAll()

Blinker.mode("BLINKER_WIFI")
Blinker.begin(auth)

button1 = BlinkerButton("btn-abc")
number1 = BlinkerNumber("num-abc")

counter = 0

def button1_callback(state):
    """ """

    BLINKER_LOG('get button state: ', state)

    button1.icon('icon_1')
    button1.color('#FFFFFF')
    button1.text('Your button name or describe')
    button1.print(state)

def data_callback(data):
    global counter
    
    BLINKER_LOG("Blinker readString: ", data)
    counter += 1
    number1.print(counter)

def dataStorage():
    Blinker.dataStorage("data1", random.randint(0,120))
    Blinker.dataStorage("data2", random.randint(0,120)/0.5)

button1.attach(button1_callback)
Blinker.attachData(data_callback)
Blinker.attachDataStorage(dataStorage)

if __name__ == '__main__':

    while True:
        Blinker.run()
